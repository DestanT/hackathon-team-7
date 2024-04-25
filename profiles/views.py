from django.views import generic
from django.views.generic.detail import DetailView
from .models import Profile

class ProfileList(generic.ListView):
    model = Profile
    queryset = Profile.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profiles/profile.html'
