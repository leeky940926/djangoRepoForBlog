from django.urls import path

from apps.orms.views import NonRaceConditionView, RaceConditionView

urlpatterns = [
    path('/race-conditions', RaceConditionView.as_view()),
    path('/non-race-conditions', NonRaceConditionView.as_view())
]
