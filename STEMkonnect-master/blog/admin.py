from django.contrib import admin
from .models import Place, Event, PostImage, Review

class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Place, PlaceAdmin)


class PostImageInline(admin.TabularInline):
	model = PostImage

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'location', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('name', 'body')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    inlines = [PostImageInline,]
  
admin.site.register(Event, EventAdmin)



class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('event', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']

admin.site.register(Review, ReviewAdmin)
