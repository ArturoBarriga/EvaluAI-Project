"""Unit tests for the JWT layer (backend/auth.py). Fully offline."""
import datetime as dt

import jwt
import pytest
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials

from backend import auth as auth_mod


def _creds(token: str) -> HTTPAuthorizationCredentials:
    return HTTPAuthorizationCredentials(scheme="Bearer", credentials=token)


def test_token_roundtrip():
    token = auth_mod.create_access_token({"id": "u1", "email": "x@y.z", "role": "teacher"})
    user = auth_mod.get_current_user(_creds(token))
    assert user == {"id": "u1", "email": "x@y.z", "role": "teacher"}


def test_expired_token_rejected():
    payload = {"sub": "u1", "email": "x@y.z", "role": "teacher",
               "exp": dt.datetime.now(dt.timezone.utc) - dt.timedelta(minutes=1)}
    token = jwt.encode(payload, auth_mod.JWT_SECRET, algorithm=auth_mod.JWT_ALGORITHM)
    with pytest.raises(HTTPException) as e:
        auth_mod.get_current_user(_creds(token))
    assert e.value.status_code == 401


def test_tampered_token_rejected():
    token = auth_mod.create_access_token({"id": "u1", "email": "x@y.z", "role": "teacher"})
    with pytest.raises(HTTPException) as e:
        auth_mod.get_current_user(_creds(token + "x"))
    assert e.value.status_code == 401


def test_wrong_secret_rejected():
    payload = {"sub": "u1", "exp": dt.datetime.now(dt.timezone.utc) + dt.timedelta(hours=1)}
    token = jwt.encode(payload, "another-secret", algorithm=auth_mod.JWT_ALGORITHM)
    with pytest.raises(HTTPException) as e:
        auth_mod.get_current_user(_creds(token))
    assert e.value.status_code == 401
