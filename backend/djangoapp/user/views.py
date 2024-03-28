from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser
from .serializers import UserSerializer

@api_view(http_method_names=['get'])
def read_users(request):
    try:
        users = CustomUser.objects.all()
        
        if(users):
            serializer = UserSerializer(instance=users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response('Não foi possível encontrar nenhum usuário!', status=status.HTTP_404_NOT_FOUND)
    except:
        return Response('Algo deu errado ao buscar os usuários!', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(http_method_names=['get', 'patch', 'delete'])
def put_detail_delete_user(request, pk):
    try:
        user = CustomUser.objects.get(pk=pk)

        if request.method == 'GET':
            serializer = UserSerializer(
                instance=user,
                many=False,
                context={'request': request}
            )

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'PATCH':
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
        
        elif request.method == 'DELETE':
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    except:
        return Response(f'Não foi possível encontrar o usuário de id {pk}', status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def login(request):
    try:        
        user = CustomUser.objects.get(email=request.data['email'])

        if not user.check_password(request.data['password']):
            return Response('Email ou senha não encontrado!', status=status.HTTP_404_NOT_FOUND)

        token, created = Token.objects.get_or_create(user=user)
        
        return Response({'token': token.key})
    
    except:
        return Response(f'Usuário com email {request.data['email']} não encontrado!', status=status.HTTP_404_NOT_FOUND)
        
    
    

    
@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = CustomUser.objects.get(email=request.data['email'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)

        return Response({'token': token.key, "user": serializer.data})
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response({
        'id': request.user.id,
        'email': request.user.email,
        'username': request.user.username,
        'createAt': request.user.created_at,
        'updateAt': request.user.updated_at,
        'isSuperUser': request.user.is_superuser
    })