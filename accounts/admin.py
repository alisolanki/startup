from django.contrib import admin
from .models import UserProfile, RegisteredEvent

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(RegisteredEvent)

# class RegisteredEventInline(admin.StackedInline):
#     model = RegisteredEvent

# class UserProfileAdmin(admin.ModelAdmin):
#     inlines = [
#         RegisteredEventInline,
#     ]
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('category_name',)

# class RegisteredEventAdmin(admin.ModelAdmin):
#     list_display = ('category_name', 'item_name', 'item_description',)