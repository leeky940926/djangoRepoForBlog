from django.urls import path

from apps.tdds.views import RoleView, SignUpView, UserListView

urlpatterns = [
    path('/roles', RoleView.as_view()),
    path('/signup', SignUpView.as_view()),
    path('/users', UserListView.as_view())   
]
