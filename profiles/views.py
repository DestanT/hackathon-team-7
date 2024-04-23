from django.shortcuts import render
from django.views import generic
from .models import Profile

class ProfileList(generic.ListView):
    queryset = Profile.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3
