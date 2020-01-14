from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import EmailField
from rest_framework.serializers import CharField
from rest_framework.validators import UniqueValidator
from users.models import CustomUser

class UserCreateSerializer(ModelSerializer):
	email = EmailField(
			required=True,
			validators=[UniqueValidator(queryset=CustomUser.objects.all())]
			)
	password = CharField(min_length=8)
	name = CharField(max_length=255)


	def create(self, validated_data):
		user = CustomUser.objects.create_user(
			email=validated_data['email'],
			username=validated_data['email'],
			password=validated_data['password'],
			name=validated_data['name']
		)
		return user

	class Meta:
		model = CustomUser
		fields = ['id', 'email', 'password', 'name']

class UserListSerializer(ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ['id', 'email', 'name']