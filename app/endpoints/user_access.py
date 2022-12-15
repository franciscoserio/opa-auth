from fastapi import APIRouter, status

from app.schemas import UserAccessResponse, UserInfo
from app.services import UserAccessService

router = APIRouter()


@router.post(
    "/api/user-access/",
    status_code=status.HTTP_200_OK,
    response_model=UserAccessResponse,
)
def check_user_access(user_info: UserInfo):
    user_access_service = UserAccessService(user_info=user_info)
    user_access_service.run()
    return UserAccessResponse(hasAccess=user_access_service.has_access)
