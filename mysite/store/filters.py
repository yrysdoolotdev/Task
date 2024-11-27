from django_filters import FilterSet
from .models import Task


class TaskFilter(FilterSet):
    class Meta:
        model = Task
        fields = {
            'title_name': ['exact'],
            'created_date': ['gt', 'lt']
        }
