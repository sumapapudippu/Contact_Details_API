from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
class Contact(TimeStampedModel):
    frist_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

    def __str__(self):
    	return self.frist_name +' '+ self.last_name

class ContactDetails(TimeStampedModel):
    name = models.ForeignKey(Contact, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    address = models.TextField()

    def __str__(self):
    	return self.email


