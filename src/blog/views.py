from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from pure_pagination.mixins import PaginationMixin

from .models import Post


class PostListView(PaginationMixin, ListView):
    paginate_by = 5
    template_name = "blog/post_list.html"
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.select_related('author')


class PostDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.select_related('author')