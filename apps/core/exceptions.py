from django.http.response import JsonResponse
from rest_framework.views import exception_handler as _exception_handler


def exception_handler(exc, context):
    response = _exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code

    return response


def not_found_error_handler(request, exception=None):
    return JsonResponse({
        'status_code': 404,
        'error': 'The page was not found'
    })


def internal_server_error_handler(request, exception=None):
    return JsonResponse({
        'status_code': 500,
        'error': 'Internal Server Error'
    })
