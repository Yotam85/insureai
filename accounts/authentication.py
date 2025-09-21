from rest_framework.authentication import TokenAuthentication

class BearerTokenAuthentication(TokenAuthentication):
    """Allow Authorization: Bearer <token> in addition to default Token keyword."""
    keyword = "Bearer"
