from rest_framework import serializers

from apps.mentor_information.models import MentorInformation


class MentorInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorInformation
        fields = "__all__"
