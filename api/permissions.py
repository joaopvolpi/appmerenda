from rest_framework.permissions import BasePermission, SAFE_METHODS


class AdminPodeTudoAutenticadoSoLe(BasePermission):

    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS and request.user.is_authenticated):
            return True
        if request.user.is_staff:
            return True
        return False

class OwnerPraVer(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.usuario == request.user

class QueroDoar(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if (request.method in SAFE_METHODS):
                return True
            if request.user.quero_doar:
                return True
        return False