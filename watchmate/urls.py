

from django.contrib import admin
from django.urls import path, include

from watchlist_app.models import StreamPlatform

urlpatterns = [
    path("admin/", admin.site.urls),
    path("watch/", include("watchlist_app.api.v1.urls")),

    # path("stream/", include("watchlist_app.api.v1.urls")),
]
