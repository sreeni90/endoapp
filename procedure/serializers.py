from django.contrib.auth.models import User
from rest_framework import serializers
from procedure.models import Procedure


class ProcedureUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "email", "date_joined")


class ProcedureSerializer(serializers.ModelSerializer):
    user = ProcedureUserSerializer(read_only=True)

    class Meta:
        model = Procedure
        fields = ("user","procedure_id", "start_time", "room_id","cecum_time","inside_time","stop_time")