
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import StripeWH_Hander

import stripe
import os

from os import path
if path.exists("env.py"):
    import env


@require_POST
@csrf_exempt
def webhook(request):

    wh_secret = os.environ.get('STRIPE_WH_SEC')
    stripe.api_key = settings.STRIPE_SECRET_KEY
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        print('Fail1')
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        print('Fail2')
        return HttpResponse(status=400)
    except Exception as e:
        print('Fail3')
        return HttpResponse(content=e, status=400)

    print('Success!')
    return HttpResponse(status=200)
