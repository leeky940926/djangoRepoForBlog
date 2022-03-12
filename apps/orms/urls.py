from django.urls import path

from apps.orms.views import NonRaceConditionView, RaceConditionView

urlpatterns = [
    path('/race-conditions/<int:cloth_id>', RaceConditionView.as_view()),
    path('/non-race-conditions/<int:cloth_id>', NonRaceConditionView.as_view())
]
