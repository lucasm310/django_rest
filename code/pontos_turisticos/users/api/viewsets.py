from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from users.models import CustomUser
from .serializers import UserListSerializer
from .serializers import UserCreateSerializer


class UserViewSet(ModelViewSet):
	queryset = CustomUser.objects.all()

	def get_serializer_class(self):
		if self.action == 'list':
			return UserListSerializer
		elif self.action == 'create':
			return UserCreateSerializer
		else:
			return UserListSerializer
