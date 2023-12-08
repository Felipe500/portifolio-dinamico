from django.contrib.auth.backends import ModelBackend

from .models import User


class AccountsBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = None
        username = kwargs.get("email") or request.POST.get("username") or username
        if username:
            username = username.strip()
            user = (
                User.objects.get_queryset()
                .filter(email__iexact=username, deleted_at__isnull=True)
                .first()
            )

        if not user:
            User().set_password(password)
        elif user.check_password(password) and self.user_can_authenticate(user):
            return user
