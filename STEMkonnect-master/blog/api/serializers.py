from rest_framework import serializers
from .models Category, Post, PostImage

class CategorySerializer(serializers.ModelSerializer): 
	class Meta:
		model = Category
		fields = ('id', 'title', 'slug')

class PostSerializer(serializers.ModelSerializer): 
	class Meta:
		model = Post
		fields = ('id', 'title', 'slug', 'image', 'author', 'body', 'publish', 'status')


class PostImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = PostImage 
		fields = ('id', 'file')