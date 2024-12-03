from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Garden, GardenInfo
from .serializers import GardenSerializer, GardenInfoSerializer


# Create your views here.
class GardensListView(APIView):
    def get(self, request):
        gardens = Garden.objects.all()
        serializer = GardenSerializer(gardens, many=True)

        return Response(serializer.data)


class GardenCreateView(CreateAPIView):
    serializer_class = GardenSerializer


class GardenInfoCreateView(CreateAPIView):
    serializer_class = GardenInfoSerializer


# Create your views here.
class GardensInfoListView(APIView):
    def get(self, request):
        gardens = GardenInfo.objects.all()
        serializer = GardenInfoSerializer(gardens, many=True)

        return Response(serializer.data)


class GardenInfosListView(APIView):
    def get(self, request, *args, **kwargs):
        garden_id = kwargs.get("id")
        try:
            garden = GardenInfo.objects.filter(garden_id=garden_id)
        except GardenInfo.DoesNotExist:
            raise NotFound({"detail": "Garden with thta id doesn't exist"})

        serializer = GardenInfoSerializer(garden, many=True)

        return Response(serializer.data)
