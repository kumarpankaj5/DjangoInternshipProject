# consumer_services/views.py
from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import Account 
from django.contrib.auth.forms import UserCreationForm
@login_required
def view_account(request):
    account = request.user.account
    service_requests = ServiceRequest.objects.filter(account=account)
    return render(request, 'view_account.html', {'account': account, 'service_requests': service_requests})

@login_required
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)

            service_request.account = request.user.account  # Associate with logged-in user's account
            service_request.save()
            return redirect('request_tracking')  # Redirect to request tracking page
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_service_request.html', {'form': form})

@login_required
def request_tracking(request):
    # Retrieve the account associated with the logged-in user
    account = request.user.account
    # Retrieve service requests associated with the user's account
    service_requests = ServiceRequest.objects.filter(account=account)
    return render(request, 'request_tracking.html', {'service_requests': service_requests})
# views.py

# views.py
# views.py

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Create an account record for the new user
            Account.objects.create(user=user)
            
            login(request, user)
            messages.success(request, 'Account created successfully. You are now logged in.')
            return redirect('submit_service_request')  # Redirect to desired page after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

