from django.urls import path

from apps.tdds.views import RoleView, SignUpView

urlpatterns = [
    path('/roles', RoleView.as_view()),
    path('/signup', SignUpView.as_view())    
]
