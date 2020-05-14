from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from blog.models import Blog
from .forms import BlogForm


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Blog

    def get(self, request):
        """ GET a list of Pages. """
        blogs = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': blogs
        })

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Blog

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        blog = self.get_queryset().get(slug__iexact=slug)

        return render(request, 'page.html', {
          'page': blog
        })
    
class CreateBlogView(CreateView):
  model = Blog

  def get(self, request):
    """ Returns a specific wiki page by slug. """
    form = BlogForm()

    return render(request, 'new.html', {
      'form': form
    })

  def post(self, request):
    if request.method == "POST":
      form = BlogForm(request.POST)
      
      if form.is_valid():
              
        blog = form.save(commit=False)
        blog.author = request.user
        blog.save()

        return render(request, 'page.html', {'page': blog})

    else:
      form = BlogForm()

    context = {'form': form}

    return render(request, 'new.html', context)

class DeleteBlogView(CreateView):
  def get(self, request, slug):
    pass

  def post(self, request, slug):
    if request.method == "POST":
      blog = Blog.objects.get(slug=slug)
      blog.delete()

      return HttpResponseRedirect(reverse('blog-list-page'))


# class UpdateBlogView(CreateView):
  # def get(self, request, slug):
    
  #   blog = Blog.objects.get(slug=slug)

  #   form = BlogForm(instance=blog)

  #   return render(request, 'new.html', {
  #     'form': form
  #   })

  # def post(self, request, slug):
  #   blog = Blog.objects.get(slug=slug)
  #   if request.method == "POST":
  #     form = BlogForm(request.POST)
      
  #     if form.is_valid():
              
  #       blog.title  = request.POST.get('title', '')
  #       blog.slug = request.POST.get('slug', '')
  #       blog.content = request.POST.get('content', '')
  #       blog.modified = request.POST.get('modified', '')
  #       blog.save()

  #       # return HttpResponseRedirect(reverse('blog-details-page', kwargs={'slug': blog.slug}))
  #       return render(request, 'page.html', {
  #         'page': blog
  #       })

  #   else:
  #     form = BlogForm()

  #   context = {'form': form}

  #   return render(request, 'new.html', context)
