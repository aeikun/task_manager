from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import index, YourApiView

# Create a router and register the TaskViewSet
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', index, name='index'),  # This maps the root URL to the index view
    path('api/', YourApiView.as_view(), name='api_endpoint'),  # Your new API endpoint
    # JWT authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Include the router URLs for tasks
    path('api/', include(router.urls)),  
]
