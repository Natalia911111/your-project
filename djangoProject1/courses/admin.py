from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Subject)
class Subject(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug':('title',)}


class ModuleInline(admin.StackedInline):
    model = models.Module


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'created_at')
    list_editable = ('subject',)
    list_filter = ('created_at', 'subject')
    search_fields = ('title', 'overview')
    prepopulated_fields = {'slug':('title',)}
    inlines = (ModuleInline, )

