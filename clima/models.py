from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE, HARD_DELETE_NOCASCADE

class Busqueda(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    id = models.AutoField(primary_key=True)
    ciudad = models.CharField(max_length=255, db_index=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Busquedas'

    def __str__(self):
        return self.nombre