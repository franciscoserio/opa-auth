from fastapi import HTTPException, status


class ErrorException(HTTPException):
    def __init__(self, detail):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = detail
