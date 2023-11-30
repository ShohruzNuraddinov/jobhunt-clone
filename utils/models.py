from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return self.title
        except:
            return str(self.id)

    class Meta:
        abstract = True
