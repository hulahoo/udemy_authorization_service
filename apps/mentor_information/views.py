from rest_framework.generics import CreateAPIView

from permissions.mentor import IsUserMentor
from apps.mentor_information.models import MentorInformation
from apps.mentor_information.serializers import MentorInformationSerializer


class CreateMentorInformationView(CreateAPIView):
    queryset = MentorInformation.objects.all()
    serializer_class = MentorInformationSerializer
    permission_classes = [IsUserMentor]
