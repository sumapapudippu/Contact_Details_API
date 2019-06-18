from contactbook.models import Contact, ContactDetails
from rest_framework.serializers import ModelSerializer

class ContactSerializer(ModelSerializer):
	class Meta:
		model = Contact
		fields = '__all__'

class ContactDetailsSerializer(ModelSerializer):
	class Meta:
		model = ContactDetails
		fields = '__all__'		