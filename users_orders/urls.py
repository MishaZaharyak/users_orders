from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api/v1/', include('core.api.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
