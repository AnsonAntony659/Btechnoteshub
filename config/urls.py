
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('universities/',include('universities.urls')),
    path('courses/',include('courses.urls')),
    path('subjects/', include('subjects.urls')),
    path("schemes/", include("scheme.urls")),
    path("years/",include("year.urls")),
    path("notes/",include("notes.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)