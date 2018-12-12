from django.db import models
from datetime import datetime
# Create your models here.
class Enquiry(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField(blank=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    enquiry_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name