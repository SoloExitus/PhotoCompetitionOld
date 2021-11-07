from django.db.models import Count, Case, When, F
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from rest_framework import viewsets

from competition.models import PhotoPost
from competition.serializers import PhotoPostSerializer


class HomePageView(TemplateView):

    template_name = "competition/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'Home'
        return context


class PhotoPostViewSet(viewsets.ReadOnlyModelViewSet):
    """
     provides `list` and `retrieve` actions.
    """
    queryset = PhotoPost.objects.filter(status=PhotoPost.APPROVED).annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comments', distinct=True),
    )
    serializer_class = PhotoPostSerializer