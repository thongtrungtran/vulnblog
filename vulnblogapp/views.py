from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.

# View for Home
class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-post_date']

# View for all categories
class CategoriesView(ListView):
    model = Category
    template_name = 'categories.html'
    ordering = ['name']

# View for a specific category
def CategoryView(request,cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'category.html',{'cats':cats.title().replace('-',' '), 'category_posts':category_posts})

# View for likes
def LikeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

# View for Article details
class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"

    
# View for adding posts
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

# View for adding categories
class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)        
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

# View for update post
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title','title_tag','body']

# View for delete post
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')