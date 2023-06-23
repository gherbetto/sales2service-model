from django.urls import path
from .views import UnitList, UnitDetail, UnitCreate, UnitUpdate, UnitDelete

urlpatterns = [
    path('', UnitList.as_view(), name='units'),
    path('unit/<int:pk>/', UnitDetail.as_view(), name='unit'),
    path('unit-create/', UnitCreate.as_view(), name='unit-create'),
    path('unit-update/<int:pk>/', UnitUpdate.as_view(), name='unit-update'),
    path('unit-delete/<int:pk>/', UnitDelete.as_view(), name='unit-delete'),
]