from django.db import models


class CodeSave(models.Model):
    code = models.TextField()
    client_id = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.client_id[8]}'
