from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup (View):
    def get(self, request):
        return render (request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone = postData.get ('phone')
        email = postData.get ('email')
        password = postData.get ('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer (first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password)
        error_message = self.validateCustomer (customer)

        if not error_message:
            customer.password = make_password (customer.password)
            customer.register ()
            return redirect ('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "Ismingizni kiriting"
        elif len (customer.first_name) < 3:
            error_message = "Ism haqiqyga o'xshamayabdi kamida 4 ta harfdan ko'p bo'lishi kerak"
        elif not customer.last_name:
            error_message = "Familiyangizni kiriting"
        elif len (customer.last_name) < 3:
            error_message = "Familiya haqiqyga o'xshamayabdi kamida 4 ta harfdan ko'p bo'lishi kerak"
        elif not customer.phone:
            error_message = "Telefon raqamingizni kiriting"
        elif len (customer.phone) < 9:
            error_message = "Telefon raqam kamida 9 ta raqamdan iborat bo'ladi !"
        elif len (customer.password) < 5:
            error_message = "Parolingiz eng kamida 5 ta belgidan iborat bo'lsin"
        elif customer.isExists ():
            error_message = 'Bu email allaqachon ishlatilgan..'

        return error_message
