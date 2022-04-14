from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('employers-list', views.EmployerList, name='employers-list'),
    path('employers-search', views.EmployerSearch, name='employers-search'),
    path('employer-create', views.EmployerCreate, name='employer-create'),
    path('employer-update/<int:pk>', views.EmployerUpdate, name='employer-update'),
    path('employer-delete/<int:pk>', views.EmployerDelete, name='employer-delete'),
    path('employer-detail/<int:pk>', views.detail_view, name='employer-detail'),
    path('qr_code/', include('qr_code.urls', namespace="qr_code")),
]
