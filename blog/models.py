from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'  # Fixed missing comma between code and label
        PUBLISH = 'PB', 'Publish'

    title = models.CharField(max_length=250)  # Fixed typo "max_lenght" to "max_length"
    slug = models.SlugField(max_length=250)  # Fixed typo "max_lenght" to "max_length"
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Fixed typo "setting" to "settings"
        on_delete=models.CASCADE,
        related_name='blog_posts'  # Renamed to plural for better readability
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)  # Fixed typo "dateTimefield" to "DateTimeField"
    created = models.DateTimeField(auto_now_add=True)  # Fixed capitalization issue "Create" to "created"
    updated = models.DateTimeField(auto_now=True)  # Fixed capitalization issue "update" to "updated"
    status = models.CharField(
        max_length=2,  # Fixed typo "max_lenght" to "max_length"
        choices=Status.choices,  # Used .choices to get choices from Status
        default=Status.DRAFT
    )
    
    class Meta:
        ordering = ['-publish']
        indexes = [
        models.Index(fields=['publish'])
        ]

    def __str__(self):  # Fixed typo "_str_" to "__str__"
        return self.title