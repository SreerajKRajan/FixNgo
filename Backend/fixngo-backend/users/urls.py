from django.urls import path
from .views import UserSignupView, UserLoginView, UserLogoutView, OtpVerificationView, UserProfileView, get_nearby_workshops, UserForgotPasswordView, ResetPasswordView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='user-signup'),
    path('otp_verification/', OtpVerificationView.as_view(), name='user-otp-verification'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('workshops/nearby/', get_nearby_workshops, name='nearby-workshops'),
    path('forgot-password/', UserForgotPasswordView.as_view(), name='user-forgot-password'),
    path('reset-password/<uidb64>/<token>/', ResetPasswordView.as_view(), name='reset-password'),
]
