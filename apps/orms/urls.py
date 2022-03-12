from django.urls import path

from apps.orms.views import NonRaceConditionView, RaceConditionView

urlpatterns = [
    path('/race-conditions/<int:posting_id>', RaceConditionView.as_view()),
    path('/non-race-conditions/<int:posting_id>', NonRaceConditionView.as_view())
]
