from django.shortcuts import HttpResponse


def dummy_user_view(request):
    return HttpResponse('Hello Peeps')
