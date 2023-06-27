from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
class auth(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auth')
    is_admin = models.BooleanField(default=False)
    
from django.db import models
from accounts.models import auth
from django.contrib.auth.models import User

class customer(models.Model):
    orderedby = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateField()
    company = models.CharField(max_length=50, help_text="Only alphanumeric characters are allowed.")
    owner = models.CharField(max_length=50, help_text="Only alphanumeric characters are allowed.")
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    weight = models.FloatField()
    request_for_shipment = models.CharField(max_length=200)
    tracking_id = models.CharField(max_length=50)
    shipment_size = models.CharField(max_length=50, help_text="Format: L*B*H")
    box_count = models.IntegerField()
    specification = models.TextField()
    checklist_quantity = models.CharField(max_length=200)

    def __str__(self):
        return f"Order #{self.id}"
