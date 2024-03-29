from django.contrib.auth.models import User
from .serializers import UserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['admin'] = user.is_staff
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(http_method_names=['post'])
def signup(request):
    try:
        user_data = request.data

        is_admin = user_data.get('is_staff', False)

        user = User.objects.create_user(username=user_data['username'], email=user_data['email'], password=user_data['password'], is_staff=is_admin)
        user.save()

        return Response(f"O usuário {user_data['username']} foi cadastrado com sucesso!", status=status.HTTP_201_CREATED)
    except:
        return Response('Não foi possível realizar o cadastro! Tente novamente e se o erro persistir contate a admnistração.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(http_method_names=['get'])
def read_users(request):
    try:
        users = User.objects.all()

        if(users):
            serializer = UserSerializer(instance=users, many=True)
            return Response(serializer.data)
        
        return Response('Nenhum usuário cadastrado no momento!', status=status.HTTP_404_NOT_FOUND)
    
    except:
        return Response('Não foi possível acessar os usuários no banco!', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(http_method_names=['get', 'patch', 'delete'])
def read_update_delete_user(request, pk):
    try: 
        user = User.objects.get(pk=pk)

    except:
        return Response(f'Não foi possível incontrar um usuário com o id {pk}', status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        try:
            serializer = UserSerializer(
                instance=user, 
                many=False
            )

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except:
            return Response(f'Não foi possível buscar os dados do usuário de id {pk}.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'PATCH':
        try:
            serializer = UserSerializer(
                instance=user,
                data=request.data,
                many=False,
                context={'request': request},
                partial=True
            )

            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            return Response(f'Não foi possível atualizar os dados do usuário de id {pk}.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'DELETE':
        try:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except:
            return Response(f'Não foi possível deletar o usuário de id {pk}.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)