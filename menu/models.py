from django.db import models
from django.urls import reverse


class Menu(models.Model):
    """Model definition for MenuItem."""
    title = models.CharField(
        verbose_name='title', max_length=64)
    is_main = models.BooleanField(default=False)
    parent = models.ForeignKey(
        'self', blank=True, null=True, related_name='child')
    slug = models.CharField(
        verbose_name='slug', max_length=64, blank=True, null=True)
    url = models.CharField(
        verbose_name='URL', max_length=200, blank=True, null=True)
    named_url = models.CharField(
        verbose_name='named URL', max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for MenuItem."""

        verbose_name = 'MenuItem'
        verbose_name_plural = 'MenuItems'

    def __str__(self):
        """Unicode representation of MenuItem."""
        return self.title

    def get_url(self):
        if self.named_url:
            return reverse(self.named_url)
        elif self.url:
            return reverse(self.url)
        elif self.slug:
            return reverse('draw', args=(self.slug,))
        return '/'
