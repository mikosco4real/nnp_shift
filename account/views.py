from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse, reverse
from django.contrib.auth import login, update_session_auth_hash, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, PermissionDenied
from django.views import View
from .forms import RegisterForm
from nnp_shift.settings import LOGIN_URL

# Create your views here.

class Register(View):
    login_url = LOGIN_URL
    template_name = 'account/register.html'
    form_class = RegisterForm

    def get(self, request):
        context = {"form": self.form_class}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        context = {"form": form}

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('account:login'))

        return render(request, self.template_name, context)