from django.shortcuts import render
from .models import Post
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView, UpdateView, ListView
from .models import Post, Category, SubCategory, Comment
from .forms import CommentForm, PostForm
from django.urls import reverse_lazy
# Create your views here
class NavbarView(TemplateView):
    template_name = 'base.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context

class HomeView(NavbarView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = Post.objects.filter(status='published')
        return context

class PostDetailView(TemplateView):
    template_name = 'post_detail.html'
    forms_class = CommentForm
    success_url = reverse_lazy('review:postdetail')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = kwargs['slug']
        post = Post.objects.get(slug=url_slug)
        category = Category.objects.all()
        post.view_count += 1
        post.save()
        context['category'] = category
        context["post"] = post 

        return context

    def form_valid(self, form):
        return super().form_valid(form)

class CategoryDetailView(NavbarView):
    template_name = 'category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_id = kwargs['pk']
        category = Category.objects.get(pk=url_id)
        subcategory = SubCategory.objects.filter(category=url_id)
        post = Post.objects.filter(category=url_id)
        context['subcategory'] = subcategory
        context['post'] = post
        context['ca'] = category
        return context

class SubCategoryDetailView(NavbarView):
    template_name = 'subcategory_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_id = kwargs['pk']
        subcategory = SubCategory.objects.get(pk=url_id)
        post = Post.objects.filter(subcategory=url_id)
        context['subcat'] = subcategory
        context['post'] = post
        return context

class AdminPostCreateView(CreateView):
    template_name = 'admin/create.html'
    model = Post
    fields = "__all__"

    def get_queryset(self):
        author = self.request.user
        return super().get_queryset()
    
class AdminPostDeleteView(DeleteView):
    template_name = 'admin/delete.html'
    model = Post

class AdminPostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name='admin/postlist.html'

class AdminPostUpdateView(UpdateView):
    template_name = 'admin/post_update.html'
    model = Post
    fields = "__all__"

