from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
import json
from .models import Post, Student

# Create your views here.
def index(request):
    return HttpResponse('Hello world!')


def list_students(request):
    students = Student.objects.all()
    student_list = [{'id': s.id, 'name': s.name, 'age': s.age} for s in students]
    return JsonResponse({'students': student_list})

def get_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return JsonResponse({'student': {'id': student.id, 'name': student.name, 'age': student.age}})

@require_http_methods(["POST"])
def create_student(request):
    try:
        name = request.POST.get('name')
        age = request.POST.get('age')
        student = Student(name=name, age=int(age))
        student.save()
        return JsonResponse({'status': 'success', 'id': student.id})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@require_http_methods(["PATCH"])
def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    try:
        name = request.POST.get('name')
        age = request.POST.get('age')
        if name:
            student.name = name
        if age:
            student.age = int(age)
        student.save()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
@require_http_methods(["DELETE"])
def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return JsonResponse({'status': 'success'})


def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        # 获取上传的图片文件对象
        image_file = request.FILES['image']
        
        # 保存图片到指定的目录中
        with open('E:/django/image.jpg', 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)
        
        # 返回JSON响应，或者做其他处理
        return JsonResponse({'message': 'Image uploaded successfully'})
    else:
        return JsonResponse({'error': 'No image uploaded'}, status=400)
    

    
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

# def index(request):
#     context = { 'news_list': Post.objects.all() }
#     return render(request, 'news/index.html', context=context)

# def create_post(request):
#     new_post = Post(title="新的标题", content="新的内容")
#     new_post.save()
#     return HttpResponse("文章已创建")

# def update_post(request, title, new_title):
#     post = Post.objects.get(title = title)
#     post.title = new_title
#     post.save()
#     return HttpResponse("文章已修改")

# def delete_post(request, title):
#     post = Post.objects.get(title=title)
#     post.delete()
#     return HttpResponse("文章已删除")

# def getStudent(request):
#     data = Student.objects.all()
#     print(data[0].name)
#     print('hello test')
#     return HttpResponse(data)
