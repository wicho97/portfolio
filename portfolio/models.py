from django.db import models


from django_ckeditor_5.fields import CKEditor5Field


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


class Information(models.Model):
    name_complete = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatar/", blank=True, null=True)
    about = CKEditor5Field(config_name="extends")
    cv = models.FileField(upload_to="cv/", blank=True, null=True)

    def __str__(self):
        return self.name_complete


class Social(TimestampMixin, models.Model):
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)


class Project(TimestampMixin, models.Model):
    title = models.CharField(max_length=100)
    description = CKEditor5Field(config_name="extends")
    image = models.ImageField(upload_to="portfolio/%Y/%m/%d", blank=True)
    demo = models.URLField(blank=True)
    github = models.URLField(blank=True)
    technologies = models.ManyToManyField(
        Technology, related_name="projects", blank=True
    )

    def __str__(self):
        return self.title


class Experience(TimestampMixin, models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    description = CKEditor5Field(config_name="extends")
    the_year = models.CharField(max_length=50)

    def __str__(self):
        return self.title
