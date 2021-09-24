from django.urls import path, include
from .api import EmployeeCreateApi
from .api import EmployeeApi
from .api import EmployeeUpdateApi
from .api import EmployeeDeleteApi
from webbrowser import get
# from employee.views import EmployeeViewSet
from .RenderViews import listViewSet

from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'users', EmployeeViewSet, basename='user')
# router.register(r'list', EmployeeViewSet, basename='list'),
# router.register(r'create-employee', EmployeeViewSet, basename='create-employee')
router.register(r'list', listViewSet.index, basename='list'),
# router.register(r'create-employee',listViewSet.index, basename='create-employee')
# router.register(r'abc/', EmployeeViewSet)
  

urlpatterns = [
    # path('api',EmployeeApi.as_view()),
    # path('api/get',EmployeeApi.as_view()),
    # path('api/post',EmployeeViewSet.as_view()),
    # path('hero/get/<int:pk>',views.EmployeeViewSet),
    # path('hero/get/<int:pk>',views.EmployeeViewSet.get),
    # path('api/create',EmployeeCreateApi.as_view()),
    # path('api/<int:pk>',EmployeeUpdateApi.as_view()),
    # path('api/<int:pk>/delete',EmployeeDeleteApi.as_view()),
    # path(r'', include(router.urls)),
    path('', listViewSet.index, name="index-page"),
    # path('list', listViewSet.list,name = "list-page"),
    path('create-employee/',listViewSet.create,name = "create-employee"),
    path('get-employee/',listViewSet.list,name = "get-employee"),
    path('update-employee/<int:pk>',listViewSet.update,name = "update-employee"),
    path('destroy-employee/<int:pk>',listViewSet.destroy,name = "destroy-employee"),

]