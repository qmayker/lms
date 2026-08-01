from django.contrib.auth.views import LoginView

# Create your views here.


class UserLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


# class UserLogoutView(LogoutView):
#     http_method_names = LogoutView.http_method_names + ["get"]
#     logout_template_name = "registration/logging_out.html"

#     def get(self, request, *args, **kwargs):
#         return render(request, self.logout_template_name)
