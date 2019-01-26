from django.shortcuts import render


def sign_up(request):
    return render(request, 'accounts/sign_up.html')

def log_in(request):
    return render(request, 'accounts/log_in.html')

def log_out(request):
    # TODO: log out and route to home page
    return render(request, 'accounts/sign_up.html')
