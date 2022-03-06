from django.urls import path

from apps.tdds.views import RoleView

urlpatterns = [
    path('/roles', RoleView.as_view())
]
