from django.views.generic import ListView

from blog.models import Article


class PostListView(ListView):
    model = Article
    template_name = "blog/post_list.html"