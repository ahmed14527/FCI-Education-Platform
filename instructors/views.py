from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def create_superuser(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password :
        return Response({'error': 'Please provide username, password.'}, status=400)

    try:
        user = User.objects.create_superuser(username=username, password=password)
        return Response({'success': 'Superuser created successfully.'}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=400)
