from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle Stripe webhook """

    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        """
        Handle an unknown/enexpected webhook event 
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_inten_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from stripe 
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)
    
    def handle_payment_inten_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from stripe 
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)
