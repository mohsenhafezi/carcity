from django.http.response import HttpResponse


def home_page(request):
    return HttpResponse("You're at the carcity home page.")
