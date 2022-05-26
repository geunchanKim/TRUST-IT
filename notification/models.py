from django.db import models


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    fromwho = models.CharField(max_length=10, blank=True)
    forwho = models.TextField(blank=True)
    how = models.TextField(blank=True)
    content = models.TextField(blank=True)
    #created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def get_absolute_url(self):
        return f'/notification/{self.pk}/'
# Create your models here.
