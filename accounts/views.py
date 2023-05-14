from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UserForm
from .models import User


def register_user(request):
    if request.method == 'POST':
        # print(request.POST)
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.role = User.CUSTOMER
            user.save()
            
            return redirect("register-user")
    else:
        form = UserForm()

    context = {
        'form': form
    }

    return render(request, "accounts/register.html", context)
