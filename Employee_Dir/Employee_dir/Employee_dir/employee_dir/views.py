from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Employee_dir_data
from .models import Employee_dir
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.


def welcome_hi(request):
	return HttpResponse("hello django")

@login_required
def Employee_Data(request):
	# sweetify.success(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')
	if request.method == 'POST':
		form = Employee_dir_data(request.POST,request.FILES)
		if form.is_valid():
			# instance=form.save(commit=False)
			# instance.author=request.user
			# instance.save()
			form.save()
			messages.success(request, 'Your Form submitted Successfully')
			return redirect("data_table")
	else:
		form = Employee_dir_data()
	return render(request, 'employ_form.html', {'form': form})

@login_required
def Emp_data(request):
	data_emp=Employee_dir.objects.all()
	return render(request,'emp_data.html',{"data_emp":data_emp})

@login_required
def EmployeeTableUpdate(request,id=None):
	EmployeeDataEdit=Employee_dir.objects.get(id=id)
	if request.method=="POST":
		form = Employee_dir_data(request.POST,instance=EmployeeDataEdit)
		if form.is_valid():
			form.save()
			# htmly = get_template('email.html')
			# d = Context({ 'username': username })
			# subject, from_email, to = 'hello', 'satishpal456@gmail.com', 'satishkumar@solulab.co'
			# html_content = htmly.render(d)
			# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
			# msg.attach_alternative(html_content, "text/html")
			# msg.send()
			# subject, from_email, to = 'Salary Update', 'satishpal456@gmail.com', 'satishkumar@solulab.co'
			# text_content = 'This is an important message.'
			# html_content = '<p>This is an <strong>important</strong> message.{{Emp_salary}}</p>'
			# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
			# msg.attach_alternative(html_content, "text/html")
			# msg.send()
			subject = 'Subject'
			data_emp=Employee_dir.objects.all()
			html_message = render_to_string('mail_template.html',{"data_emp":data_emp})
			plain_message = strip_tags(html_message)
			from_email = 'Satish Department <Satishpal456@gmail.com>'
			to = 'satishkumar@solulab.co'
			mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message) 
			messages.success(request, 'Your Data Updated Successfully')
			return redirect('data_table')
	else:
		EmployeeDataupdate = Employee_dir_data(instance=EmployeeDataEdit)
	return render(request, 'Employee_data_update.html', {'EmployeeDataupdate': EmployeeDataupdate})

@login_required
def homepage(request):
	return render(request,'hr_homepage.html')







