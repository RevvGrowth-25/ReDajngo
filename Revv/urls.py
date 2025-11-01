"""
URL configuration for Revv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from home.views import ceo_dashboard,get_workflow_report,test_webhook_raw

urlpatterns = [
    path('', ceo_dashboard),
    path('api/workflow-report/', get_workflow_report),
    # 👈 this should be '' instead of '/'
path('api/test-webhook/', test_webhook_raw),
    path('admin/', admin.site.urls),

]

