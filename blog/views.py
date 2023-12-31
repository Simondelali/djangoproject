from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.http import HttpResponse
# import csv, requests

# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# class export():

#     def posts_csv(request):
#         response = HttpResponse(content_type='text/csv')   
#         response['Content-Disposition'] = 'attachment; filename="posts.csv"'

#         # create the csv writer object
#         writer = csv.writer(response)

#         # desiqnate the model
#         posts = Post.objects.all()

#         # add column headings to the csv file
#         writer.writerow(['Title', 'content', 'Author', 'date posted'])

#         # add  data to csv file
#         for post in posts:
#             writer.writerow([post.title, post.content, post.author.username, post.date_posted])

#         return response
    
#     def fetch_data_from_api(request):

#         api_url = "https://randomuser.me/api/"

#         try:   
#             response = requests.get(api_url)

#             if response.status_code == 200:
#                 data = response.json()

#                 users = data.get('results', [])

#                 # Create an HttpResponse with content type 'text/csv'
#                 response = HttpResponse(content_type='text/csv')
#                 response['Content-Disposition'] = 'attachment; filename="users.csv"'

#                 # create the csv writer object
#                 writer = csv.writer(response)

#                 # add column headings to the csv file
#                 writer.writerow(['Gender', 'Name', 'location', 'Nationality'])

#                 # add  data to csv file

#                 for user in users:
#                     writer.writerow([user['gender'], user['name']['first'], user['location']['city'], user['nat']])
                
#                 return response
#             else:
#                 return HttpResponse('Error while fetching data from API', status=500)
            
#         except Exception as e:
#             return HttpResponse(f'Error at: {str(e)}', status=500)

class PostListView(ListView):   
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5



class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


    
class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        return super().form_valid(form)
    
    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'blog/about.html', {'title':'About'})