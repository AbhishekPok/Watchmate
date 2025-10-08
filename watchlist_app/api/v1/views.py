from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from pyexpat.errors import messages
from rest_framework import status, mixins
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from watchlist_app.api.v1.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from watchlist_app.models import WatchList, StreamPlatform, Review


# Create your views here.

# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method.lower() == 'get':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data, status = status.HTTP_200_OK)
#
#     if request.method.lower() == 'post':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             print("VALID")
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         else:
#             print("INVALID")
#             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # print(type(serializer.data))
    #movies_list = {"movies": list(movies.values())}
    #return JsonResponse(movies_list)


class MovieListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            print("VALID")
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            print("INVALID")
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class MovieDetailAV(APIView):
    def get(self, request, pk):
        movie = get_object_or_404(WatchList, id=pk)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        movie = get_object_or_404(WatchList, id=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = get_object_or_404(WatchList, id=pk)
        movie.delete()
        return Response({"message": "Movie deleted"},status = status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        movie = get_object_or_404(WatchList, id=pk)
        serializer = WatchListSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class StreamPlatformAV(APIView):
    def get(self,request):
        stream = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(stream, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self,request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            print("VALID")
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            print("INVALID")
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class StreamDetailAV(APIView):
    def get(self,request,pk):
        stream = get_object_or_404(StreamPlatform, id=pk)
        serializer = StreamPlatformSerializer(stream,context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        stream = get_object_or_404(StreamPlatform,id=pk)
        serializer = StreamPlatformSerializer(stream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        stream = get_object_or_404(StreamPlatform,id=pk)
        serializer = StreamPlatformSerializer(stream, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        stream = get_object_or_404(StreamPlatform, id=pk)
        stream.delete()
        return Response({"message": "Movie deleted"},status = status.HTTP_204_NO_CONTENT)


class ReviewListAV(mixins.ListModelMixin,mixins.CreateModelMixin,GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class ReviewDetailAV(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self,request,*args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request,*args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class ReviewListAV(APIView):
#     def get(self, request):
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self,request):
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             print("VALID")
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         else:
#             print("INVALID")
#             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE','PATCH'])
# def movie_detail(request, pk):
#     if request.method.lower() == 'get':
#         movie = get_object_or_404(Movie, id=pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data,status = status.HTTP_200_OK)
#     if request.method.lower() == 'put':
#         movie = get_object_or_404(Movie, id=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#
#
#     if request.method.lower() == 'delete':
#         movie = get_object_or_404(Movie, id=pk)
#         movie.delete()
#         return Response({"message": "Movie deleted"},status = status.HTTP_204_NO_CONTENT)
#
#
#     if request.method.lower() == 'patch':
#         movie = get_object_or_404(Movie, id=pk)
#         serializer = MovieSerializer(movie, data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    # print("Movie",movie)
    # data = {"name": movie.name,
    #         "description": movie.description,
    #         "active": movie.active,
    #         }
    # return JsonResponse(data)