from django.http import JsonResponse

class EnsureGuestKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Preflight
        if request.method == "OPTIONS":
            return self.get_response(request)

        # Skip for auth endpoints
        if request.path.startswith("/api/auth/"):
            return self.get_response(request)

        # Enforce for anon writes under /api/
        if (not request.user.is_authenticated
            and request.path.startswith("/api/")
            and request.method in {"POST", "PUT", "PATCH"}):
            gk = request.headers.get("X-Guest-Key")
            if not gk:
                return JsonResponse({"detail": "Missing guest key."}, status=400)

        return self.get_response(request)
