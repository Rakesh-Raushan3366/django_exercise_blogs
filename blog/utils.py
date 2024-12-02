import requests

def get_client_ip(request):
    # Extract the client's IP from the request
    ip = request.META.get('REMOTE_ADDR')
    return ip

def get_public_ip():
    # Get the current public IP using an external api
    response = requests.get('https://api.ipify.org?format=json')
    public_ip = response.json().get('ip')
    return public_ip

def get_user_country(request):
    # Check if the request is coming from localhost or public domain
    ip = get_client_ip(request)
    if ip == '127.0.0.1':
        ip = get_public_ip()
    
    # Get country information based on the detected IP
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    country = response.json().get('country_name')
    return country


def get_user_country(request):
    return "India"
