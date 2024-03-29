from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return  self.title

    class Meta:
        ordering = ('title',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Course(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,related_name='courses_creator')
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='courses')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    overview = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(get_user_model(), related_name='courses_students')
    course_image = models.ImageField(upload_to='courses')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Module(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='modules')

    def __str__(self):
        return self.title


class Content(models.Model):
    module = models.ForeignKey('Module', on_delete=models.CASCADE, related_name='contents')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={
        'models__in':('text', 'video', 'image', 'file')
    })
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type','object_id')





class ItemBase(models.Model):
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, related_name='%(class)s_related')
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Text(ItemBase):
    content = models.TextField()


class Video(ItemBase):
    content = models.URLField()


class File(ItemBase):
    content = models.FileField(upload_to='files')


class Image(ItemBase):
    content = models.ImageField(upload_to='images')

