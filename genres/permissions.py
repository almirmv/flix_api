from rest_framework import permissions

# herda de BasePermissions
class GenrePermissionClass(permissions.BasePermissions):
    def has_permission(self, request,view):
        # podemos validar o que quiser aqui
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            # view, add, change, delete ('nomedoapp.permissao_model')
            return request.user.has_permission('genres.view_genre')
        return False