from django.db import models
from django.db import models
from administrator.models import Services,Agent
from django.contrib.auth.models import User
# Create your models here.


CHOICES=(
	('Client','Client'),
	('Lead','Lead'),
	
)
CHOICE_Ref=	(('Website','Website'),
	('Social Media','Social Media'),
	('Marketing','Marketing'),
    ('Other','Other'),
)
CHOICE_Ref1=	(
    ('Gpay','Gpay'),
	('Bank Transfer','Bank Transfer'),
	('Paytm','Paytm'),
    ('Online Transfer',' Online Transfer'),
    ('Cash','Cash'),
    ('Other','Other'),
)

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50,null=True, blank=True)
    mobile = models.CharField(max_length=12,null=True, blank=True)
    Whatsappmobile = models.CharField(max_length=12,null=True, blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    City=models.CharField(max_length=50,null=True, blank=True)
    State=models.CharField(max_length=20,null=True, blank=True)
    GST_NUM=models.CharField(max_length=15,null=True, blank=True)
    lead_status=models.CharField(choices = CHOICES,max_length=10,default='Lead')
    Agent_Name=models.ForeignKey(Agent,on_delete=models.SET_NULL,related_name='agent_name',null=True, blank=True)
    lead_ref=models.CharField(choices = CHOICE_Ref,max_length=15,default='Social Media')
    def __str__(self):
        id_f=str(self.Name+"["+(str(self.id))+"]")
        return id_f


class Services_taken(models.Model):
    id = models.AutoField(primary_key=True)
    Name=models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='customer_name')
    Service=models.ForeignKey(Services, on_delete=models.CASCADE,related_name='Service_name')
    Start_date=models.DateField(null=True, blank=True)
    End_date=models.DateField(null=True, blank=True)
    GST=models.IntegerField(null=True, blank=True)
    days_left=models.DurationField(null=True, blank=True)
    Tot_payement=models.IntegerField(null=True, blank=True)
    payment_reference_number=models.CharField(max_length=125)
    payment_mode=models.CharField(choices = CHOICE_Ref1,max_length=50,default='Other')
    def __str__(self):
        id_s=str(self.Name.Name+ " [ "+self.Service.Service_Name+"("+(str(self.id))+") ]")
        return id_s


class Services_taken_request(models.Model):
    id = models.AutoField(primary_key=True)
    Service=models.ForeignKey(Services, on_delete=models.CASCADE,related_name='Service_name_request')
    Name=models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='customer_name_request')
    def __str__(self):
        id_s=str(self.Name.Name+ " [ "+self.Service.Service_Name+"("+(str(self.id))+") ]")
        return id_s
    