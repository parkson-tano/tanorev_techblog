from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
app_name = 'review'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('<slug>', PostDetailView.as_view(), name='postdetail'),
    path('category/<slug:slug>', CategoryDetailView.as_view(), name='filter_category'),
    path('subcategory/<slug:slug>', SubCategoryDetailView.as_view(), name='filter_subcategory'),
    path('search/', SearchView.as_view(), name='search'),
    path('admins/create/', AdminPostCreateView.as_view(), name='create_post'),
    path('admins/<int:pk>/delete/', AdminPostDeleteView.as_view(), name='delete_post'),
    path('adminedit/<int:pk>/', AdminPostUpdateView.as_view(), name='edit_post'),
    path('admins/post', AdminPostListView.as_view(), name='list_post'),
]
