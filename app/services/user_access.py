from app.schemas import UserInfo
from app.utils import OPA


class UserAccessService:
    """
    Service responsible to get info regarding user access
    from OPA (Open Policy Agent) via Rest API

    parameters: user_info (object)
    """

    def __init__(self, user_info: UserInfo) -> None:
        self.user_info: UserInfo = user_info
        self._has_access: bool = False

    @property
    def has_access(self) -> bool:
        return self._has_access

    def run(self) -> None:
        self._get_user_access()

    def _get_user_access(self) -> None:
        self._has_access = OPA.get_user_access(
            username=self.user_info.username, role=self.user_info.role
        )
