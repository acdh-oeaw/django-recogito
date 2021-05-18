from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer

from rest_framework import viewsets

from recogito.api_serializers import RecogitoAnnotationSerializer
from recogito.api_renderers import RecogitoRenderer
from recogito.models import RecogitoAnnotation


class RecogitoAnnotationViewSet(viewsets.ModelViewSet):
    queryset = RecogitoAnnotation.objects.all()
    serializer_class = RecogitoAnnotationSerializer
    filter_backends = [DjangoFilterBackend]
    renderer_classes = [
        BrowsableAPIRenderer,
        JSONRenderer,
        RecogitoRenderer
    ]
    filterset_fields = [
        're_app',
        're_model',
        're_object_id',
        're_field_name'
    ]
