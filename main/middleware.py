from django.http import HttpResponseForbidden
from ipware import get_client_ip

class BlockIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Define the list of blocked IP addresses
        self.blocked_ips = []  # Add the IPs you want to block

    def __call__(self, request):
        client_ip, _ = get_client_ip(request)
        print(client_ip)

        # Check if the client's IP is in the blocked list
        if client_ip in self.blocked_ips:
            return HttpResponseForbidden("Access Forbidden")
        
        # Allow the request to proceed to the next middleware or view
        return self.get_response(request)