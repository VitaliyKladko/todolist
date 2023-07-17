from django.db import models

from core.models import User


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class GoalCategory(BaseModel):
    title = models.CharField(verbose_name="Название", max_length=255)
    user = models.ForeignKey(User, verbose_name="Автор", on_delete=models.PROTECT)
    is_deleted = models.BooleanField(verbose_name="Удалена", default=False)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
