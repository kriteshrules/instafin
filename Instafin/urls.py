from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from dashboard import views as dash_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from ideabox import views as ideabox_views
from thematic import views as thematic_views
from aceinvestors import views as aceinvestors_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name="register"),
    path('profile/', user_views.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('home/', include('home.urls')),
    path('', dash_views.home, name="dashboard-home"),
    path('ideabox/', ideabox_views.home, name="ideabox-home"),
    path('thematic/', thematic_views.home, name="thematic-home"),
    path('thematic/', include('thematic.urls')),
    path('ace-investors/', aceinvestors_views.home, name="aceinvestors-home"),
    path('ace-investors/', include('aceinvestors.urls')),
    path('fundamental-tools/', include('fundamentaltools.urls')),
    path('sentiment/', include('sentiment.urls')),
    path('stocks/', include('stocks.urls')),
    path('watchlist/', include('watchlist.urls')),
    path('fire/', include('fijourney.urls')),
]

#path('ideabox/', include('ideabox.urls')),
#path('thematic/', include('thematic.urls')),
#path('ace-investors/', include('aceinvestors.urls')),

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
