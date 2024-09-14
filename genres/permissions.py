from rest_framework import permissions

# herda de BasePermissions
class GenrePermissionClass(permissions.BasePermissions):
    def has_permission(self, request,view):
        # podemos validar o que quiser aqui
        # view, add, change, delete ('nomedoapp.permissao_model')
        if request.method in ['GET', 'OPTIONS', 'HEAD']:            
            return request.user.has_permission('genres.view_genre')
        if request.method == 'POST':
            return request.user.has_permission('genres.add_genre')
        if request.method in ['PUT', 'PATH']:
            return request.user.has_permission('genres.change_genre')
        if request.method == 'DELETE':
            return request.user.has_permission('genres.delete_genre')
        
        return False