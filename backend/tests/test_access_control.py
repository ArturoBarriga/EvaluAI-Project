"""API access-control tests. Repository functions are monkeypatched, so no
test touches MongoDB or the LLM provider."""
from backend.tests.conftest import auth
from backend import auth as auth_mod


def test_missing_token_is_rejected(client):
    assert client.get("/exams/all_my_exams").status_code == 401


def test_invalid_token_is_rejected(client):
    assert client.get("/exams/all_my_exams", headers=auth("not-a-token")).status_code == 401


def test_identity_taken_from_token(client, token_a, monkeypatch):
    seen = {}

    def fake_get_all(user_id):
        seen["user_id"] = user_id
        return []

    monkeypatch.setattr("backend.routers.exams.get_all_user_exams", fake_get_all)
    r = client.get("/exams/all_my_exams", headers=auth(token_a))
    assert r.status_code == 200
    assert seen["user_id"] == "user-A"


def test_exam_of_other_user_is_hidden(client, token_a, token_b, monkeypatch):
    monkeypatch.setattr("backend.routers.exams.get_exam",
                        lambda exam_id: {"_id": exam_id, "user_id": "user-A"})
    assert client.get("/exams/e1", headers=auth(token_b)).status_code == 404
    assert client.get("/exams/e1", headers=auth(token_a)).status_code == 200


def test_rubric_of_other_user_is_hidden(client, token_a, token_b, monkeypatch):
    monkeypatch.setattr("backend.routers.rubrics.get_rubric_by_id",
                        lambda rid: {"_id": rid, "creator": "a@test.com"})
    assert client.get("/rubrics/get/r1", headers=auth(token_b)).status_code == 404
    assert client.get("/rubrics/get/r1", headers=auth(token_a)).status_code == 200


def test_rubric_creator_is_set_server_side(client, token_a, monkeypatch):
    captured = {}

    def fake_create(rubric):
        captured.update(rubric)
        return "rid-1"

    monkeypatch.setattr("backend.routers.rubrics.create_rubric", fake_create)
    body = {"name": "R", "creator": "spoofed@evil.com",
            "questions": [{"text": "Q1", "criteria": [{"description": "c", "points": 1}]}]}
    r = client.post("/rubrics/create", json=body, headers=auth(token_a))
    assert r.status_code == 200
    assert captured["creator"] == "a@test.com"


def test_temp_exam_delete_requires_ownership(client, token_b, monkeypatch):
    monkeypatch.setattr("backend.routers.temp_exams.get_temp_exam",
                        lambda tid: {"_id": tid, "user_id": "user-A"})
    called = {"n": 0}
    monkeypatch.setattr("backend.routers.temp_exams.delete_temp_exam",
                        lambda tid: called.__setitem__("n", called["n"] + 1) or True)
    assert client.delete("/temp_exams/t1", headers=auth(token_b)).status_code == 404
    assert called["n"] == 0


def test_login_is_public_and_returns_token(client, monkeypatch):
    monkeypatch.setattr("backend.routers.users.validate_user",
                        lambda email, password: True)
    monkeypatch.setattr("backend.routers.users.get_user_by_email",
                        lambda email: {"_id": "user-A", "name": "Test",
                                       "email": "a@test.com", "role": "teacher"})
    r = client.post("/users/login", json={"email": "a@test.com", "password": "x"})
    assert r.status_code == 200
    token = r.json()["access_token"]
    import jwt as pyjwt
    payload = pyjwt.decode(token, auth_mod.JWT_SECRET, algorithms=[auth_mod.JWT_ALGORITHM])
    assert payload["sub"] == "user-A"
