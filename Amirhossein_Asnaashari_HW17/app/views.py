from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from rest_framework.viewsets import ReadOnlyModelViewSet


class PostViewSet(ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class CommentViewSet(ReadOnlyModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
