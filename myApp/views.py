from rest_framework.viewsets import ModelViewSet

from myApp.models import Person
from myApp.serializers import PersonSerializer


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
