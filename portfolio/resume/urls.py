from django.urls import path

from resume import views

urlpatterns = [
    path('portfolio/', include('.urls')),
    path('admin/', admin.site.urls),
]