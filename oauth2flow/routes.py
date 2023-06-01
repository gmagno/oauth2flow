from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from httpx import AsyncClient, Response, codes

from oauth2flow.schemas import Token

GITHUB_OAUTH_CLIENT_ID = "< client_id goes here >"
GITHUB_OAUTH_CLIENT_SECRET = "< client_secret goes here >"
GITHUB_OAUTH_SCOPE = "read:user user:email"
GITHUB_OAUTH_CODE_REDIRECT_URI = "https://oauth2flow.loca.lt/api/v1/oauth/code"
GITHUB_OAUTH_REDIRECT_URI = "https://github.com/login/oauth/authorize"
GITHUB_OAUTH_ALLOW_SIGNUP = True
GITHUB_OAUTH_ACCESS_TOKEN_URL = "https://github.com/login/oauth/access_token"

oauth_router = APIRouter()


@oauth_router.get("/login", include_in_schema=True)
async def login() -> RedirectResponse:
    github_authorize_url: str = (
        f"{GITHUB_OAUTH_REDIRECT_URI}"
        f"?client_id={GITHUB_OAUTH_CLIENT_ID}"
        f"&redirect_uri={GITHUB_OAUTH_CODE_REDIRECT_URI}"
        f"&scope={GITHUB_OAUTH_SCOPE}"
        f"&allow_signup={GITHUB_OAUTH_ALLOW_SIGNUP}"
    )
    return RedirectResponse(github_authorize_url)


@oauth_router.get("/code", include_in_schema=True)
async def code(code: str, state: str) -> RedirectResponse:
    async with AsyncClient(base_url=GITHUB_OAUTH_ACCESS_TOKEN_URL) as ac:
        response: Response = await ac.post(
            "",
            params={
                "client_id": GITHUB_OAUTH_CLIENT_ID,
                "client_secret": GITHUB_OAUTH_CLIENT_SECRET,
                "code": code,
                "redirect_uri": GITHUB_OAUTH_CODE_REDIRECT_URI,
            },
            headers={
                "Accept": "application/json",
            },
        )
    if response.status_code != codes.OK:
        return None

    response_payload = response.json()
    token = Token.parse_obj(response_payload)
    print(token)
    return RedirectResponse("https://oauth2flow.loca.lt/api/docs")
