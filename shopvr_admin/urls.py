"""shopvr_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.shortcuts import redirect


urlpatterns = [
    path('', lambda r:redirect('franchise_hp:main'),name='root'),
    path('admin/', lambda r:redirect('store:sales_analysis'),name='root_main'),
    path('admin_django/', admin.site.urls),
    path('admin/accounts/', include('accounts.urls')),
    path('admin/survey/', include('survey.urls', namespace='survey')),
    path('admin/store/', include('store.urls', namespace='store')),
    path('admin/location/', include('location.urls', namespace='location')),
    path('franchise/', include('franchise_hp.urls', namespace='franchise_hp'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))

    ]