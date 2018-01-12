# _*_ coding:utf-8 _*_
import  xadmin
from xadmin import views

from .models import EmailVerifyRecord, UserProfile, Banner


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "Online Learning"
    site_footer = "Jamal Learning"
    # menu_style = "accordion"

class UserProfileAdmin(object):
    pass


class EmailVerifyRecordAdmin(object):
    search_fields = ['code' , 'email']
    list_display =['code' , 'email']
    list_filter = ['code' , 'email']
    pass


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


# xadmin.site.register(UserProfile , UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord , EmailVerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView , BaseSettings)
xadmin.site.register(views.CommAdminView , GlobalSettings)
xadmin.site.register(Banner, BannerAdmin)