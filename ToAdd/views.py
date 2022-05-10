from django.shortcuts  import render, redirect, reverse

# Create your views here.
from django.http import HttpResponse
from ToAdd.models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


def index(request):
	return render(request, 'login.html')

def Login(request):
	if request.method =='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = authenticate(username = username, password = password)
		if user==None:
			return render(request, 'Register.html')
		login(request, user)
		taskinsert=ListTask.objects.filter(UserName=username)
		context={
		'task':taskinsert
		}
		return render(request, 'templates.html',context)

def afterlogin(request):
		error=request.GET.getlist('error')
		errmsg=""
		if error:
			errmsg="please enter the task before submit"

		username=request.GET.getlist('item')
		print(username[0])
		taskinsert=ListTask.objects.filter(UserName=username[0])
		context={
		'task':taskinsert,
		'error':errmsg
		}
		return render(request, 'templates.html',context)



def register(request):
	if request.method =='POST':
		username=request.POST.get('username')
		email=request.POST.get('email')
		password=request.POST.get('psw')
		hashedpsw=make_password(password)
		UserModel = get_user_model()
		user = UserModel.objects.create(username=username, password=hashedpsw)
		user.save()
		login(request, user)
		return render(request, 'sucess.html')
	else:
		return render(request, 'Register.html')


	

def Add(request):
	taskname=request.POST.get('TaskName')
	date=request.POST.get('Date')
	
	username=None
	if request.user.is_authenticated:
		username = request.user.username
	if not taskname:
		return redirect(('/afterlogin') + '?error=error'+'&'+'item='+username)
	if date=='':
		Taskinsert=ListTask(UserName=username,Task=taskname)
	else:
		Taskinsert=ListTask(UserName=username,Task=taskname,DueDate=date)
	Taskinsert.save()
	
	return redirect(('/afterlogin')+ '?item='+username)

def Delete(request,id):
	username=None
	if request.user.is_authenticated:
		username = request.user.username
	taskinsert=ListTask.objects.filter(id=id)
	taskinsert.delete()
	return redirect(('/afterlogin')+ '?item='+username)

def Update(request,id):
	if request.user.is_authenticated:
		username = request.user.username
	taskinsert=ListTask.objects.get(id=id)
	context={
	'taskinsert':taskinsert,
	}
	return render(request, 'Update.html',context)

def UpdateRecord(request,id):
	username=request.POST.get('Username')
	task=request.POST.get('Task')
	status=request.POST.get('Status')

	taskinsert=ListTask.objects.get(id=id)
	taskinsert.UserName=username
	taskinsert.Task=task
	taskinsert.Status=status
	taskinsert.save()
	return redirect(('/afterlogin')+ '?item='+username)
