from rest_framework.decorators import api_view
from user_app.api.v1.serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework.status import  HTTP_201_CREATED ,HTTP_400_BAD_REQUEST

@api_view(['POST'])
def user_register_view(request):
    serializer =UserRegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)