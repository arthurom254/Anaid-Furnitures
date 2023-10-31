from django.contrib import admin
from django.urls import path, reverse_lazy, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .sitemap import ItemSitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views as auth_views
# import django_pesapal

sitemaps={
    'item':ItemSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('administrator.urls')),
    path('', include('clients.urls')),    
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps}),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        # email_template_name='registration/password_reset_email.html',
        # subject_template_name='accounts/password_reset_subject.txt',
        success_url=reverse_lazy('password_reset_done')
    ), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name='password_reset_done'),
    path('password_reset_<uidb64>_<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        success_url=reverse_lazy('password_reset_complete')
    ), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)