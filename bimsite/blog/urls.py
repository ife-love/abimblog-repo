from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/<str:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/create', views.PostCreateView.as_view(), name='create-post'),
    path('post/update/<int:pk>/', views.PostUpdateView.as_view(), name='edit-post'),
    path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete-post'),
    path('post/add/category', views.AddCategoryView.as_view(), name='add-category'),


]