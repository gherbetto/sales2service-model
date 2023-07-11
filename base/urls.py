from django.urls import path
from .views import UnitList, UnitDetail, UnitCreate, UnitUpdate, UnitDelete, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', UnitList.as_view(), name='units'),
    path('unit/<int:pk>/', UnitDetail.as_view(), name='unit'),
    path('unit-create/', UnitCreate.as_view(), name='unit-create'),
    path('unit-update/<int:pk>/', UnitUpdate.as_view(), name='unit-update'),
    path('unit-delete/<int:pk>/', UnitDelete.as_view(), name='unit-delete'),
]