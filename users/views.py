from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserRegisterForm, UserUpdateForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES, )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your account has been created! You are now able to log in"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user
        )
        if u_form.is_valid():
            u_form.save()
            messages.success(
                request,
                "Your account has been updated!"
            )
            return redirect("profile")

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        "u_form": u_form,
    }

    return render(request, "users/profile.html", context)
