from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, AllowAny
from users.models import CustomUser
from .serializers import UserListSerializer
from .serializers import UserCreateSerializer

class UserViewSet(ModelViewSet):
	authentication_classes = [TokenAuthentication]

	queryset = CustomUser.objects.all()

	def get_permissions(self):
		if self.action == 'create':
			permission_classes = [AllowAny]
		else:
			permission_classes = [IsAdminUser]
		
		return [permission() for permission in permission_classes]

	def get_serializer_class(self):
		if self.action == 'list':
			return UserListSerializer
		elif self.action == 'create':
			return UserCreateSerializer
		else:
			return UserListSerializer
