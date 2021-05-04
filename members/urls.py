from django.urls import path
from .views import UserRegisterView, UserEditView, ChangePasswordView
from . import views

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    # path('login/',UserLoginView.as_view(),name='login')
    path('edit-profile', UserEditView.as_view(), name='edit-profile'),
    path('password/', ChangePasswordView.as_view(), name='change-password'),
    path('password_success',views.password_success,name="password-success"),
]