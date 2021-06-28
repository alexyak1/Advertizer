from rest_advert.models import Ad
from rest_advert.serializers import AdSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AdList(APIView):
    """
    List all ads, or create a new ad.
    """
    def get(self, request, format=None):
        ads = Ad.objects.all()
        serializer = AdSerializer(ads, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdDetail(APIView):
    """
    Retrieve, update or delete a ad instance.
    """
    def get_object(self, pk):
        try:
            return Ad.objects.get(pk=pk)
        except Ad.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AdSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AdSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

