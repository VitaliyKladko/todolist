from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from goals.models import GoalComment
from goals.permissions import GoalCommentPermission
from goals.serializers import GoalCommentSerializer, GoalCommentWithUserSerializer


class GoalCommentCreateView(generics.CreateAPIView):
    serializer_class = GoalCommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class GoalCommentList(generics.ListAPIView):
    serializer_class = GoalCommentWithUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['goal']
    ordering = ['-created']

    def get_queryset(self):
        return GoalComment.objects.select_related('user').filter(user=self.request.user)


class GoalCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [GoalCommentPermission]
    serializer_class = GoalCommentWithUserSerializer

    def get_queryset(self):
        return GoalComment.objects.select_related('user')
