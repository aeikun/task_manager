from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import index

# Create a router and register the TaskViewSet
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    # Include the router URLs for tasks
    path('', include(router.urls)),
    # JWT authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('tasks/', TaskList.as_view(), name='task-list'),  # Example for listing tasks
    # path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('', index, name='index'),
]
