from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    # email = models.EmailField()
    phone = models.PositiveIntegerField()
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
    
class Category(models.Model):
    category = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.category
    
CHARGE = (
    ('FREE', 'FREE'),
    ('PAID', 'PAID')
)

class Course(models.Model):
    instructor = models.ForeignKey(User, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.PositiveIntegerField()
    attended_no = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='course_image')
    cover_video = models.FileField(upload_to='course_video')
    charge = models.CharField(max_length=20, choices=CHARGE, default='FREE')

    def __str__(self):
        return self.course_name

class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    title = models.CharField(max_length=254, default="ok")
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.PROTECT)
    title = models.CharField(max_length=260)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    duration = models.DurationField()
    video =models.FileField(upload_to='lesson_video')

    def __str__(self):
        return self.title

PAYMENT_METHOD = (
    ('MTN MOBILE MONEY', 'MTN MOBILE MONEY'),
    ('ORANGE MONEY', 'ORANGE MONEY'),
    ('YUP', 'YUP'),
    ('VISA CARD', 'VISA CARD'),
    ('PAYPAL', 'PAYPAL')
)

    