from django.db import models

# Create your models here.


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["created_at"]
        indexes = [
            models.Index(fields=["created_at"]),
        ]


class CustomModel(TimestampMixin, models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="icon/%Y/%m/%d", blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Technology(CustomModel):
    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"


class Project(TimestampMixin, models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to="portfolio/%Y/%m/%d", blank=True)
    technologies = models.ManyToManyField(
        Technology, related_name="projects", blank=True
    )

    def __str__(self):
        return self.title


class Link(CustomModel):
    url = models.URLField(max_length=200)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="links", default=None
    )

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"
