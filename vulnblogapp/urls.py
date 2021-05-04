from django.urls import path
from .views import HomeView, ArticleDetailView,AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoriesView, LikeView

urlpatterns = [
    path('',HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add-post/',AddPostView.as_view(), name='add-post'),
    path('add-category/',AddCategoryView.as_view(), name='add-category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update-post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete-post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('categories/',CategoriesView.as_view(), name="categories"),
    path('like/<int:pk>',LikeView,name='like-post'),
]