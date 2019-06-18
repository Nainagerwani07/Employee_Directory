from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Employee_dir(models.Model):
	Emp_name=models.CharField("Employee Name",max_length=30,blank=False,null=True)
	Emp_phone_number = PhoneNumberField("Employee Phone Number",null=True, blank=True)
	Emp_Email=models.EmailField("Employee Email",max_length=70, null=True, blank=True, unique=True,)
	Emp_city=models.CharField("Employee City",max_length=30,blank=False,null=True)
	Emp_state=models.CharField("Employee State",max_length=30,blank=False,null=True)
	Emp_country=models.CharField("Employee Country",max_length=30,blank=False,null=True)
	Emp_date_of_joining = models.DateField("Employee Date of Joining",null=True, blank=True)
	Emp_Increment_Date=models.DateField("Employee Date of Increment", null=True, blank=True)
	Emp_Salary=models.IntegerField("Employee Salary",null=True,blank=True)

	def __str__(self):
		return self.Emp_name
	class Meta:
		ordering = ['-Emp_Salary']
		