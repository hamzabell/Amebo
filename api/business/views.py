from django.shortcuts import render
from rest_framework import generics, exceptions
from rest_framework.response import Response
from core.models import User
from .models import Business, Product, Rating
from .serializers import RateBusinessOrProductSerializer, RegisterBusinessSerializer, ListBusinessSerializer
from core.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class BusinessRegisterView(generics.GenericAPIView):
    serializer_class = RegisterBusinessSerializer

    def post(self, request, format=None):
        data = request.data
        serializer = self.get_serializer(data=data)

        serializer.is_valid(raise_exception=True)

        validated_data = serializer.data

        business_data = {
            "business_category":  validated_data.pop('business_category', None),
            "address": validated_data.pop('address', None),
            "business_name": validated_data.pop('business_name', None),
            "pictures": validated_data.pop('pictures', None)
        }
        
        password = validated_data.pop('password', None)
        confirm_password = validated_data.pop('confirm_password', None)

        if password != confirm_password:
            raise exceptions.APIException('Passwords do not match')

        user_instance = User(**validated_data)
        user_instance.set_password(password)

        user_instance.user_type = 'BUS'
        user_instance.save()
        
        business_instance = Business(**business_data)

        business_instance.user = user_instance

        business_instance.save()

        response = Response()

        response.data = {
            'message': 'Business created successfully',
        }

        return response


class ListBusinessView(generics.GenericAPIView):
    serializer_class = ListBusinessSerializer
    queryset = Business.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        if pk:
            data = super(ListBusinessView, self).get_queryset()
            business = data.filter(id=pk).first()
            serializer = self.get_serializer(business)
            
            if not business:
                raise exceptions.APIException('Business does not exist')
        else:
            business = self.get_queryset()
            serializer = self.get_serializer(business, many=True)

        response = Response()
        response.data = {
            'message': 'Data retreived successfully',
            'data': serializer.data
        }

        return response

class RateBusinessView(generics.GenericAPIView):
    serializer_class = RateBusinessOrProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.data

        target = validated_data.pop('target', None)
        id = validated_data.pop('id', None)
        user_id = validated_data.pop('user_id', None)

        user_instance = User.objects.get(pk=user_id)


        if target == 'BUS':
            try:
                business_instance = Business.objects.get(pk=id)
            except Business.DoesNotExist:
                raise exceptions.APIException('Business does not exist')

            rating = Rating(business=business_instance, user=user_instance, **validated_data)
            rating.save()
        else:
            try:
                product_instance = Product.objects.get(pk=id)
            except Product.DoesNotExist:
                raise exceptions.APIException('Product does not exist')

            rating = Rating(product=product_instance, user=user_instance, **validated_data)
            rating.save()

        response = Response()

        response.data = {
            "message": "Your Rating has been received"
        }

        return response