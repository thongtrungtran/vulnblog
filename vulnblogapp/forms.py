from django import forms
from .models import Comment, Post,Category

# get category choices for selection in form
def getCategoryChoices():
    choices = Category.objects.all().values_list('name','name')
    choice_list = []
    for item in choices:
        choice_list.append(item)
    return choice_list


# Form for creating Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','snippet','body','header_image')
        choices = getCategoryChoices()
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag':forms.TextInput(attrs={'class': 'form-control'}),
            'author':forms.TextInput(attrs={'class': 'form-control','id':'post_author','value':'','type':'hidden'}),
            # 'author':forms.Select(attrs={'class': 'form-control'}),
            'category':forms.Select(choices=choices,attrs={'class': 'form-control'}),
            'snippet':forms.Textarea(attrs={'class': 'form-control'}),
            'body':forms.Textarea(attrs={'class': 'form-control'}),
        }


# Form for editting Post
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','category','snippet','body')
        choices = getCategoryChoices()
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag':forms.TextInput(attrs={'class': 'form-control'}),
            'category':forms.Select(choices=choices,attrs={'class': 'form-control'}),
            # 'author':forms.Select(attrs={'class': 'form-control'}),
            'snippet':forms.Textarea(attrs={'class': 'form-control'}),
            'body':forms.Textarea(attrs={'class': 'form-control'}),
        }

# Form for adding comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'body':forms.Textarea(attrs={'class': 'form-control'}),
        }