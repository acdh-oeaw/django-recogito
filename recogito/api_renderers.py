import json
from rest_framework import renderers


class RecogitoRenderer(renderers.BaseRenderer):
    media_type = 'application/json'
    format = 'recogito'

    def render(self, data, media_type=None, renderer_context=None):
        payload = [x['re_payload'] for x in data]
        return json.dumps(payload)
