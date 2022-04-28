from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path("", include("homepage.urls", namespace="homepage")),
    path("catalog/", include("catalog.urls", namespace="catalog")),
    path("about/", include("about.urls", namespace="about")),
    path("auth/", include("users.urls", namespace="auth")),
    path("auth/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    path("tinymce/", include("tinymce.urls")),
    
] 

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
