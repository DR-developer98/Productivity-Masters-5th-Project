from rest_framework import permissions

# ↓↓↓ CREDIT: Django Rest Framework Code Institue module ↓↓↓
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
# ↑↑↑ CREDIT: Django Rest Framework Code Institue module ↑↑↑
        
        # Check for 'owner' attribute
        # ↓↓↓ CREDIT: Django Rest Framework documentation ↓↓↓
        if hasattr(obj, 'owner'):
            return obj.owner == request.user

        # Check for 'owners' ManyToManyField
        if hasattr(obj, 'owners'):
            return request.user in obj.owners.all()
        # ↑↑↑ CREDIT: Django Rest Framework documentation ↑↑↑