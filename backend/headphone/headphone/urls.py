"""
URL configuration for headphone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from products.views import MyTokenObtainPairview

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("products.urls")),
    path('all_products/', include('all_products.urls')),

    # path('' , include('blog.urls' , namespace='blog')),
    # path('api/' , include('blog_api.urls' , namespace='blog_api')),
    # path('api-auth/' , include('rest_framework.urls' , namespace='rest_framework')),
    
    # path('api/users/', include('accounts.urls')),
    # simple jwt authentication
    # path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# handle404 = 'utils.error.handle404'
# handle500 = 'utils.error.handle500'
