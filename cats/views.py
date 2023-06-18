from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cat
from .serializers import CatSerializer


# # View-функция cat_list() будет обрабатывать только запросы GET и POST,
# # запросы других типов будут отклонены,
# # так что в теле функции их можно не обрабатывать
# @api_view(['GET', 'POST'])
# def cat_list(request):
#     if request.method == 'POST':
#         # Создаём объект сериализатора
#         # и передаём в него данные из POST-запроса
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             # Если полученные данные валидны —
#             # сохраняем данные в базу через save().
#             serializer.save()
#             # Возвращаем JSON со всеми данными нового объекта
#             # и статус-код 201
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # Если данные не прошли валидацию —
#         # возвращаем информацию об ошибках и соответствующий статус-код:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     cats = Cat.objects.all()
#     serializer = CatSerializer(cats, many=True)
#     return Response(serializer.data)

@api_view(['GET', 'POST'])  # Разрешены только POST- и GET-запросы
def cat_list(request):
    # В случае POST-запроса добавим список записей в БД
    if request.method == 'POST':
        serializer = CatSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # В случае GET-запроса возвращаем список всех котиков
    cats = Cat.objects.all()
    serializer = CatSerializer(cats, many=True)
    return Response(serializer.data)

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
