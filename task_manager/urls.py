from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from tasks.views import api_root

# Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Task Manager API",
        default_version='v1',
        description="API documentation for Task Management API",
        contact=openapi.Contact(email="support@taskmanager.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel

    # Include the task_manager/tasks/urls.py
    path('api/', include('tasks.urls')),  # This includes all the task-related URLs
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('', api_root, name='api-root'),
    
    # Add Swagger documentation route
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
