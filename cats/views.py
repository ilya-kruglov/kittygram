from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Cat
from .serializers import CatSerializer


class APICat(APIView):
    def get(self, request):
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APICatDetail(APIView):
    """
    Retrieve, update or delete a cat instance.
    """
    def get_object(self, pk):
        try:
            return Cat.objects.get(pk=pk)
        except Cat.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        cat = self.get_object(pk)
        serializer = CatSerializer(cat)
        return Response(serializer.data)

    def put(self, request, pk):
        cat = self.get_object(pk)
        serializer = CatSerializer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        cat = self.get_object(pk)
        serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cat = self.get_object(pk)
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Для POST, если нужна возможность добавления нескольких объектов:
# serializer = CatSerializer(data=request.data, many=True)
# С many=True в API будет ожидаться список [], а не {}

# Для обновления существующей записи первым параметром в сериализатор
# передаётся тот объект модели, который нужно обновить. В этом случае
# вызов save() не приведёт к созданию нового объекта.
# ...
# cat = Cat.objects.get(id=id)
# serializer = CatSerializer(cat, data=request.data)
# # Если вызвать serializer.save(), будет обновлён существующий экземпляр Cat


# Если при создании экземпляра сериализатора указать
# аргумент partial=True — отсутствие в запросе обязательных полей
# не приведёт к ошибке. Добавлять для PUT, PATCH, DELETE.

# serializer = CatSerializer(cat, data=request.data, partial=True)
