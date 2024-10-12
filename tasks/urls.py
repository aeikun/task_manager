from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import index, YourApiView  # Make sure to import YourApiView

# Create a router and register the TaskViewSet
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', index, name='index'),  # This maps the root URL to the index view
    path('api/', YourApiView.as_view(), name='api_endpoint'),  # Your new API endpoint
    # JWT authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Uncomment and adjust if you want to add specific task-related paths
    # path('tasks/', TaskList.as_view(), name='task-list'),  
    # path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('api/', include(router.urls)),  # Include the router URLs for tasks
]