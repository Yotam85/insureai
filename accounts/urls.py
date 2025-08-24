from django.urls import path
from .views import StartLogin, VerifyCode, logout, claim_guest_work

urlpatterns = [
    path("auth/start/",  StartLogin.as_view(),  name="auth-start"),
    path("auth/verify/", VerifyCode.as_view(), name="auth-verify"),
    path("auth/logout/", logout,               name="auth-logout"),
    path("auth/claim/",  claim_guest_work,     name="auth-claim"),
]
