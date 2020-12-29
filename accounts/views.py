from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import (
  LoginView, logout_then_login, 
  PasswordChangeView as AuthPasswordChangeView,
)
from django.core.mail import send_mail
from django.contrib.auth import login as auth_login
from .models import Post

login=LoginView.as_view(template_name="accounts/login_form.html")

def logout(request):
  messages.success(request, '로그아웃되었습니다.')
  return logout_then_login(request)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)
            messages.success(request, "회원가입 환영합니다.")
            #signed_user.send_welcome_email()  # FIXME: Celery로 처리하는 것을 추천.
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })
#loginrequiredmixin은 class view 함수에서 login 권한을 체크해준다
class PasswordChangeView(LoginRequiredMixin, AuthPasswordChangeView):
  success_url=reverse_lazy("password_change")
  template_name = 'accounts/password_change_form.html'

  def form_valid(self, form):
    messages.success(self.request, "비밀번호가 변경되었습니다")
    return super().form_valid(form)

password_change=PasswordChangeView.as_view()


def post_detail(request, pk):
  post=get_object_or_404(Post, pk=pk)

