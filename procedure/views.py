from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from procedure.models import Procedure
from procedure.permissions import UserIsOwnerProcedure
from procedure.serializers import ProcedureSerializer


class ProcedureListCreateAPIView(ListCreateAPIView):
    serializer_class = ProcedureSerializer

    def get_queryset(self):
        return Procedure.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProcedureDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProcedureSerializer
    lookup_field = 'procedure_id'
    queryset = Procedure.objects.all()
    permission_classes = (IsAuthenticated, UserIsOwnerProcedure)


