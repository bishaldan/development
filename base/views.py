from django.shortcuts import render,  redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Student  # Import your Student model
# Create your views here.


def home(request):
    return render(request,  'base/home.html')


def room(request):
    return render(request, 'base/room.html')


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if there is a student with the provided email
        try:
            student = Student.objects.get(email=email)
        except Student.DoesNotExist:
            # If the student doesn't exist, show an error
            error_message = "Invalid email or password"
            return render(request, 'base/login.html', {'error_message': error_message})

        # Authenticate the student with the provided password
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Password matched, login the user
            login(request, user)
            # Redirect to main student page upon successful login
            return redirect('main_student')
        else:
            # If the password is incorrect, show an error
            error_message = "Invalid email or password"
            return render(request, 'base/login.html', {'error_message': error_message})

    else:
        return render(request, 'base/login.html')


def main_student(request):
    return render(request, 'base/main_student.html')


def chatbot_student(request):
    return render(request, 'base/chatbot_student.html')
