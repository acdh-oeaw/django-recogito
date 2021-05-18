# django-recogito

[![Test](https://github.com/acdh-oeaw/django-recogito/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/acdh-oeaw/django-recogito/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/acdh-oeaw/django-recogito/branch/master/graph/badge.svg?token=mX5llsx4Fz)](https://codecov.io/gh/acdh-oeaw/django-recogito)

A python package to integrate [recogito-js](https://github.com/recogito/recogito-js) in a django-project


## install

`pip install django_recogito`

add `recogito` to INSTALLED_APPS as well as `rest_framework` and `django_filters`:

```python
#  project/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'recogito',
    'example',
]
```

register the annotation api-endpoint in your project's `urls.py`:
```python
#  project/urls.py

from django.urls import path, include
from rest_framework import routers
from recogito import api_views

router = routers.DefaultRouter()
router.register(r'recogitoannotations', api_views.RecogitoAnnotationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/', include(router.urls)),
]
```

run migrations `python manage.py migrate`



