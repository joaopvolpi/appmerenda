from rest_framework.permissions import BasePermission, SAFE_METHODS

class QueroDoar(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if (request.method in SAFE_METHODS):
                return True
            if request.user.quero_doar:
                return True
        return False

class Validado(BasePermission):

    message = 'Seu usuário ainda não foi validado!'
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.validado:
            return True
        return False
