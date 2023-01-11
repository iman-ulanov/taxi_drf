from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Taxi, Order
from .permissions import IsProfilePermission
from .serializers import TaxiSerializer, OrderSerializer, StatusDriverSerializer


class TaxiViewSet(viewsets.ModelViewSet):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer

    @action(methods=['POST'], detail=True)
    def leave_mark(self, request, pk=None):
        serializer = StatusDriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                profile=request.user.profile,
                point=self.get_object()
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsProfilePermission]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


