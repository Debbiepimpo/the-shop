from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
def content_file_name(instance, filename):
    # Generate a unique filename for the uploaded image
    # For example, you can use a combination of timestamp and the original filename
    # Here's an example implementation:
    import os
    from datetime import datetime
    basefilename, file_extension = os.path.splitext(filename)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = f"{basefilename}_{timestamp}{file_extension}"
    return new_filename


class Items(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.FloatField(null=True, blank=True)
    photo = models.ImageField(upload_to=content_file_name)

    class Meta:
        verbose_name = _("Artículo")
        verbose_name_plural = _("Artículos")

    STATUS_CHOICES = (
            ('Available', 'Disponible'),
            ('Current Unavailable', 'No Disponible')
    )
    status = models.CharField(
            max_length=20,
            choices=STATUS_CHOICES,
            default='Available'
    )

    def __str__(self):
        return self.name
