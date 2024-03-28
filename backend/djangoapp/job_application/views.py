from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import JobApplication
from .serializers import JobApplicationSerializer

@api_view(http_method_names=['get', 'post'])
def read_insert_job_application(request):
    if request.method == 'GET':
        try:
            job_applications = JobApplication.objects.all()

            if job_applications:
                serializer = JobApplicationSerializer(instance=job_applications, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            return Response('Não foi possível encontrar nenhuma candidatura.', status=status.HTTP_404_NOT_FOUND)
        except:
            return Response('Algo deu errado ao tentar buscar suas candidaturas. Contate a administração!', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        try:
            print(request.data)
            serializer = JobApplicationSerializer(
                data=request.data,
                context={'request': request}
            )

            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except:
            return Response(
                'Não foi possível fazer o cadastro da candidatura no momento, tente mais tarde ou contate a administração!', 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@api_view(http_method_names=['get', 'patch', 'delete'])
def read_update_delete_job_application(request, pk):
    try:
        job_application = JobApplication.objects.get(pk=pk)

        if request.method == 'GET':
            try:
                serializer = JobApplicationSerializer(
                    instance=job_application,
                    many=False,
                    context={'request': request}
                )
                return Response(serializer.data,status=status.HTTP_200_OK)

            except:
                return Response('Algo deu errado ao buscar os dados da candidatura, se o erro persistir, contate a administração!', status=status.HTTP_500_INTERNAL_SERVER_ERROR)        
            
        elif request.method == 'PATCH':
            try:
                serializer = JobApplicationSerializer(
                    instance=job_application,
                    data=request.data,
                    many=False,
                    context={'request': request},
                    partial=True
                )

                serializer.is_valid(raise_exception=True)
                serializer.save()

                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response('Algo deu errado ao atualizar os dados da candidatura, se o erro persistir, contate a administração!', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        elif request.method == 'DELETE':
            try:
                job_application.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except:
                return Response('Algo deu errado ao apagar os dados da candidatura, se o erro persistir, contate a administração!', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except:
        return Response('Não foi possível encontrar essa candidatura no momento, se o erro persistir, contate a administração!', status=status.HTTP_404_NOT_FOUND) 
