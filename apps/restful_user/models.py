# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.

class UserManager(models.Manager):
	# this is where the validation is going
	def basic_validator(self, postData):
		isValid = False
		errors = {}
		if 'first_name' in postData:
			first_name = postData['first_name'].strip()
			if len(first_name) < 1:
				errors["first_name"] = "First name should not be empty."
			elif not first_name.isalpha:
				errors["first_name"] = "First name should not contain any numbers or symbols."
		
		if 'last_name' in postData:
			last_name = postData['last_name'].strip()
			if len(last_name) < 1:
				errors["last_name"] = "Last name should not be empty."
			elif not first_name.isalpha:
				errors["last_name"] = "Last name should not contain any numbers or symbols."		

		if 'email' in postData:
			email = postData['email'].strip()
			if len(email) < 1:
				errors["email"] = "Email should not be empty."
			elif EMAIL_REGEX.match(email)==None:
				errors["email"] = "Email must be in the correct format."

		print " EMAIL_REGEX.match(email)",  EMAIL_REGEX.match(email)
			

		if len(errors)==0:
			isValid = True
		for i in errors:
			print errors[i], "^^^^^^^^^^^^^^^^^^^^^^^^^THSESE AREA THE ERROS"
		return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = UserManager()