from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages ,auth
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required

# verification Email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            # user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email,phone_number=phone_number, username=username, password=password)
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email,username=username, password=password)
            user.phone_number = phone_number
            # harinm methana is active danna ba activatin method eke thamai danna ona
            #  m ahe wada nathi nisaa essarahata karagena yanna on anisa mehema kare

            user.is_active = True
            print(user)
            user.save()

            # User Activation  
            # verification email
            # current_site = get_current_site(request)
            # mail_subject = 'Please activate your account'
            # message = render_to_string('accounts/account_verification_email.html', {
            #     'user': user,
            #     'domain': current_site,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': default_token_generator.make_token(user),
            # })
            
            # print(email)
            
            # to_email = email
            # send_email = EmailMessage(mail_subject, message, to=[to_email])
            # print(send_email)
            # send_email.send()

            
            messages.success(request, 'Registation sucessful.')
            return redirect('register') 

        else:
            print("not save")
    else:
        print("why wada naththe")
        form = RegistrationForm()
        

    context = {
         'form':form,
    }
    return render(request , 'accounts/register.html' , context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email = email ,password=password)

        if user is not None:
            auth.login(request , user)
            return redirect('home')
        else:
            print("wada na ")
            messages.error(request , 'Invalid login credentials')
            return redirect('login')
        
    return render(request , 'accounts/login.html')


@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')

def activate(request ,uidb64 ,token):
    return HttpResponse("ok")