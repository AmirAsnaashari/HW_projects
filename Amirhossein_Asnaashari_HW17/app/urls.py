from rest_framework import routers
from .views import PostViewSet, CommentViewSet
from rest_framework.urlpatterns import format_suffix_patterns

blogs_router = routers.DefaultRouter()
blogs_router.register("post", viewset=PostViewSet, basename="posts")
blogs_router.register("comment", viewset=CommentViewSet, basename="comments")

urlpatterns = [
]

urlpatterns = format_suffix_patterns(urlpatterns)
