from django.urls import path
from .views import UnitList, UnitDetail

urlpatterns = [
    path('', UnitList.as_view(), name='units'),
    path('unit/<int:pk>/', UnitDetail.as_view(), name='unit'),
]