from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from config import settings

class CustomUser(AbstractUser):
#     COUNTRY_CHOICES =(
#     ("1", "United States Of America"),
#     ("2", "United Kingdom"),
#     ("3", "Canada"),
# )
#     country = models.ChoiceField(choices = COUNTRY_CHOICES)
    pass

    def __str__(self):
        return self.email


class Company(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user.socialaccount_set.filter(provider='google')[0].extra_data['picture']
    name = models.CharField(max_length=30)
    eni = models.CharField(max_length=30, default='')
    address = models.CharField(max_length=30, default='')
    zip = models.CharField(max_length=30, default='')
    entity_type= models.CharField(max_length=30, default='')
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return self.user.first_name + 'company'




    def save(self, *args, **kwargs):
            super().save( *args, **kwargs)

            # img = Image.open(self.image.path)

            # if img.height > 300 or img.width > 300:
            #     output_size = (200, 200)
            #     img.thumbnail(output_size)
            #     img.save(self.image.path) 