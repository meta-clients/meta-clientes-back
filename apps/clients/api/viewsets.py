from rest_framework.viewsets import ModelViewSet
from ..models import ClientModel, ChildrenModel
from .serializers import ClientSerializer, ChildrenSerializer


class ClientViewSet(ModelViewSet):
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializer

    
class ChieldrenViewSet(ModelViewSet):
    queryset = ChildrenModel.objects.all()
    serializer_class = ChildrenSerializer