"""evi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django_registration.backends.one_step.views import RegistrationView

from core.views import IndexTemplateView
from users.forms import CustomUserForm

urlpatterns = [
    path('admin/', admin.site.urls),

    # path("accounts/register/", RegistrationView.as_view(form_class=CustomUserForm, success_url="/",), name="django_registration_register"), 
    path("accounts/", include("django_registration.backends.one_step.urls")),
    path("accounts/", include("django.contrib.auth.urls")),

    path("app/sessions/signUp/", RegistrationView.as_view(form_class=CustomUserForm, success_url="/",), name="vue_register"), 
    # path("app/sessions/", include("django_registration.backends.one_step.urls")),
    # path("app/sessions/", include("django.contrib.auth.urls")),

    path('api/', include("inspection.api.urls")),
    path('api/', include("users.api.urls")),

    # login via browsable api
    path('api-auth/', include("rest_framework.urls")),

    # login via REST
    path('api/rest-auth/', include("rest_auth.urls")),

    # registration via REST
    path('api/rest-auth/register/', include("rest_auth.registration.urls")),

    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
