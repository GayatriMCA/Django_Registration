from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from App.models import User
from django.views import View

# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, 'base.html')

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        phone_number = postData.get('phone_number')
        email = postData.get('email')
        password = postData.get('password')

        #validation

        value = {
            'first_name':first_name,
            'last_name':last_name,
            'phone_number':phone_number,
            'email':email,
        }
        
        error_message = None

        customer = User(first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                email=email,
                password=password)

        error_message = self.validateUser(customer)
        
        #save  
        if not error_message:
            #print(first_name ,last_name , phone_number , email , password)
            customer.password = make_password(password)
            customer.save()
            return redirect('homepage')
        else:
            context = {
                    'error':error_message,
                    'values':value
            }
            return render(request,'signup.html', context)

    def validateUser(self, customer):
        error_message = None
        if not customer.first_name:
                error_message = "First Name Required !!"
        elif len(customer.first_name)<4:
                error_message = "First Name must be 4 char long or more"
        elif not customer.last_name:
                error_message = "Last Name Required !!"
        elif len(customer.last_name)<4:
                error_message = "Last Name must be 4 char long or more"
        elif not customer.phone_number:
                error_message = "Phone Number Required !!"
        elif len(customer.phone_number)>10:
                error_message = "Phone Number must be 10 char Long"
        elif len(customer.email)<5:
                error_message = "Email must be 5 char long"
        elif customer.isExists():
                error_message = "Email Address Already Exists"
        elif len(customer.password)<6:
                error_message = "Password must be 6 char long"
        return error_message


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.get_user_by_email(email)
        error_message = None
        if user:
            flag = check_password(password, user.password)
            if flag:
                return redirect('homepage')
            else:
                error_message = "Email or Password Invalid !!"
        else:
            error_message = "Email or Password Invalid !!"

        context = {
            'email':email,
            'error':error_message
        }

        return render(request, 'login.html', context)

def logout(request):
    return redirect('login')