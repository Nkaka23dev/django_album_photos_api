from django.urls import path 
from .views import GetAlbumById

urlpatterns = [
    # path("album/", GetAlbumData.as_view(),name="Album"),
    path("album_photos_by_id/<int:album_id>", GetAlbumById.as_view(),name="album_by_id")
]