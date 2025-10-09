from django.urls import path
from watchlist_app.api.v1 import views
from rest_framework import routers
from watchlist_app.api.v1.views import ReviewModelViewSet, StreamPlatformMovieViewSet
# review_list = views.ReviewListViewSet.as_view({'get':'list'})
# review_detail = views.ReviewListViewSet.as_view({'get':'retrieve'})

router = routers.DefaultRouter()
router.register("review", ReviewModelViewSet, basename="review")
router.register("stream", StreamPlatformMovieViewSet, basename="stream")

urlpatterns = [
    path("list/", views.MovieListAV.as_view(), name="movie_list"),
    path("list/<int:pk>/", views.MovieDetailAV.as_view(), name="movie_detail"),

    # path("stream/", views.StreamPlatformAV.as_view(), name="stream_list"),
    # path("stream/<int:pk>/", views.StreamDetailAV.as_view(), name="streamplatform-detail"),

    # path("review/", views.ReviewListAV.as_view(), name="review_list"),
    # path("review/<int:pk>/", views.ReviewDetailAV.as_view(), name="review_detail"),


    # path("review/",review_list, name="review_list"),
    # path("review/<int:pk>/", review_detail, name="review_detail"),
] + router.urls