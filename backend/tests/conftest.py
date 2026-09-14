"""Offline test configuration: dummy env vars are set BEFORE any backend
import so that the app can be imported without a real MongoDB instance or
Gemini API key. No test performs network or database operations."""
import os
import sys

os.environ.setdefault("GEMINI_API_KEY", "test-key")
os.environ.setdefault("JWT_SECRET", "test-secret-for-pytest")
os.environ.setdefault("MONGODB_URI", "mongodb://localhost:27017/testdb")

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import pytest
from fastapi.testclient import TestClient

from backend.auth import create_access_token
from backend.main import app


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def token_a():
    return create_access_token({"id": "user-A", "email": "a@test.com", "role": "teacher"})


@pytest.fixture()
def token_b():
    return create_access_token({"id": "user-B", "email": "b@test.com", "role": "teacher"})


def auth(token):
    return {"Authorization": f"Bearer {token}"}
