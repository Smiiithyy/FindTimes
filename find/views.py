from django.shortcuts import render, redirect

from .forms import BarForm, CommentForm

# Create your views here.
from .serializers import BarSerializer, CommentSerializer
from .models import Bar, Comment
from django.http import JsonResponse
from rest_framework import generics

from find import serializers
from django.views.decorators.csrf import csrf_exempt

# def bar_list(request): 
#     bars = Bar.objects.all()
#     return render(request, 'find/bar_list.html', {'bars': bars})

# def bar_detail(request, pk):
#     bar = Bar.objects.get(id=pk)
#     return render(request, 'find/bar_detail.html', {'bar': bar})

# def comment_list(request):
#     comments = Comment.objects.all()
#     return render(request, 'find/comment_list.html', {'comments': comments})

# def bar_create(request):
#     if request.method == 'POST':
#         form = BarForm(request.POST)
#         if form.is_valid():
#             bar = form.save()
#             return redirect('bar_detail', pk=bar.pk)
#     else:
#         form = BarForm()
#     return render(request, 'find/bar_form.html', {'form': form})

# def comment_create(request):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save()
#             return redirect('bar_detail', pk=comment.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'find/comment_form.html', {'form': form})

# def comment_edit(request, pk):
#     bar = Comment.objects.get(pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST, instance=bar)
#         if form.is_valid():
#             comment = form.save()
#             return redirect('bar_detail', pk=comment.pk)
#         # Need to fix
#     else:
#         form = CommentForm(instance=bar)
#     return render(request, 'find/comment_form.html', {'form': form})

# def bar_delete(request, pk):
#     Bar.objects.get(id=pk).delete()
#     return redirect('bar_list')

# def comment_delete(request, pk):
#     Comment.objects.get(id=pk).delete()
#     return redirect('bar_list')

# ____________


class BarList(generics.ListCreateAPIView): 
    queryset=Bar.objects.all()
    serializer_class = BarSerializer
    
class BarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bar.objects.all()
    serializer_class=BarSerializer
    
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer