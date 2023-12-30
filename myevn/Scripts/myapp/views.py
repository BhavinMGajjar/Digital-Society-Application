from django.shortcuts import render
from . models import User, Watchmen, Events
from django.conf import settings
from django.core.mail import send_mail
import random
# Create your views here.

def index(request):
	return render(request, 'index.html')

def members(request):
	member=User.objects.all()
	context = {'member':member}
	return render(request, 'members.html', context)
	

def watchmen(request):
	watchman=Watchmen.objects.all()
	context = {'watchman':watchman}
	return render(request, 'watchmen.html', context)

def notice(request):
	return render(request, 'notice.html')

def events(request):
	events=Events.objects.all()
	context = {'events':events}
	return render(request, 'events.html', context)
	

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				request.session['email']=user.email
				request.session['fname']=user.fname
				return render(request, 'index.html')
			else:
				msg="Incorrect Password"
				return render(request,'login.html', {'msg':msg})
		except:
			msg="Email not registered"
			return render(request,'login.html', {'msg':msg})		
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		return render(request,'login.html')
	except:
		msg="User logged out Successfully"
		return render(request,'login.html', {'msg':msg})


def forgot_password(request):

	if request.method=="POST":
		try:

			user=User.objects.get(email=request.POST['email'])
			otp=random.randint(1000,9999)
			subject = 'OTP for forgot password'
			message = 'Hello '+user.fname+"Your OTP for forgot password is"+str(otp)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email, ]
			send_mail( subject, message, email_from, recipient_list )
			return render(request,'otp.html',{'otp':otp,'email':user.email})
			
		except:
			msg="Email is not registered"
			return render(request, 'forgot-password.html', {'msg':msg})

	else:
		return render(request, 'forgot-password.html')

def verify_otp(request):

	email=request.POST['email']
	otp=int(request.POST['otp'])
	uotp=int(request.POST['uotp'])

	if otp==uotp:
		return render(request,'new-password.html',{'email':email})
	else:
		msg="Invalid OTP"
		return render(request,'otp.html',{'otp':otp, 'email':email,'msg':msg})


def profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.mobile=request.POST['mobile']
		try:
			user.profile_picture=request.FILES['profile_picture']
		except:
			pass
			user.save()
			request.session['profile_picture']=user.profile_picture.url
			msg="Profile updated Successfully"
			return render(request, 'profile.html', {'user':user,'msg':msg})
	else:
		return render(request, 'profile.html', {'user':user})

