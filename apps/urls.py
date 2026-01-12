from django.urls import path

from apps.views import ProductListView, ProductDetailView, CustomLoginView, ProfileUpdateView, RegisterCreateView, \
    CustomLogoutView, GoogleLoginView, GoogleCallbackView, ProfileImageUpdateView, ProfileChangePasswordView, UserDelete

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list_page'),
    path('detail/<slug:slug>', ProductDetailView.as_view(), name='product_detail_page'),

    path('auth/login', CustomLoginView.as_view(), name='login_page'),
    path('auth/profile/update-image', ProfileImageUpdateView.as_view(), name='profile_update_image_page'),
    path('auth/profile/update-password', ProfileChangePasswordView.as_view(), name='profile_update_password_page'),
    path('auth/profile', ProfileUpdateView.as_view(), name='profile_page'),
    path('auth/register', RegisterCreateView.as_view(), name='register_page'),
    path('auth/logout', CustomLogoutView.as_view(), name='logout_page'),
    path('auth/profile/delete-user', UserDelete.as_view(), name='delete_user_page'),

    path('auth/google-login', GoogleLoginView.as_view(), name='google_login_page'),
    path('auth/oauth2/callback', GoogleCallbackView.as_view(), name='google_callback_page')
]