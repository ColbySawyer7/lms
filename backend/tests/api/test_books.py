from httpx import AsyncClient

from app.core.config import settings
from app.models.book import Book
from app.models.user import User
from tests.utils import get_jwt_header


class TestGetBooks:
    async def test_get_books_not_logged_in(self, client: AsyncClient):
        resp = await client.get(settings.API_PATH + "/books")
        assert resp.status_code == 401

    async def test_get_books(self, client: AsyncClient, create_user, create_book):
        user: User = await create_user()
        await create_book(user=user)
        jwt_header = get_jwt_header(user)
        resp = await client.get(settings.API_PATH + "/books", headers=jwt_header)
        assert resp.status_code == 200
        assert resp.headers["Content-Range"] == "0-1/1"
        assert len(resp.json()) == 1


class TestGetSingleBook:
    async def test_get_single_book(self, client: AsyncClient, create_user, create_book):
        user: User = await create_user()
        book: Book = await create_book(user=user)
        jwt_header = get_jwt_header(user)
        resp = await client.get(
            settings.API_PATH + f"/books/{book.id}", headers=jwt_header
        )
        assert resp.status_code == 200, resp.text
        data = resp.json()
        assert data["id"] == book.id
        assert data["value"] == book.value


class TestCreateBook:
    async def test_create_book(self, client: AsyncClient, create_user):
        user: User = await create_user()
        jwt_header = get_jwt_header(user)

        resp = await client.post(
            settings.API_PATH + "/books", headers=jwt_header, json={"value": "value"}
        )
        assert resp.status_code == 201, resp.text
        assert resp.json()["id"]


class TestDeleteBook:
    async def test_delete_book(self, client: AsyncClient, create_user, create_book):
        user: User = await create_user()
        book: Book = await create_book(user=user)
        jwt_header = get_jwt_header(user)

        resp = await client.delete(
            settings.API_PATH + f"/books/{book.id}", headers=jwt_header
        )
        assert resp.status_code == 200

    async def test_delete_book_does_not_exist(self, client: AsyncClient, create_user):
        user: User = await create_user()
        jwt_header = get_jwt_header(user)

        resp = await client.delete(
            settings.API_PATH + f"/books/{10**6}", headers=jwt_header
        )
        assert resp.status_code == 404, resp.text


class TestUpdateBook:
    async def test_update_book(self, client: AsyncClient, create_user, create_book):
        user: User = await create_user()
        book: Book = await create_book(user=user)
        jwt_header = get_jwt_header(user)

        resp = await client.put(
            settings.API_PATH + f"/books/{book.id}",
            headers=jwt_header,
            json={"value": "new value"},
        )
        assert resp.status_code == 200, resp.text
        assert resp.json()["value"] == "new value"
