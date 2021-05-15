from django.contrib import admin
from django.conf.urls import url , include

urlpatterns = [
    url(r'^daila/', include('entry.urls', namespace='entry')),
    url(r'^daila/', include('boutique.urls', namespace='boutique')),
    url(r'^admin/', admin.site.urls),
]
