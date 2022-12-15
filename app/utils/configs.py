import os
import sys

OPA_URL = os.environ.get("OPA_URL")
OPA_USER_ACCESS_ENDPOINT = os.environ.get("OPA_USER_ACCESS_ENDPOINT")

if not OPA_URL:
    print("Environment variable 'OPA_URL' is not set.")
    sys.exit(0)

if not OPA_USER_ACCESS_ENDPOINT:
    print("Environment variable 'OPA_URL' is not set.")
    sys.exit(0)
