from django.db import models


class User(models.Model):
	owner_email = models.EmailField(unique=True, null=False)
	owner_name = models.CharField(max_length=20, null=False)

	def to_dict(self) -> dict:


		return {
			"name": self.owner_name,
			"email": self.owner_email
		}

class Pet(models.Model):
	pet_name = models.CharField(max_length=20, null=False)
	pet_breed = models.CharField(max_length=20)

	def to_dict(self):
		return {
			"name": self.pet_name,
			"breed": self.pet_breed
		}

class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE) ## User can have many pet profiles?
	pet = models.OneToOneField(Pet, on_delete=models.CASCADE)

	def to_dict(self):
		return {
			"user": self.user.to_dict(),
			"pet": self.pet.to_dict()
		}