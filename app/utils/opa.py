import requests

from urllib.parse import urljoin

from app.utils.exceptions import ErrorException

from .configs import OPA_URL, OPA_USER_ACCESS_ENDPOINT


class OPA:
    """
    This class is responsible to connect to the OPA service and
    perform requests to its endpoints
    """

    @staticmethod
    def get_user_access(username: str, role: str) -> bool:
        headers = {"Content-type": "application/json"}
        payload = {"input": {"username": username, "role": role}}
        url = urljoin(OPA_URL, OPA_USER_ACCESS_ENDPOINT)

        try:
            response = requests.post(url, json=payload, headers=headers)
            response = response.json()
            return response["result"]["allow"]
        except Exception:
            raise ErrorException("There was an error connecting to OPA service")
