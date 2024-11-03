import stripe
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import os
from  dotenv import load_dotenv

# Create your views here.

class PaymentView(APIView):
    def post(self, request, format=None):
        try:
            load_dotenv()
            stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
            payment_intent = stripe.PaymentIntent.create(amount=1000, currency='pln', payment_method_types=['card'],
                                                     receipt_email='test@test.com')

            return Response(payment_intent)
        except:
            return Response({'error': 'Error processing payment'})

