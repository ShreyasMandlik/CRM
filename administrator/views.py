from importlib.resources import contents
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth,Group
from django.contrib.auth import  authenticate,login,logout
from .models import Agent,Services
from django.contrib import messages
from administrator.decorator import *
from Agent.models import Customer,Services_taken,Services_taken_request
from Agent.forms import Services_Form,Service_Taken_Form,CustomerForm,Service_trial_Taken_Form
def home(request):
	return render(request,'administrator/Home.html')

@allowed_users(allowed_roles=['Administrator'])
@authenticated_user 
def administrator_home(request):
	Services_s=Services.objects.all()
	total_customer=Customer.objects.all().count()
	total_client=Customer.objects.filter(lead_status="Lead").count()
	user_a=User.objects.all()
	group = Group.objects.get(name='Agent')
	d=0
	for i in Services_s:
		a=0
		Services_taken_s=Services_taken.objects.filter(Service=i)
		d=d+1
		for j in Services_taken_s:
			a=a+1
		i.Sales_count=a
		i.save()
	for l in user_a:
		b=c=0
		try:
			Agents_a=Agent.objects.get(Agent_user=l)
			Customer_a=Customer.objects.filter(Agent_Name=Agents_a)
			for m in Customer_a:
				Services_taken_s=Services_taken.objects.filter(Name=m)
				b=b+1
				for n in Services_taken_s:
					c=c+1
			Agents_a.Client_count=b
			Agents_a.Sales_count=c
			Agents_a.save()
		except:
			pass
	Services_taken_request_b=Services_taken_request.objects.all()
	Agents_b=Agent.objects.all()
	context = {'Agents_b':Agents_b,'Services_s':Services_s,'total_customer':total_customer,'total_client':total_client,'d':d,'Services_taken_request_b':Services_taken_request_b}
	return render(request,'administrator/Administrator_home.html',context)
	
def logout_view(request):
	logout(request)
	return redirect('home')

@allowed_users(allowed_roles=['Administrator'])
def Agent_Signup(request):
	if request.method == 'POST':
		username = request.POST['username1'] 
		first_name = request.POST['First_name']
		last_name = request.POST['Last_name']
		email = request.POST['Email']
		password1 = request.POST['password']
		password2 = request.POST['password2']
		Mobile = request.POST['Mobile']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				return render(request,'administrator/Agent_Signup.html',{'i':'user already exsist'})
			else:
				users = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
				group = Group.objects.get(name= 'Agent')
				group.user_set.add(users)
				users.save()
				users_a = User.objects.get(username=username)
				Agent_n=Agent(Agent_user=users_a,mobile=Mobile,Client_count=0,Sales_count=0)
				Agent_n.save()
				return redirect('administrator_home')
		else:
			return render(request,'administrator/Agent_Signup.html',{'i':'Passwords are not same'})
	else:
		return render(request,'administrator/Agent_Signup.html')

def administrator_login(request):
	if request.method=='POST':
		username = request.POST['usernames']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request, user)
			return redirect('administrator_home')
		else:
			return render(request,'administrator/administrator_Signin.html',{'i':'Invalid username or Password'})

	else:
		return render(request,'administrator/administrator_Signin.html')


def administrator_Signup(request):
	if request.method == 'POST':
		first_name = request.POST['First_name']
		last_name = request.POST['Last_name']
		username = request.POST['username']
		email = request.POST['Email']
		password1 = request.POST['password']
		password2 = request.POST['password2']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				return render(request,'administrator/administrator_Signup.html',{'i':'user already exsist'})
			else:
				users = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
				group = Group.objects.get(name='Administrator')
				group.user_set.add(users)
				users.save()
				return redirect('administrator_home')
		return render(request,'administrator/administrator_Signup.html',{'i':'Passwords are not same'})
	else:
		return render(request,'administrator/administrator_Signup.html')


@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def service_add(request):
	form=Services_Form()
	if request.method == 'POST':
		form=Services_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('administrator_home')
		else:
			return render(request, 'administrator/administrator_service_add.html', {'i':'somthing went wrong'})
			
	context = {'form':form}
	return render(request, 'administrator/administrator_service_add.html', context)

@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def service_update(request,pk):
	service_u=Services.objects.get(id=pk)
	form=Services_Form(instance=service_u)
	if request.method == 'POST':
		form=Services_Form(request.POST,instance=service_u)
		if form.is_valid():
			form.save()
			return redirect('administrator_home')
	context = {'form':form}
	return render(request, 'administrator/administrator_service.html', context)

@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def service_delete(request,pk):
	Services_delete= Services.objects.get(id=pk)
	if request.method == "POST":
		Services_delete.delete()
		return redirect("administrator_home")
	context = {'Services_delete':Services_delete}
	return render(request, 'administrator/administrator_service_delete.html', context)

@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def approve_trial(request,pk):
	Services_taken_request_a=Services_taken_request.objects.get(id=pk)
	form=Service_trial_Taken_Form()
	if request.method == "POST":
		form=Service_trial_Taken_Form(request.POST)
		Services_taken_request_add=form.save(commit=False)
		Services_taken_request_add.Tot_payement=0
		Services_taken_request_add.Name=Services_taken_request_a.Name
		Services_taken_request_add.Service=Services_taken_request_a.Service
		Services_taken_request_add.save()
		Services_taken_request_a.delete()
		messages.info(request,'trial Approved')
		return redirect('administrator_home')
	context = {'form':form,'Services_taken_request_a':Services_taken_request_a}
	return render(request, 'administrator/Administartor_service_request.html', context)

@allowed_users(allowed_roles=['Administrator'])
@authenticated_user
def Delete_trial(request,pk):
	Services_taken_request_a=Services_taken_request.objects.get(id=pk)
	if request.method == "POST":
		Services_taken_request_a.delete()
		messages.info(request,'trial not Approved')
		return redirect('administrator_home')
	context = {'Services_taken_request_a':Services_taken_request_a}
	return render(request, 'administrator/Administartor_service_request_delete.html', context)

def validate_username(request):
	if request.method == 'GET':
		users = list(User.objects.values_list('username', flat=True)) 
		username = {'usernames':users}
		return JsonResponse(username)


