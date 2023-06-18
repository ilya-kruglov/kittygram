from django.urls import path

from cats.views import APICat, APICatDetail

urlpatterns = [
   path('cats/', APICat.as_view(), name='cat_list'),
   path('cats/<int:pk>/', APICatDetail.as_view(), name='cat_edit'),
]
