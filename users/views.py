from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.messages.views import SuccessMessageMixin
# from django.urls import reverse_lazy
from django.views.generic import DetailView



class AccountHomeView(LoginRequiredMixin, DetailView):
    """User Profile Page"""
    template_name = 'users/profile.html'

    def get_object(self):
        return self.request.user





