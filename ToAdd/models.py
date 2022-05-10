from django.db import models
import datetime
STATUS_CHOICES = (
    ('Pending', "Pending"),
    ('Inprogress', "Inprogress"),
    ('Completed', "Completed"),
   
)
# Create your models here.
class ListTask(models.Model):
 	UserName=models.CharField(max_length=250,null=True)
 	Task=models.TextField()
 	Status=models.CharField(max_length=250,choices=STATUS_CHOICES, default='Pending')
 	DueDate=models.DateField(blank=True,default=datetime.date.today)
 	Expired=models.BooleanField(default=False)
 	CreatedDate=models.DateTimeField(auto_now_add=True)
 	ModiefiedTime=models.DateTimeField(auto_now=True) 
