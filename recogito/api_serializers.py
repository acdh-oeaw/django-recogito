from rest_framework import serializers

from recogito.models import RecogitoAnnotation


class RecogitoAnnotationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = RecogitoAnnotation
        fields = ['url', ] + [x.name for x in model._meta.get_fields()]
