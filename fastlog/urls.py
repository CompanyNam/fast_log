from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers,viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from django.conf.urls import url
from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,CreateAPIView
from rest_framework.permissions import AllowAny
from .models import *
from rest_framework.serializers import ModelSerializer
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']




# class AlbumSerializers(serializers.ModelSerializer):
#     album=BookModelCreateSerializer(many=True)
#     class Meta:
#         model=Album
#         fields="__all__"

# ViewSets define the view behavior.

class BookerUserForNested(ModelSerializer):
    class Meta:
        model=BookerUser
        fields=[
            'first_name',
            'last_name',
        ]
class DriverUserForNested(ModelSerializer):
    class Meta:
        model=DriverUser
        fields=[
            'first_name',
            'last_name',
            'lat',
            'len',
        ]
class OrderCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'

class OrderSerializers(serializers.ModelSerializer):
    driver_user=DriverUserForNested()
    booker_user=BookerUserForNested()
    class Meta:
        model=Order
        fields="__all__"

class OrderListAPIView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    # def post(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class AlbumViewSet(viewsets.ModelViewSet):
#     queryset = Album.objects.all()
#     serializer_class = AlbumSerializers
class OrderDetailAPIView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)



class OrderUpdateAPIView(UpdateAPIView):


    queryset = Order.objects.all()
    permission_classes = [AllowAny]
    serializer_class = OrderCreateSerializers
    def get(self, request, pk):
        return Response("ok")
    


class OrderDeleteAPIView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class =OrderCreateSerializers
    permission_classes = [AllowAny]
    def get(self, request, pk):
        return Response("ok")

class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializers
    permission_classes = [AllowAny]
    def get(self, request):
        return Response("ok")



# Routers provide an easy way of automatically determining the URL conf.

# router.register(r'books', BookViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^orders/$', OrderListAPIView.as_view() , name="order_list"),
    url(r'^orders/(?P<pk>\d+)/detail/$', OrderDetailAPIView.as_view() , name="order_detail"),
    url(r'^orders/(?P<pk>\d+)/update/$', OrderUpdateAPIView.as_view() , name="order_update"),
    url(r'^orders/(?P<pk>\d+)/delete/$', OrderDeleteAPIView.as_view() , name="order_delete"),
    url(r'^orders/create/$', OrderCreateAPIView.as_view() , name="order_create"),
    

    
]