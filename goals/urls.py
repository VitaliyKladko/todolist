from django.urls import path

from goals.apps import GoalsConfig
from goals.views.categories import CategoryCreateView, CategoryListView, CategoryDetailView

app_name = GoalsConfig.name

urlpatterns = [
    path('goal_category/create', CategoryCreateView.as_view(), name='create-category'),
    path('goal_category/list', CategoryListView.as_view(), name='categories-list'),
    path('goal_category/<int:pk>', CategoryDetailView.as_view(), name='category-details'),
]
