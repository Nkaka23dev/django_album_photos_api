from django.shortcuts import render   
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response 
import requests

# class GetAlbumData(APIView):  
#     _url="https://jsonplaceholder.typicode.com/albums"

#     def get(self,request,format=None):
#         album=requests.get(self._url) 

#         return Response({
#             'data':album.json(),
#             'message':'Data successfully retrieved',
#             'status':status.HTTP_200_OK
#         })

class GetAlbumById(APIView):
    def get(self, request, album_id, format=None):
        _url=f"https://jsonplaceholder.typicode.com/albums/{album_id}/photos"
        album_by_id= requests.get(_url)
        return Response(album_by_id.json())