from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from django.conf import settings
from tasks import urls as tasks_urls

admin.site.site_header = 'Task Management'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('users.urls')),
    path('', include(tasks_urls)),

]

