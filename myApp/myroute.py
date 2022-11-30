from django.http import HttpResponse


def myroute(request):
    return HttpResponse(
        "<h1>Hello, world. You're at my route. :-> </h1>")
