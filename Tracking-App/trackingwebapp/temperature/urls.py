from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from temperature.models import Post

urlpatterns = [ url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:15],
											template_name="temperature/temperature.html"))]

