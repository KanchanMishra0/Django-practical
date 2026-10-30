from django.db import models


class LostFoundReport(models.Model):
    item_name = models.CharField(max_length=100)
    report_type = models.ChoiceField(choices=[('lost', 'Lost'), ('found', 'Found')])
    description = models.TextField()
    created_at