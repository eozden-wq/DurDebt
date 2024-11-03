from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import UserProfileSerializer
# Create your views here.

class GetUserProfileView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user

            use = User.objects.get()

            user_profile = UserProfile.objects.get(user=user)
            user_profile = UserProfileSerializer(user_profile)

            return Response({'profile': user_profile.data, 'username': str(user.username), 'balance': float(user_profile.data.balance)})
        except:
            return Response({'error': 'User not found'})

class UpdateUserProfileView(APIView):
    def put(self, request, format=None):
        try:
            user = self.request.user
            username = user.username

            data = self.request.data
            first_name = data['first_name']
            last_name=  data['last_name']

            user = User.objects.get(id=user.id)

            UserProfile.objects.filter(user=user).update(first_name=first_name, last_name=last_name)

            user_profiles = UserProfile.objects.get(user=user)
            user_profile = UserProfileSerializer(user_profiles)

            return Response({'profile': user_profile.data, 'username': str(user.username) })
        except:
            return Response({'error': 'Error updating user profile'})
