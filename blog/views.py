from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator

# READ
def home(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})

# DETAIL READ
def detail(request, blog_id): #blog_id(1)를 넘겨받음
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog}) #blog를 blog라는 이름으로 detail.html이라는 그릇에 담을거야


# CREATE
def new(request):
    return render(request, 'new.html')


def create(request):
    new_blog = Blog() #빈 객체(Blog)를 만들겠다.
    new_blog.title = request.POST['title'] #손님이 요청
    new_blog.content = request.POST['content']
    new_blog.image = request.FILES.get('image')
    new_blog.save() #냉장고 매니저를 통해 저장
    return redirect('detail', new_blog.id) #detail은 url의 별명 (함수자체를 불러와야겠구나? 그러면 redirect)
    # return render(request, 'detail.html', {'blog': new_blog}) #render는 새로고침을 했을 때 url이 바뀌지 않음. html을 직접 받아서 사용하므로


# UPDATE
def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'edit_blog':edit_blog})


def update(request, blog_id):
    old_blog = get_object_or_404(Blog, pk=blog_id)
    old_blog.title = request.POST.get('title')
    old_blog.content = request.POST.get('content')
    old_blog.image = request.FILES.get('image')
    old_blog.save()
    return redirect('detail', old_blog.id)
    # return render(request, 'detail.html', {'blog': old_blog}) 


# DELETE
def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    return redirect('home')