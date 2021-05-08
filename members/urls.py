from django.urls import path
from .views import UserRegisterView, UserEditView, ChangePasswordView, ShowProfileView, EditProfileView, CreateProfileView
from . import views

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    # path('login/',UserLoginView.as_view(),name='login')
    path('edit-settings/', UserEditView.as_view(), name='edit-settings'),
    path('password/', ChangePasswordView.as_view(), name='change-password'),
    path('password_success',views.password_success,name="password-success"),
    path('<int:pk>/profile', ShowProfileView.as_view(), name="show-profile"),
    path('<int:pk>/edit-profile', EditProfileView.as_view(), name="edit-profile"),
    path('create-profile/', CreateProfileView.as_view(), name="create-profile"),
]