from django.db import models


class RecogitoAnnotation(models.Model):
    re_id = models.CharField(max_length=100, primary_key=True)
    re_text = models.TextField(blank=True, null=True)
    re_start = models.IntegerField(blank=True, null=True)
    re_end = models.IntegerField(blank=True, null=True)
    re_payload = models.JSONField(blank=True, null=True)
    re_app = models.CharField(max_length=100, blank=True, null=True)
    re_model = models.CharField(max_length=100, blank=True, null=True)
    re_object_id = models.CharField(max_length=100, blank=True, null=True)
    re_field_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.re_text} ({self.re_id})"

    def save(self, *args, **kwargs):
        if self.re_payload:
            data = self.re_payload
            target = data['target']['selector']
            for y in target:
                if 'start' in y.keys():
                    self.re_start = y['start']
                    self.re_end = y['end']
                else:
                    self.re_text = y['exact']
        super().save(*args, **kwargs)
