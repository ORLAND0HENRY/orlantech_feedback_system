from django.http import JsonResponse
from .models import Feedback


def submit_feedback(request):
    if request.method == "POST":
        msg = request.POST.get('message')
        # Capturing the 'Source' to know WHICH project sent it
        source_project = request.META.get('HTTP_HOST', 'Unknown')

        Feedback.objects.create(
            message=msg,
            device_info=request.META.get('HTTP_USER_AGENT'),
            project_name=source_project
        )
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"}, status=400)