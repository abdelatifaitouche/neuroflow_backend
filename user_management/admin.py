from django.contrib import admin
from .models import CustomUser , Departement
from django.contrib.auth.admin import UserAdmin
# Register your models here.




class CustomUserAdmin(UserAdmin):
    # Fields to display in the admin
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_active','departement', 'date_joined']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['email', 'first_name', 'last_name']

    # The fields to be used in the form for adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2' , 'departement')}
        ),
    )

    # The fields to be used in the form for editing an existing user
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name' , 'departement')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Define how the user should be created
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is new, set password manually
            obj.set_password(form.cleaned_data["password1"])
        super().save_model(request, obj, form, change)

# Register the CustomUser model with the custom admin
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Departement)