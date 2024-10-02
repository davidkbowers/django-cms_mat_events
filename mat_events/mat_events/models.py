from django.db import models
from django.urls import reverse
from cms.models import CMSPlugin

class MatEvent(models.Model):
    # ... (previous MatEvent model code remains unchanged) ...

class MatEventPlugin(CMSPlugin):
    # ... (previous MatEventPlugin code remains unchanged) ...

class HireService(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=50)  # e.g., "1 hour", "2 hours", etc.
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='hire_service_images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('hire_service_detail', args=[str(self.id)])

class HireServicePlugin(CMSPlugin):
    service = models.ForeignKey(HireService, on_delete=models.CASCADE)

    def __str__(self):
        return self.service.title


class HomePageSection(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='home_page_images/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Order of appearance on the home page")
    link_text = models.CharField(max_length=100, blank=True)
    link_url = models.URLField(blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class HomePageSectionPlugin(CMSPlugin):
    section = models.ForeignKey(HomePageSection, on_delete=models.CASCADE)

    def __str__(self):
        return self.section.title

