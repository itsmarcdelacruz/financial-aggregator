from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("budgetapp/", include("budgetapp.urls")),
    path("admin/", admin.site.urls),
]
