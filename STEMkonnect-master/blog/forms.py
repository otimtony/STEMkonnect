from django import forms
from .models import Event, Place, PostImage, Review
from taggit.models import Tag
from django.forms import ModelForm, Textarea


class PlaceForm(forms.ModelForm):
	class Meta:
		model = Place
		fields = [
				"name"
		]

class PostImageForm(forms.ModelForm):
	class Meta:
		model = PostImage
		fields = [
				"file",
		]

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = [
				"place",
				"name",
				"author",
				"image",
				"description",
				"publish",
				"status",
				"tags",
				
		]

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }

