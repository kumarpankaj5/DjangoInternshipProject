# consumer_services/models.py
from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields as needed

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    ]
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)  # Add file upload field
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.request_type} - {self.submitted_at}"
