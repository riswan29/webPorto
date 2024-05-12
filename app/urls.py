from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('contact/', views.contact, name='contact'),
    path('project/detail/', views.project_detail, name='detail'),
    path('blog/', views.blog, name='blog'),
    path('blog/detail/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('Blog/kategori/<int:category_id>/', views.blog_by_category, name='blog_by_category'),
    path('search/', views.search_blog, name='search_blog'),
    path('services/', views.services, name='services'),
    path('credential/', views.credential, name='credential')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
