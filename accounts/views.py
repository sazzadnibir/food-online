from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .forms import UserForm
from .models import User


def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            # password = form.cleaned_data["password"]

            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()
            
            ### Create the user using create_user method
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
            )
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, "You account has been registered successfully")
            
            return redirect("register-user")
        else:
            print("invalid form")
            print(form.errors)
    else:
        form = UserForm()

    context = {
        'form': form
    }

    return render(request, "accounts/register.html", context)
