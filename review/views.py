from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Admin
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView, UpdateView, ListView,FormView, View
from .models import Post, Category, SubCategory, Comment
from .forms import CommentForm, PostForm, AdminLoginForm, ContactForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
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
        post = Post.objects.filter(status='published')
        paginator = Paginator(post, 10)
        page_number = self.request.GET.get('page')
        post_list = paginator.get_page(page_number)
        context['post'] = post

        return context

class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    context_object_name = 'post'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments_connected = Comment.objects.filter(post=self.get_object()).order_by('-date_created')
        context["comments"] = comments_connected
        context['comment_form'] = CommentForm
        return context

    def post(self, request, *args, **kwargs):
        new_comment = Comment(content=request.POST.get('content'),
                                  name=request.POST.get('name'),
                                  email = request.POST.get('email'),
                                  post=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)

class SearchView(TemplateView):
    template_name = 'search_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET['keyword']
        result = Post.objects.filter(Q(title__icontains=kw) | Q(content__icontains=kw) | Q(excerpt__icontains=kw))
        context["result"] = result
        return context    

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

class SubCategoryDetailView(TemplateView):
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

class ContactView(CreateView):
	template_name = 'contact_us.html'
	form_class = ContactForm
	success_url = reverse_lazy('review:index')
	
	def get(self, request, *args, **kwargs):
		form = self.form_class
		return render(request, self.template_name, {'form': form})

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

class AdminPostCreateView(CreateView):
    template_name = 'admin/create.html'
    model = Post
    fields = ['author', 'category', 'subcategory', 'title', 'image_1', 'excerpt', 'content', 'status']
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


# class AdminLoginView(FormView):
# 	template_name = 'adminpages/adminlogin.html'
# 	form_class = AdminLoginForm
# 	success_url = reverse_lazy('review:adminhome')
# 	def form_valid(self, form):
# 		uname = form.cleaned_data.get('username')
# 		pword = form.cleaned_data.get('password')
# 		usr = authenticate(username=uname, password=pword)
# 		if usr is not None and Admin.objects.filter(user=usr).exists():
# 			login(self.request, usr)
# 		else:
# 			return render(self.request, self.template_name, {'form': self.form_class, 'error':'invalid creditials'})	


# 		return super().form_valid(form)

# 	def get_success_url(self):
# 		if 'next' in self.request.GET:
# 			next_url = self.request.GET.get('next')
# 			print(next_url)
# 			return next_url 	
# 		else:
# 			return self.success_url

# class AdminRequiredMixin(object):
# 	def dispatch(self, request, *args, **kwargs):
# 		if request.user.is_authenticated and Admin.objects.filter(user=request.user).exists():
# 			pass
# 		else:
# 			return redirect('/admin-login')

# 		return super().dispatch(request, *args, **kwargs)

# class AdminHomeView(AdminRequiredMixin, TemplateView):
# 	template_name = 'adminpages/adminhome.html'

# 	def get_context_data(self, **kwargs):
# 	    context = super().get_context_data(**kwargs)
# 	    context['post'] = [1,2,3]

# 	    return context

# class AdminLogoutView(View):
	
# 	def get(self, request):
# 		logout(request)
# 		return redirect('review:adminhome')	

# class AdminProductListView(AdminRequiredMixin, ListView):
# 	template_name = 'adminpages/adminproductlist.html'
# 	queryset = Post.objects.all().order_by('-id')
# 	context_object_name = 'allproducts'

# class AdminManageProductView(AdminRequiredMixin, View):
	
# 	def get(self, request, **kwargs):
# 		p_id = self.kwargs['p_id']
# 		action = request.GET.get('action')
# 		p_obj = Post.objects.get(id=p_id)
# 		p_obj.save()	

# 		if action == 'rmv':
# 			p_obj.save()
# 			p_obj.delete()
# 		else:
# 			pass
# 		return redirect('review:adminpostlist')

# class AdminProductEditView(AdminRequiredMixin, UpdateView):
# 	template_name = 'adminpages/adminproductedit.html'
# 	model = Post
# 	success_url = reverse_lazy('review:adminproductlist')
# 	fields = '__all__'

# class AdminProductdeleteView(AdminRequiredMixin, DeleteView):
# 	template_name = 'adminpages/product_confirm_delete.html'
# 	model = Post
# 	success_url = reverse_lazy('review:adminproductlist')