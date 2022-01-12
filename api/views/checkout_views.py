# Import key from project settings
from json.encoder import JSONEncoder
from django.conf import settings
from django.http.request import QueryDict

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import redirect


import stripe
# This is your test secret API key.
stripe.api_key = settings.STRIPE_SECRET_KEY

class StripeCheckoutView(APIView):
    # Override the authentication/permissions classes so this endpoint
    # is not authenticated & we don't need any permissions to access it.
    authentication_classes = ()
    permission_classes = ()
    def post(self, request):
        # This gets me the objects to match the User Selected Services Passed Down by State from React FE
        # with the array of objects I will create here to store the KV of service name and Price ID from Stripe
        for key, value in QueryDict.items(request.data):
            print(key)
            print(value)
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': 'price_1KGlJ1HRuIv0fDSuFPIp3Frq',
                        'quantity': 1,
                    },
                    {
                        'price': 'price_1KGlIlHRuIv0fDSuilPnZcyV',
                        'quantity': 1,
                    }
                ],
                payment_method_types=['card',],
                mode='payment',
                success_url=settings.CHECKOUT_URL_REDIRECT + '?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url=settings.CHECKOUT_URL_REDIRECT+ '?canceled=true',
            )
            return redirect(checkout_session.url)
        except:
            return Response(
                {'error': 'Something went wrong when creating Stripe checkout session'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )