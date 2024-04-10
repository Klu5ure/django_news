from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
# def index(request):
#     return HttpResponse('Hello world!')


# def index(request):
#     context = {
#         'news_list': [
#             {
#                 "title": "图雀写作工具推出了新的版本",
#                 "content": "随随便便就能写出一篇好教程，真的很神奇",
#             },
#             {
#                 "title": "图雀社区正式推出快速入门系列教程",
#                 "content": "一杯茶的功夫，让你快速上手，绝无担忧",
#             },
#         ]
#     }

#     return render(request, 'news/index.html', context=context)

def index(request):
    context = { 'news_list': Post.objects.all() }
    return render(request, 'news/index.html', context=context)

def create_post(request):
    new_post = Post(title="新的标题", content="新的内容")
    new_post.save()
    return HttpResponse("文章已创建")

def update_post(request, title, new_title):
    post = Post.objects.get(title = title)
    post.title = new_title
    post.save()
    return HttpResponse("文章已修改")

def delete_post(request, title):
    post = Post.objects.get(title=title)
    post.delete()
    return HttpResponse("文章已删除")

