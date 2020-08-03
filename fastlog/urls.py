from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import booking
from django.conf.urls import url
from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,CreateAPIView
from rest_framework.permissions import AllowAny
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class BookSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=booking
        fields = fields=[
            'booker',
            'endPlace',
            'initialPlace',
            'id',
            'price',
            'distance',
        ]

class BookModelCreateSerializer(ModelSerializer):
    class Meta:
        model=booking
        fields = fields=[
            'booker',
            'endPlace',
            'initialPlace',
            
            'price',
            'distance',
        ]

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = BookSerializers
class BookDetailAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelCreateSerializer


class BookUpdateAPIView(UpdateAPIView):


    queryset = Book.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BookModelCreateSerializer


class BookDeleteAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class =BookModelCreateSerializer
    permission_classes = [IsAdminUser]

class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelCreateSerializer
    permission_classes = [IsAdminUser]

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'booking',BookViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    url(r'^(?P<pk>\d+)/detail/$', BookDetailAPIView.as_view() , name="docdetail"),
    url(r'^(?P<pk>\d+)/update/$', BookUpdateAPIView.as_view() , name="docupdate"),
    url(r'^(?P<pk>\d+)/delete/$', BookDeleteAPIView.as_view() , name="docdel"),
    url(r'^create/$', BookCreateAPIView.as_view() , name="doccre"),
    
]