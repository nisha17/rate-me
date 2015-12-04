from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .forms import  ContactForm

# Create your views here.
def home(request):
	title = "Contact Us"
 	form = ContactForm(request.POST or None)
 	confirm_message =None

 	template = 'contact/home.html'

 	if form.is_valid():
 	 	#print request.POST
 	 	#print form.cleaned_data['email']

 	 	sbj ='Mesage from BrokeRate.com'
 	 	msg = '%s %s' %(form.cleaned_data['message'], form.cleaned_data['full_name'])
 	 	frm = form.cleaned_data['email']
 	 	to_us = [settings.EMAIL_HOST_USER]

 	 	send_mail(sbj, msg, frm, to_us, fail_silently=False)

 	 	title = "Thank you"
 	 	confirm_message = """
 	 		Thank you for your message!
 	 	"""
 	 	form = None

 	context = {
		"form":form,
		"title": title,
		"confirm_message": confirm_message
	}

 	 	#save in model

 	return render(request,template, context)

