from django.contrib import admin
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('employers-list', views.EmployerList, name='employers-list'),
    path('employers-search', views.EmployerSearch, name='employers-search'),
    path('employer-create', views.EmployerCreate, name='employer-create'),
    path('employer-update/<int:pk>', views.EmployerUpdate, name='employer-update'),
    path('employer-delete/<int:pk>', views.EmployerDelete, name='employer-delete'),
    path('employer-detail/<int:person>',
         views.detail_view, name='employer-detail'),
    path('traitement-create/<int:person>',
         views.TraitementCreate, name='traitement-create'),
    path('traitement-delete/<int:pk>',
         views.TraitementDelete, name='traitement-delete'),
    path('qr_code/', include('qr_code.urls', namespace="qr_code")),
    path('partenaire-list', views.PartenaireList, name='partenaire-list'),
    #path('employers-search', views.EmployerSearch, name='employers-search'),
    path('partenaire-create', views.EmployerCreate, name='partenaire-create'),
    path('partenaire-update/<int:pk>',
         views.EmployerUpdate, name='partenaire-update'),
    path('partenaire-delete/<int:pk>',
         views.EmployerDelete, name='partenaire-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
