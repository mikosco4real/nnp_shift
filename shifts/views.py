from django.shortcuts import render, reverse, HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionDenied, PermissionRequiredMixin
from django.views import View
from nnp_shift.settings import LOGIN_URL

# Create your views here.
class Home(LoginRequiredMixin, View):
    login_url = LOGIN_URL
    template_name = "shifts/home.html"

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)