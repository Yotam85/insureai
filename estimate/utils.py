# estimate/utils.py
from django.core import signing

def get_guest_key(request) -> str | None:
    return (
        request.COOKIES.get("guest_key")
        or request.headers.get("X-Guest-Key")
        or None
    )

