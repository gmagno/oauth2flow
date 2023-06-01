# OAuth 2 Authorization Code flow

A trivial implementation of the oauth2 authorization code flow, for illustration purposes only.

https://github.com/gmagno/oauth2flow/assets/46817915/be9d74f8-c00f-4bb2-8a8c-8c586a4b71b6

## Dependencies

- [localtunnel](https://github.com/localtunnel/localtunnel)
- python: fastapi, httpx, pydantic and uvicorn

## Setup

Create a Github OAuth App under your user profile "Developer Settings" menu -> choose "OAuth Apps" -> fill in the form:

![github_oauth_app](https://github.com/gmagno/oauth2flow/assets/46817915/2f831b33-db2a-4bfb-9bdb-8b7187f3cae4)

Create a python environment and install the dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
make run
```
