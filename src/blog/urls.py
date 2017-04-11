from django.conf.urls import url

from .views import PostListView, PostDetailView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
]
