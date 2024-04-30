from httpx import AsyncClient

from app.core.config import settings
from app.models.library import Library
from app.models.user import User
from tests.utils import get_jwt_header


class TestGetLibrarys:
    async def test_get_libraries_not_logged_in(self, client: AsyncClient):
        resp = await client.get(settings.API_PATH + "/libraries")
        assert resp.status_code == 401

    async def test_get_libraries(self, client: AsyncClient, create_user, create_library):
        user: User = await create_user()
        await create_library(user=user)
        jwt_header = get_jwt_header(user)
        resp = await client.get(settings.API_PATH + "/libraries", headers=jwt_header)
        assert resp.status_code == 200
        assert resp.headers["Content-Range"] == "0-1/1"
        assert len(resp.json()) == 1


class TestGetSingleLibrary:
    async def test_get_single_library(self, client: AsyncClient, create_user, create_library):
        user: User = await create_user()
        library: Library = await create_library(user=user)
        jwt_header = get_jwt_header(user)
        resp = await client.get(
            settings.API_PATH + f"/libraries/{library.id}", headers=jwt_header
        )
        assert resp.status_code == 200, resp.text
        data = resp.json()
        assert data["id"] == library.id
        assert data["value"] == library.value


class TestCreateLibrary:
    async def test_create_library(self, client: AsyncClient, create_user):
        user: User = await create_user()
        jwt_header = get_jwt_header(user)

        resp = await client.post(
            settings.API_PATH + "/libraries", headers=jwt_header, json={"value": "value"}
        )
        assert resp.status_code == 201, resp.text
        assert resp.json()["id"]


class TestDeleteLibrary:
    async def test_delete_library(self, client: AsyncClient, create_user, create_library):
        user: User = await create_user()
        library: Library = await create_library(user=user)
        jwt_header = get_jwt_header(user)

        resp = await client.delete(
            settings.API_PATH + f"/libraries/{library.id}", headers=jwt_header
        )
        assert resp.status_code == 200

    async def test_delete_library_does_not_exist(self, client: AsyncClient, create_user):
        user: User = await create_user()
        jwt_header = get_jwt_header(user)

        resp = await client.delete(
            settings.API_PATH + f"/libraries/{10**6}", headers=jwt_header
        )
        assert resp.status_code == 404, resp.text


class TestUpdateLibrary:
    async def test_update_library(self, client: AsyncClient, create_user, create_library):
        user: User = await create_user()
        library: Library = await create_library(user=user)
        jwt_header = get_jwt_header(user)

        resp = await client.put(
            settings.API_PATH + f"/libraries/{library.id}",
            headers=jwt_header,
            json={"value": "new value"},
        )
        assert resp.status_code == 200, resp.text
        assert resp.json()["value"] == "new value"
