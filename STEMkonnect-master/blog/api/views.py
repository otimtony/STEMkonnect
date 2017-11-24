
from .serializers import CategorySerializer, PostSerializer, PostImageSerializer
from rest_framework import generics
from ..models import Category, Post, PostImage



class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostImageListView(generics.ListAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer