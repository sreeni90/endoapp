from django.contrib.auth.models import User
from rest_framework import serializers
from procedure.models import Procedure,EndoPolyp, EndoMiniclip,EndoCenter


class ProcedureUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "email", "date_joined")

class ProcedurePolypSerializer(serializers.ModelSerializer):

    class Meta:
        model = EndoPolyp
        fields = ("size","removed_by_equipment", "location")


class ProcedureMiniClipSerializer(serializers.ModelSerializer):

    class Meta:
        model = EndoMiniclip
        fields = ("clip_link","equipment_id", "created_at","polyp_id")

class ProcedureCenterSerializer(serializers.ModelSerializer):

    class Meta:
        model = EndoCenter
        fields = ("center_name","room_id")


class ProcedureSerializer(serializers.ModelSerializer):
    polyps = ProcedurePolypSerializer(many=True,read_only=True)
    miniclip = ProcedureMiniClipSerializer(many=True,read_only=True)
    center = ProcedureCenterSerializer(read_only=True)
    class Meta:
        model = Procedure
        fields = ("procedure_id", "start_time", "room_id","cecum_time","inside_time","stop_time","polyps","miniclip","center")