from django.shortcuts import render, get_object_or_404
from .models import Category, Post

# Create your views here.
def blog(request):
    posts = Post.objects.all()

    contexto = {
        'posts': posts
    }

    return render(request, 'blog/blog.html', contexto)


## Crear vista categoria
def category(request, category_id):
    #category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category, id = category_id)

    # Obtener post segun su categoria (filtrar)
    # posts = Post.objects.filter(categories = category)

    context = {
        'category': category,
        #'posts': posts
    }

    return render(request, "blog/category.html", context)