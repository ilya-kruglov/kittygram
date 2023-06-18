from django.urls import path

from cats.views import CatList, CatDetail

urlpatterns = [
   path('cats/', CatList.as_view(), name='cat_list'),
   path('cats/<int:pk>/', CatDetail.as_view(), name='cat_detail'),
]
