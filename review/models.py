from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(upload_to='cat_img', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='subcat_img', blank=True, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    class PostManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    sta = (
        ('published', 'published'), 
        ('draft', 'draft'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, blank=True, null=True)
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=200, unique_for_date='date_created')
    excerpt = models.TextField(null=True, blank=True)
    content = models.TextField()
    sub_title_1 = models.CharField(max_length=256, blank=True, null=True)
    sub_content_1 = models.TextField(blank=True, null=True)
    file_1 = models.FileField(upload_to='files', blank=True, null=True)
    file_2 = models.FileField(upload_to='files', blank=True, null=True)
    image_1 = models.ImageField(upload_to="image", blank=True, null=True)
    image_2 = models.ImageField(upload_to='image', blank=True , null=True)
    url_1 = models.URLField(blank=True, null=True)
    url_2 = models.URLField(blank=True, null=True)
    sub_title_2 = models.CharField(max_length=256, blank=True, null=True)
    sub_content_2 = models.TextField(blank=True, null=True)
    file_3 = models.FileField(upload_to='files', blank=True, null=True)
    file_4 = models.FileField(upload_to='files', blank=True, null=True)
    image_3 = models.ImageField(upload_to="image", blank=True, null=True)
    image_4 = models.ImageField(upload_to='image', blank=True , null=True)
    url_3 = models.URLField(blank=True, null=True)
    url_4 = models.URLField(blank=True, null=True)
    sub_title_3 = models.CharField(max_length=256, blank=True, null=True)
    sub_content_3 = models.TextField(blank=True, null=True)
    file_5 = models.FileField(upload_to='files', blank=True, null=True)
    file_6 = models.FileField(upload_to='files', blank=True, null=True)
    image_5 = models.ImageField(upload_to="image", blank=True, null=True)
    image_6 = models.ImageField(upload_to='image', blank=True , null=True)
    url_5 = models.URLField(blank=True, null=True)
    url_6 = models.URLField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=30, choices=sta, default='published')
    # objects  = PostManager()
    
    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post