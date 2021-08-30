from rest_framework import fields, serializers
from .models import Business, Rating
from core.serializers import email_validator

class RegisterBusinessSerializer(serializers.ModelSerializer, serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    secret_phrase = serializers.CharField(required=True)
    profile_image = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = Business
        fields = '__all__'

        extra_kwargs = {
            'user': { 'read_only': True }
        }


    @email_validator
    def validate_email(self, email):
        return email

    def validate_password(self, password):
        if len(password) < 6:
            raise serializers.ValidationError('Password must be 6 characters long')
        
        return password

class ListBusinessSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField('get_rating')
    class Meta:
        model = Business
        fields = ['id', 'business_category', 'address', 'business_name', 'pictures', 'user_id', 'rating']

    def get_rating(self, obj):
        return 5.0

TARGETS = (
    ('BUS', 'Business'),
    ('PRD', 'Product')
)
class RateBusinessOrProductSerializer(serializers.Serializer):
    target = serializers.ChoiceField(choices=TARGETS)
    id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    numberOfStars = serializers.IntegerField()
    comment = serializers.CharField()
    images = serializers.CharField()
   

    