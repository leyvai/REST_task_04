from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Flight, Booking


class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ['destination', 'time', 'price', 'id']


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'id']


class BookingDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'passengers', 'id']


class UpdateBookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['date', 'passengers']

class RegistrationSerializer(serializers.ModelSerializer):
		password = serializers.CharField(write_only=True)

		class Meta:
			model = User
			fields = ["username", "password", "first_name", "last_name"]

		def create(self, validated_data):
			u = validated_data["username"]
			p = validated_data["password"]
			f = validated_data["first_name"]
			l = validated_data["last_name"]
			user = User(username=u, first_name=f, last_name=l)
			user.set_password(p)
			user.save()

			return validated_data



