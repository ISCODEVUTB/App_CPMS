from django.http.response import JsonResponse
from django.views.decorators.http import require_safe

@require_safe
def home(request):
    return JsonResponse({"server": "running successfully"}, safe=False)
