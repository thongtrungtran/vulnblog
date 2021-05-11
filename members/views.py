from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfileForm
from vulnblogapp.models import Profile

# Create your views here.

# View for registration
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

# View for updating account settings
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

# View for changing password
class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password-success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

# View for showing profile page
class ShowProfileView(generic.DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)        
        
        page_user = get_object_or_404(Profile,id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context
        

# View for updating profile 
class EditProfileView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = ['bio','profile_pic','website_url','facebook_url','twitter_url','instagram_url','pinterest_url']
    success_url = reverse_lazy('home')

# View for create user profile
class CreateProfileView(generic.CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/create_profile.html'
    # fields = '__all__'
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)