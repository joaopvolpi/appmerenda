from rest_framework.permissions import BasePermission, SAFE_METHODS

class QueroDoar(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if (request.method in SAFE_METHODS):
                return True
            if request.user.quero_doar:
                return True
        return False
'''
class NaoQueroDoar(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if (request.method in SAFE_METHODS):
                return True
            if request.user.quero_doar:
                return False
        return False
'''