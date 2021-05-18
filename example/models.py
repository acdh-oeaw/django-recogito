from django.db import models


class MyText(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title