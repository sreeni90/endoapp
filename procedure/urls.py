from django.urls import path
from procedure.views import ProcedureListCreateAPIView,ProcedureDetailAPIView

app_name = 'procedure'

urlpatterns = [
    path('', ProcedureListCreateAPIView.as_view(), name="list"),
    path('<str:procedure_id>/',ProcedureDetailAPIView.as_view(), name="detail"),
]
