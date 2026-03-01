from django.db import models
from django.conf import settings


class Feedback(models.Model):
    CATEGORIES = [
        ('UI', 'UI/Layout Issue'),
        ('BUG', 'Technical Bug'),
        ('FEAT', 'Feature Request'),
        ('OTHER', 'General Feedback'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.CharField(max_length=5, choices=CATEGORIES, default='OTHER')
    message = models.TextField()
    # To catch the overlap bug :
    device_info = models.CharField(max_length=255, blank=True)
    screenshot = models.ImageField(upload_to='orlantech_feedback/screenshots/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    project_name = models.CharField(max_length=100, blank=True, default="Unknown Project")

    def __str__(self):
        return f"{self.category} - {self.created_at.strftime('%Y-%m-%d')}"