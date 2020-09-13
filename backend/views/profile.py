from backend.models import Profile
from backend.serializers import ProfileSerializer
from django.http import JsonResponse

from rest_framework import mixins, permissions, generics

class ProfileViewSet(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request): # change this to use the patch mixin
        profile = Profile.objects.filter(user = request.user).first()
        profile.first_name = request.data['first_name']
        profile.last_name = request.data['last_name']
        profile.bio = request.data['bio']
        profile.location = request.data['location']
        profile.save()
        return JsonResponse({"response": "change successful"})