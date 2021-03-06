from django.urls import path
# from .views.mango_views import Mangos, MangoDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.services_views import AllServices, ClientDetail
from .views.checkout_views import StripeCheckoutView

urlpatterns = [
  	# Restful routing
    # path('mangos/', Mangos.as_view(), name='mangos'),
    path('services/', AllServices.as_view(), name='services'),
    path('client/', ClientDetail.as_view(), name='client_services'),
    path('checkout/', StripeCheckoutView.as_view(), name='checkout'),
    # path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
