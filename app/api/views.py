from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import User

@api_view(["GET"])
def home(request, *args, **kwargs):

	user_data = User.objects.all().order_by("?").first()
	data = {}
	if user_data:
		data = model_to_dict(user_data)
	return Response(data)
