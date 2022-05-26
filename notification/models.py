from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    def get_absolute_url(self):
        return f'/notification/{self.pk}/'
# Create your models here.
