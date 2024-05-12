from django.shortcuts import render,get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
def home(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def project(request):
    return render(request, 'main/project.html')

def project_detail(request):
    return render(request, 'main/project_detail.html')

def blog(request):
    blog = BlogModels.objects.order_by('-id')
    postingan_terbaru = BlogModels.objects.order_by('-id')[:4]
    kategori = CategoryBlogModels.objects.all()
    paginator = Paginator(blog, 2)
    page = request.GET.get('page')
    try:
        blog_items = paginator.page(page)
    except PageNotAnInteger:
        blog_items = paginator.page(1)
    except EmptyPage:
        blog_items = paginator.page(paginator.num_pages)

    context = {
        'blog': blog_items,
        'terbaru': postingan_terbaru,
        'kategori': kategori
    }
    return render(request, 'main/blog.html', context)

def search_blog(request):
    query = request.GET.get('query', '').strip()
    results = []

    if query:
        # Lakukan pencarian berdasarkan judul menggunakan filter
        blog_items = BlogModels.objects.filter(title__icontains=query)[:10]

        # Bentuk data hasil pencarian yang akan dikirim sebagai JSON
        results = [{'id': item.id,'image':item.image.url, 'title': item.title} for item in blog_items]

    return JsonResponse(results, safe=False)

def blog_by_category(request, category_id):
    category = get_object_or_404(CategoryBlogModels, pk=category_id)
    blog = BlogModels.objects.filter(category=category)
    postingan_terbaru = BlogModels.objects.order_by('-id')[:4]
    kategori = CategoryBlogModels.objects.all()

    paginator = Paginator(blog, 2)
    page = request.GET.get('page')
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)
    context = {
        'blog': blog,
        'category': category,
        'terbaru': postingan_terbaru,
        'kategori': kategori
    }
    return render(request, 'main/kategori.html', context)

def blog_detail(request, blog_id):
    blog_details = get_object_or_404(BlogModels, pk=blog_id)
    context = {
        'b': blog_details
    }
    return render(request, 'main/blog_detail.html', context)

def services(request):
    return render(request, 'main/services.html')

def credential(request):
    return render(request, 'main/credential.html')
