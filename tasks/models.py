from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Urgent', 'Urgent'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=12, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='Pending')
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
