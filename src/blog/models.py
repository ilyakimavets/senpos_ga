from django.conf import settings
from django.db import models
from django.urls import reverse


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['updated_at', 'created_at']

        abstract = True


class Post(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
