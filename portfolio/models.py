from django.db import models

# Create your models here.

class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomModel(TimestampMixin, models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    icon = models.ImageField(upload_to='icon/%Y/%m/%d', blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
    

class Technology(CustomModel):
    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"


class Link(CustomModel):
    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"


class Project(TimestampMixin, models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/%Y/%m/%d', blank=True)
    technology = models.ForeignKey(Technology,  on_delete=models.CASCADE, related_name="project_technologies")
    link = models.ForeignKey(Technology,  on_delete=models.CASCADE, related_name="project_links")



