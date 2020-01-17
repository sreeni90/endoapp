from rest_framework.permissions import BasePermission


class UserIsOwnerProcedure(BasePermission):

    def has_object_permission(self, request, view, procedure):
        return request.user.id == procedure.user.id
