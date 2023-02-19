

import json
import sys
from django.core.management.base import BaseCommand
from django.core.serializers.json import DjangoJSONEncoder
from users.models import User
class Command(BaseCommand):
    help = "Extracting user data to JSON format"

    def handle(self, *args, **options):
        # Get User Data from User Model in monolith        
        user_microservice_data = User.objects.all()
        for user_data in user_microservice_data:
            data = {
                "model": "User",
                "id": user_data.id,
                "username": user_data.username,
                "mobile_number": user_data.mobile_number,
                "created_at": user_data.created_at,
            }
            # Dumping Data into JSON Format
            json.dump(data, sys.stdout, cls=DjangoJSONEncoder)
            sys.stdout.write("\n")