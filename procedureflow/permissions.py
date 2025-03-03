


from rest_framework.permissions import BasePermission



class UpdatePermissions(BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.writer and request.user == obj.writer:
            return True
        return False