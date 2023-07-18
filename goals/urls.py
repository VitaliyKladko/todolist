from django.urls import path

from goals.apps import GoalsConfig
from goals.views.categories import CategoryCreateView, CategoryListView, CategoryDetailView
from goals.views.goals import GoalCreateView, GoalListView, GoalDetailView

app_name = GoalsConfig.name

urlpatterns = [
    # Categories
    path('goal_category/create', CategoryCreateView.as_view(), name='create-category'),
    path('goal_category/list', CategoryListView.as_view(), name='categories-list'),
    path('goal_category/<int:pk>', CategoryDetailView.as_view(), name='category-details'),
    # Goals
    path('goal/create', GoalCreateView.as_view(), name='create-goal'),
    path('goal/list', GoalListView.as_view(), name='goals-list'),
    path('goal/<int:pk>', GoalDetailView.as_view(), name='goal-details'),
]
