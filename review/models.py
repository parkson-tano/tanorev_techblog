from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
# Create your models here.

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
	first_name = models.CharField(max_length=256)
	email = models.EmailField(max_length=256, null=True, blank=True)
	message = models.TextField(null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.first_name

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name')
    image = models.ImageField(upload_to='cat_img', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='name')
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
    slug = AutoSlugField(populate_from='title')
    image_1 = models.ImageField(upload_to='post_image', null=True)
    excerpt = models.TextField(null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=30, choices=sta, default='published')
    # objects  = PostManager()
    
    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.post.title