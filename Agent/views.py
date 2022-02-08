from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth,Group
from django.contrib.auth import  authenticate,login,logout
from django.contrib import messages
from administrator.decorator import *
from administrator.models import Agent,Services
from Agent.forms import Services_Form,Service_Taken_Form,CustomerForm,CustomerForm_update,Services_request_Form,Service_Taken_Form_update
from .models import Customer,Services_taken,Services_taken_request
from datetime import datetime


@allowed_users(allowed_roles=['Agent'])
@authenticated_user
def Agent_home(request):
	users=request.user
	Agents_a=Agent.objects.get(Agent_user=users)
	Customer_a=Customer.objects.filter(Agent_Name=Agents_a)
	b=c=diff=0
	for m in Customer_a:
	
		Services_taken_s=Services_taken.objects.filter(Name=m)
		b=b+1
		for n in Services_taken_s:
			c=c+1
		Agents_a.Client_count=b
	Agents_a.Sales_count=c
	Agents_a.save()
	Services_takenc=Services_taken.objects.filter(Name__id__in=Customer_a.all())
	a = datetime.now().date()
	for i in Services_takenc:
		date_format = "%Y-%m-%d"
		b = datetime.strptime(str(i.End_date), date_format)
		a = datetime.strptime(str(datetime.now().date()), date_format)
		diff = b-a
		i.days_left=diff
		i.save()
	context = {'Customer_a':Customer_a,'Agents_a':Agents_a,'Services_takenc':Services_takenc}
	return render(request,'Agent/Agent_home.html',context)


def Agent_login(request):
	if request.method == 'POST':
		username = request.POST['usernames']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request, user)
			return redirect('Agent_home')
		else:
			return render(request,'Agent/Agent_Signin.html',{'i':'Invalid username or Password'})

	else:
		return render(request,'Agent/Agent_Signin.html')

@allowed_users(allowed_roles=['Agent'])
@authenticated_user
def client_add(request):
	form=CustomerForm()
	users=request.user
	Agents_a=Agent.objects.get(Agent_user=users)
	if request.method == 'POST':
		form=CustomerForm(request.POST)
		if form.is_valid():
		
			client_a=form.save(commit=False)
		
			client_a.Agent_Name=Agents_a
		
			client_a.save()
		
			messages.info(request,'Client Added')
			return redirect('Agent_home')
	context = {'form':form}
	return render(request, 'Agent/Client_add.html', context)


@allowed_users(allowed_roles=['Agent'])
@authenticated_user
def client_Update(request,pk):
	Customer_c=Customer.objects.get(id=pk)
	form=CustomerForm_update(instance=Customer_c)
	if request.method == 'POST':
		form=CustomerForm_update(request.POST,instance=Customer_c)
		if form.is_valid():
			form.save()
			messages.info(request,'Client Updated')
			print(1)
			return redirect('Agent_home')
	context = {'form':form,'Customer_c':Customer_c}
	return render(request, 'Agent/client_Update.html', context)

@allowed_users(allowed_roles=['Agent'])
@authenticated_user
def client_Delete(request,pk):
	Customer_c=Customer.objects.get(id=pk)
	if request.method == "POST":
		Customer_c.delete()
		messages.info(request,'Client Deleted')
		return redirect("administrator_home")
	context = {'Customer_c':Customer_c}
	return render(request, 'Agent/Agent_client_delete.html', context)


@allowed_users(allowed_roles=['Agent'])
@authenticated_user
def Service_taken_add(request):
	form=Service_Taken_Form()
	if request.method == 'POST':
		form=Service_Taken_Form(request.POST)
		if form.is_valid():
			Services_taken_add=form.save(commit=False)
			Services_taken_add.Tot_payement=(Services_taken_add.Service.Charges+(Services_taken_add.Service.Charges*(Services_taken_add.GST/100)))
			Related_customer=Services_taken_add.Name
			Services_taken_add.Name.lead_status='Client'
			Related_customer.save()
			Services_taken_add.save()
			messages.info(request,'Service saled added')
			return redirect('Agent_home')
	context = {'form':form}
	return render(request, 'Agent/Service_taken_add.html', context)

@allowed_users(allowed_roles=['Agent'])
@authenticated_user
def Service_taken_Update(request,pk):
	Services_taken_c=Services_taken.objects.get(id=pk)
	form=Service_Taken_Form_update(instance=Services_taken_c)
	if request.method == 'POST':
		form=Service_Taken_Form_update(request.POST,instance=Services_taken_c)
		if form.is_valid():
			Services_taken_add=form.save(commit=False)
			a=(Services_taken_add.Service.Charges+(Services_taken_add.Service.Charges*(Services_taken_add.GST/100)))
			Services_taken_add.Tot_payement=a
			Services_taken_add.save()
			messages.info(request,'Service Updated')
			return redirect('Agent_home')
	context = {'form':form,'Services_taken_c':Services_taken_c}
	return render(request, 'Agent/Service_taken_Update.html', context)

@allowed_users(allowed_roles=['Agent'])
@authenticated_user
def Service_taken_delete(request,pk):
	Services_taken_d=Services_taken.objects.get(id=pk)
	if request.method == "POST":
		service_count=Services_taken_d.Name
		Services_taken_d.delete()
		a=Services_taken.objects.filter(Name=service_count).count()
		if(a==0):
			service_count.lead_status='Lead'
			service_count.save()
		
		messages.info(request,'Service delete')
		return redirect("Agent_home")
	context = {'Services_taken_d':Services_taken_d}
	return render(request, 'Agent/Agent_service_delete.html', context)
	
@allowed_users(allowed_roles=['Agent'])
@authenticated_user
def Service_taken_request(request):
	form=Services_request_Form()
	if request.method == 'POST':
		form=Services_request_Form(request.POST)
		if form.is_valid():
			form.save()
			messages.info(request,'Service requested')
			return redirect('Agent_home')
	context = {'form':form}
	return render(request, 'Agent/Service_taken_request.html', context)
	
	



# def client_show(request):
# 	usernames=request.user
# 	Agent_a=Agent.objects.get(Agent_user=usernames)
# 	Customer_c=Customer.objects.filter(Agent_Name=Agent_a)
# 	return render(request,'Agent/client_show.html',{'Customer_c':Customer_c})

# def services_taken_show(request):
# 	usernames=request.user
# 	Agent_a=Agent.objects.get(Agent_user=usernames)
# 	Customer_c=Customer.objects.filter(Agent_Name=Agent_a)
# 	Services_takenc=Services_taken.objects.filter(Name__id__in=Customer_c.all())
# 	a = datetime.now().date()
# 	for i in Services_takenc:
# 		date_format = "%Y-%m-%d"
# 		b = datetime.strptime(str(i.End_date), date_format)
# 		a = datetime.strptime(str(datetime.now().date()), date_format)
# 		diff = b-a
# 		i.days_left=diff
# 		i.save()
# 	return render(request,'Agent/services_taken_show.html',{'Services_takenc':Services_takenc})