from .models import Category, Post

def category_renderer(request):
    return {
       'all_categories': Category.objects.all(),
       'recent_post' : Post.objects.all().order_by('date_created')[:7]
    }