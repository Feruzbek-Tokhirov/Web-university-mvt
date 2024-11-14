from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")),
    path("course/", include("course.urls")),
    path("about/", include("about.urls")),
    path("contact/", include("contact.urls")),
    path("register/", include("registration.urls"))
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
