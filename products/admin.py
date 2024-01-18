from django.contrib import admin
#from django.http.request import HttpRequest
from .models import Tv, Phone, Laptop, Earbud
from guardian.admin import GuardedModelAdmin
from guardian.shortcuts import get_objects_for_user

@admin.register(Laptop)
@admin.register(Tv)
@admin.register(Earbud)
@admin.register(Phone)
class PhoneAdmin(GuardedModelAdmin):
    list_display = ('brand', 'model', 'price')

    def has_module_permission(self, request):
        if super().has_module_permission(request):
            return True 
        return self.has_permission(request, obj=None, action='view')

    def get_queryset(self, request):
        if request.user.is_superuser:
            print("is superuser:", request.user.is_superuser)
            return super().get_queryset(request)
        data = self.get_model_objects(request)
        return data # returns True if data, and False if not data

    def get_model_objects(self, request, action=None, klass=None):
        opts = self.opts
        actions = [action] if action else ['view','edit','delete']
        klass = klass if klass else opts.model
        model_name = klass._meta.model_name

        queryset = get_objects_for_user(user=request.user, perms=[f"{perm}_{model_name}" for perm in actions], klass=klass, any_perm=True)
        print(queryset)
        return queryset

    def has_permission(self, request, obj, action):
        opts = self.opts
        code_name = f"{action}_{opts.model_name}"
        if obj:
            return request.user.has_perm(f"{opts.app_label}.{code_name}", obj)
        else:
            return True

    def has_add_permission(self, request, obj=None):
        return self.has_permission(request, obj, 'add')
    
    def has_view_permission(self, request, obj=None):
        return self.has_permission(request, obj, 'view')
    
    def has_change_permission(self, request, obj=None):
        return self.has_permission(request, obj, 'change')
    
    def has_delete_permission(self, request, obj=None):
        return self.has_permission(request, obj, 'delete')