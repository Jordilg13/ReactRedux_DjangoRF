from django.db import models
from apps.core.models import TimestampedModel


# Create your models here.
class UserImage(TimestampedModel):
    image = models.FileField(
        blank=False, 
        null=False,
        upload_to="images/"
    )
    owner = models.ForeignKey(
        "profiles.Profile",
        on_delete=models.CASCADE,
        related_name='userimage')
    tags = models.ManyToManyField(
        'userimages.Tag',
        related_name="userimage",
        blank=True
    )

    def __str__(self):
        return self.image.name


class Tag(TimestampedModel):
    tag = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True, unique=True)

    def __str__(self):
        return self.tag