from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_responded = models.BooleanField(default=False)
    reply = models.TextField(blank=True, null=True)  

    def __str__(self):
        return self.subject
