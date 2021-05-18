from django.views.generic.detail import DetailView
from example.models import MyText


class MyTextDetailView(DetailView):

    model = MyText
    template_name = 'example/mytext_detail.html'
