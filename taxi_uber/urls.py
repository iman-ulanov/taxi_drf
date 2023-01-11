from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from account import views as acc_view
from service import views as ser_views

acc_router = DefaultRouter()
acc_router.register('register', acc_view.ProfileRegisterAPIView)


ser_router = DefaultRouter()
ser_router.register('taxi', ser_views.TaxiViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/', include('rest_framework.urls')),
    path('api/account/', include(acc_router.urls)),
    path('api/account/rating/<int:pk>', ser_views.TaxiViewSet),
    path('api/service/', include(ser_router.urls)),
    path('api/service/taxi/<int:pk>/order/', ser_views.OrderViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/service/taxi/<int:pk>/order/<int:id>', ser_views.OrderViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),

]
