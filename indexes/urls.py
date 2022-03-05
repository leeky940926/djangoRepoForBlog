from django.urls import path

from indexes.views import IndexFirstNameView

urlpatterns = [
    path('/firstname', IndexFirstNameView.as_view())
]
