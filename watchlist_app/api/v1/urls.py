from django.urls import path

from watchlist_app.api.v1 import views

urlpatterns = [
    path("list/", views.MovieListAV.as_view(), name="movie_list"),
    path("list/<int:pk>/", views.MovieDetailAV.as_view(), name="movie_detail"),

    path("stream/", views.StreamPlatformAV.as_view(), name="stream_list"),
    path("stream/<int:pk>/", views.StreamDetailAV.as_view(), name="streamplatform-detail"),

    path("review/", views.ReviewListAV.as_view(), name="review_list"),
    path("review/<int:pk>/", views.ReviewDetailAV.as_view(), name="review_detail"),
]
