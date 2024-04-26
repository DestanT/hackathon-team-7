from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from .forms import ProfileEditForm
from .models import Profile


class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profiles/profile_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_edit_form'] = ProfileEditForm()
        return context

class ProfileUpdate(UserPassesTestMixin, UpdateView):
    model = Profile
    fields = ['bio', 'image']

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.owner

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('profiles:profile_detail', kwargs={'pk': self.kwargs['pk']}))

    def get_success_url(self):
        return reverse('profiles:profile_detail', kwargs={'pk': self.kwargs['pk']})
