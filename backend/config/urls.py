from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/accounts/", include("apps.accounts.urls")),
    path("api/content/", include("apps.content.urls")),
    path("api/study/", include("apps.study.urls")),
    path("api-auth/", include("rest_framework.urls")),
]

