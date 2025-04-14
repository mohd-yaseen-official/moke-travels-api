import json

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

import requests

from django.contrib.auth.models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    
    email = request.data['email']
    password = request.data['password']
    name = request.data['name']
    
    if not User.objects.filter(username=email).exists():
        user = User.objects.create_user(
            username=email,
            password=password,
            first_name=name
        )

        protocol = 'https://' if request.is_secure() else 'http://'

        url = protocol + request.get_host() + '/api/v1/auth/token/'
        headers = {
            'Content-Type' : 'application/json'
        }
        data = {
            "username": email,
            "password":  password,
        }

        response = requests.post(url=url, headers=headers, data=json.dumps(data))

        if response.status_code == 200: 

            response_data = {
                'status':2200,
                'token': response.json(),
                'message': 'User created successfully' 
            }

            return Response(response_data)
        else:
            response_data = {
                'status':2400,
                'message': 'Failed to create user'
            }
            return Response(response_data)
    
    else:
        response_data = {
            'status':2400,
            'message': 'User Already Exists' 
        }

        return Response(response_data)