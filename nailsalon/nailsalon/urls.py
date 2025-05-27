from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 

from pages import views as page_views
from booking import views as booking_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page_views.home, name='home'),
    path('services/', page_views.services, name='services'),
    path('services/<int:pk>/', page_views.service_detail, name='service_detail'),
    path('book/', booking_views.book_appointment, name='book'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
