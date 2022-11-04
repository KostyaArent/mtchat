from django.db import models


class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Room(SingletonModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(verbose_name="Slug", unique="True", help_text="Slug is a field in autocomplete mode, but if you want you can modify its contents")

    def __str__(self):
        return self.name
