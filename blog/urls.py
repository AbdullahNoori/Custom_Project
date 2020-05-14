from django.urls import path
from blog.views import PageListView, PageDetailView, CreateBlogView, DeleteBlogView
from django.urls import path, include


urlpatterns = [
    
    path('', PageListView.as_view(), name='blog-list-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='blog-details-page'),
    path('new/blog/', CreateBlogView.as_view(), name='new-blog'),
    path('delete/blog/<str:slug>', DeleteBlogView.as_view(), name='delete-blog'),
    # path('update/blog/<str:slug>', UpdateBlogView.as_view(), name='update-blog'),
]