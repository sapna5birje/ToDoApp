from ToAdd.models import *
from datetime import datetime, timedelta


def my_scheduled_job():
  yesterday = datetime.now() - timedelta(1)
  ydydate=datetime.strftime(yesterday, '%m-%d-%Y')
  taskinsert=ListTask.objects.filter(DueDate__lt=ydydate).exclude(Status='Completed').update(Expired=True)
  pass
  

  