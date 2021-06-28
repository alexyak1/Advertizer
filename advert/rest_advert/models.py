from django.db import models

class Ad(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=100, blank=False)
    body = models.TextField()
    price = models.DecimalField(null=True, blank=True, default=0.0, max_digits=11, decimal_places=2)
    email = models.EmailField(max_length=320)

    class Meta:
        ordering = ['created']
