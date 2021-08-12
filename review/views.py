from django.shortcuts import render
from .models import Post
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView, UpdateView, ListView
from .models import Post, Category, SubCategory, Comment
from .forms import CommentForm, PostForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here
class NavbarView(TemplateView):
    template_name = 'base.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        subcat = SubCategory.objects.all()
        post = Post.objects.filter(status='published')

        context['post'] = post
        context['category'] = category
        context['subcat'] = subcat
        return context

class PostDetailView(TemplateView):
    template_name = 'post_detail.html'
    success_url = reverse_lazy('review:postdetail')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = kwargs['slug']

        form = CommentForm()

        post = Post.objects.get(slug=url_slug)
        comment = post.comment_set.all()
        category = Category.objects.all()
        post.view_count += 1
        post.save()
        context['category'] = category
        context["post"] = post 
        context['form'] = form
        context['comment'] = comment

        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = Post.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            comment = Comment.objects.create(
                name=name, email=email, content=content, post=post
            )

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)

class CategoryDetailView(TemplateView):
    template_name = 'category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = kwargs['slug']
        allcategory = Category.objects.all()
        category = Category.objects.get(slug=url_slug)
        subcategory = SubCategory.objects.filter(category=category)
        post = Post.objects.filter(category=category)
        context['subcategory'] = subcategory
        context['post'] = post
        context['ca'] = category
        return context

class SubCategoryDetailView(NavbarView):
    template_name = 'subcategory_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = kwargs['slug']
        category = Category.objects.all()
        subcategory = SubCategory.objects.get(slug=url_slug)
        post = Post.objects.filter(subcategory=subcategory)
        context['subcat'] = subcategory
        context['post'] = post
        context['category'] = category
        return context

class AdminPostCreateView(CreateView):
    template_name = 'admin/create.html'
    model = Post
    fields = "__all__"
    success_url = '/'

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

class SearchView(TemplateView):
    template_name = 'search_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET['keyword']
        result = Post.objects.filter(Q(title__icontains=kw) | Q(content__icontains=kw) | Q(excerpt__icontains=kw))
        context["result"] = result
        return context
    