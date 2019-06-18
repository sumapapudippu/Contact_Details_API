from django.shortcuts import render
from rest_framework import viewsets
from contactbook.models import Contact, ContactDetails
from contactbook.serializers import ContactSerializer, ContactDetailsSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
	page_size = 10

class ContactCRUD(viewsets.ModelViewSet):
	queryset = Contact.objects.all()
	serializer_class = ContactSerializer
	authentication_classes = [TokenAuthentication,]
	permission_classes = [IsAuthenticatedOrReadOnly,]

class ContactDetailsCRUD(viewsets.ModelViewSet):
	queryset = ContactDetails.objects.all()
	serializer_class = ContactDetailsSerializer
	authentication_classes = [TokenAuthentication,]
	permission_classes = [IsAuthenticatedOrReadOnly,]
	pagination_class = MyPagination

	# def get_queryset(self):
	# 	qs = ContactDetails.objects.all()
	# 	phone_num = self.request.GET.get('phone_number')
	# 	email = self.request.GET.get('email')
	# 	if phone_num is not None:
	# 		qs = qs.filter(phone_number__icontains=phone_num, email__icontains=email)
	# 	return qs
