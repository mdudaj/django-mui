from django.shortcuts import render


def design_token_parity_view(request):
    return render(request, "django_mui/design_token_parity.html")
