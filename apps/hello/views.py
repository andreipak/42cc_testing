from django.shortcuts import render
from apps.hello.models import Profile


def index(request):
    profile = Profile.objects.first()
    return render(request,
                  'hello/index.html', {
                      'profile': profile
                  })
