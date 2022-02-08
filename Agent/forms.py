from dataclasses import fields
from tkinter.ttk import Widget
from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields=['Name','mobile','email','City','State','lead_ref','Whatsappmobile','GST_NUM']
		widgets = {
			'Name' : forms.TextInput(attrs={'class':'form-control my-2','required':'required','placeholder':"Name Of client"}),
			'Whatsappmobile': forms.NumberInput(attrs={'class':'form-control my-2','required':'required', 'placeholder':" Whatsapp Number of client "}),
            'mobile' : forms.NumberInput(attrs={'class':'form-control my-2','required':'required', 'placeholder':"Mobile Number of client"}),
			'email': forms.EmailInput(attrs={'class':'form-control my-2','required':'required', 'placeholder':"Email id of client"}),
            'City' : forms.TextInput(attrs={'class':'form-control my-2','required':'required', 'placeholder':"City of client "}),
			'State' : forms.TextInput(attrs={'class':'form-control my-2','required':'required', 'placeholder':" State of client"}),
            'GST_NUM':forms.TextInput(attrs={'class':'form-control my-2','required':'required', 'placeholder':" GST number of client "}),
            'lead_ref':forms.Select(attrs={'class':'form-control my-2','required':'required', 'placeholder':"reference"}),
		}

class CustomerForm_update(forms.ModelForm):
	required_css_class='required-field'
	class Meta:
		model = Customer
		fields=['mobile','email','City','State','lead_ref','Whatsappmobile','GST_NUM',]
		widgets = {
			
			'Whatsapp Number': forms.NumberInput(attrs={'class':'form-control my-2','required':'required'}),
            'mobile' : forms.NumberInput(attrs={'class':'form-control my-2','required':'required'}),
			'email': forms.EmailInput(attrs={'class':'form-control my-2','required':'required'}),
            'Whatsappmobile' : forms.NumberInput(attrs={'class':'form-control my-2','required':'required'}),
            'City' : forms.TextInput(attrs={'class':'form-control my-2','required':'required'}),
			'State' : forms.TextInput(attrs={'class':'form-control my-2','required':'required'}),
            'GST_NUM':forms.TextInput(attrs={'class':'form-control my-2','required':'required'}),
            'lead_ref':forms.Select(attrs={'class':'form-control my-2','required':'required'}),
		}

class Service_Taken_Form(forms.ModelForm):
	class Meta:
		model = Services_taken
		fields=['Name','Start_date','End_date','GST','payment_reference_number','payment_mode','Service']
		widgets = {
			'Name' : forms.Select(attrs={'class':'form-control   my-2','required':'required'}),
            'Start_date' :DateInput(attrs={'class':'form-control   my-2','required':'required'}),
            'End_date' : DateInput(attrs={'class':'form-control   my-2','required':'required'}),
            'Service' : forms.Select(attrs={'class':'form-control   my-2','required':'required'}),
            'payment_reference_number' : forms.TextInput(attrs={'class':'form-control   my-2','required':'required','placeholder':"Add Payment reference number"}),
			'payment_mode':forms.Select(attrs={'class':'form-control   my-2','required':'required'}),
			'GST': forms.NumberInput(attrs={'class':'form-control   my-2','required':'required', 'placeholder':"Add Persent of GST 0-100"}),

		}

class Service_Taken_Form_update(forms.ModelForm):
	class Meta:
		model = Services_taken
		fields=['Start_date','End_date','GST','payment_reference_number','payment_mode']
		widgets = {
			'Start_date' :DateInput(attrs={'class':'form-control   my-2','required':'required'}),
            'End_date' : DateInput(attrs={'class':'form-control   my-2','required':'required'}),
            'payment_reference_number' : forms.TextInput(attrs={'class':'form-control   my-2','required':'required','placeholder':"Add Payment reference number"}),
			'payment_mode':forms.Select(attrs={'class':'form-control   my-2','required':'required'}),
			'GST': forms.NumberInput(attrs={'class':'form-control   my-2','required':'required', 'placeholder':"Add Persent of GST 0-100"}),
		}

class Services_Form(forms.ModelForm):
	class Meta:
		model = Services
		fields=['Service_Name','Charges']
		widgets = {
			'Service_Name' : forms.TextInput(attrs={'class':'form-control my-2','required':'required'}),
            'Charges':forms.NumberInput(attrs={'class':'form-control  my-2','required':'required'}),
            
		}


class AgentForm(forms.ModelForm):
	class Meta:
		model = Agent
		fields=['Agent_user','mobile']
		widgets = {
            'mobile':forms.NumberInput(attrs={'class':'form-control  my-2','required':'required'}),
		}



class Services_request_Form(forms.ModelForm):
	class Meta:
		model = Services_taken_request
		fields=['Service','Name']
		widgets = {
			'Service' : forms.Select(attrs={'class':'form-control  my-2','required':'required'}),
            'Name' : forms.Select(attrs={'class':'form-control  my-2','required':'required'}),
            
		}


class Service_trial_Taken_Form(forms.ModelForm):
	class Meta:
		model = Services_taken
		fields=['Start_date','End_date']
		widgets = {
            'Start_date' :DateInput(attrs={'class':'form-control my-2','required':'required'}),
            'End_date' : DateInput(attrs={'class':'form-control my-2','required':'required'}),

		}