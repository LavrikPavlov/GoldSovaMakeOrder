from django.contrib import admin
from .models import Profile, User

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields


class UserResorce(resources.ModelResource):
    id = fields.Field(column_name='ID пользователя', attribute='id')
    email = fields.Field(column_name='Почта', attribute='email')
    phone = fields.Field(column_name='Ном. телефона', attribute='phone')
    adress = fields.Field(column_name='Адресс', attribute='adress')
    org = fields.Field(column_name='Организация', attribute='org')
    succes_user = fields.Field(column_name='Потверждение пользователя', attribute='succes_user')
    email_verify = fields.Field(column_name='Потверждение почты', attribute='email_verify')


    class Meta:
        model = User
        fields = ('id', 'org', 'phone', 'email', 'adress', 'email_verify', 'succes_user')

@admin.register(User)
class UserAdmin(ImportExportActionModelAdmin):
    resource_class = UserResorce
    list_display = ['id', 'org', 'phone', 'email', 'adress','email_verify', 'succes_user', 'is_active']
    list_editable = ['succes_user']
    list_filter = ['email_verify', 'succes_user']
    

admin.site.register(Profile)

