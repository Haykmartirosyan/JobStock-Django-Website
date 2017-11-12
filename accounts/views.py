from django.shortcuts import render


def Login_view(request):
    context = {}
    template_name = "accounts/index.html"

    return render(request, template_name, context)


def Register_view(request):
    context = {}
    template_name = "accounts/signup.html"

    return render(request, template_name, context)
