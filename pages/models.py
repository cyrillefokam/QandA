from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.validators import MinValueValidator

# Create your models here.
class Record(models.Model):
	INPUT_CHOICES = (('q', 'Questions'), ('a', 'Answers'))
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	input = models.CharField(choices=INPUT_CHOICES, max_length=1, default=INPUT_CHOICES[0][0])
	topic = models.CharField(max_length=255)
	composer = models.TextField()
	number = models.PositiveIntegerField(
		default=1,
		validators=[MinValueValidator(1)], verbose_name="Number of data to generate")
	generated_data = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
