from httpx import AsyncClient

from app.core.config import settings
from app.models.transaction import Transaction
from app.models.user import User
from tests.utils import get_jwt_header


class TestGetTransactions:
    async def test_get_transactions_not_logged_in(self, client: AsyncClient):
        resp = await client.get(settings.API_PATH + "/transactions")
        assert resp.status_code == 401

    async def test_get_transactions(self, client: AsyncClient, create_user, create_transaction):
        user: User = await create_user()
        await create_transaction(user=user)
        jwt_header = get_jwt_header(user)
        resp = await client.get(settings.API_PATH + "/transactions", headers=jwt_header)
        assert resp.status_code == 200
        assert resp.headers["Content-Range"] == "0-1/1"
        assert len(resp.json()) == 1


class TestGetSingleTransaction:
    async def test_get_single_transaction(self, client: AsyncClient, create_user, create_transaction):
        user: User = await create_user()
        transaction: Transaction = await create_transaction(user=user)
        jwt_header = get_jwt_header(user)
        resp = await client.get(
            settings.API_PATH + f"/transactions/{transaction.id}", headers=jwt_header
        )
        assert resp.status_code == 200, resp.text
        data = resp.json()
        assert data["id"] == transaction.id
        assert data["value"] == transaction.value


class TestCreateTransaction:
    async def test_create_transaction(self, client: AsyncClient, create_user):
        user: User = await create_user()
        jwt_header = get_jwt_header(user)

        resp = await client.post(
            settings.API_PATH + "/transactions", headers=jwt_header, json={"value": "value"}
        )
        assert resp.status_code == 201, resp.text
        assert resp.json()["id"]


class TestDeleteTransaction:
    async def test_delete_transaction(self, client: AsyncClient, create_user, create_transaction):
        user: User = await create_user()
        transaction: Transaction = await create_transaction(user=user)
        jwt_header = get_jwt_header(user)

        resp = await client.delete(
            settings.API_PATH + f"/transactions/{transaction.id}", headers=jwt_header
        )
        assert resp.status_code == 200

    async def test_delete_transaction_does_not_exist(self, client: AsyncClient, create_user):
        user: User = await create_user()
        jwt_header = get_jwt_header(user)

        resp = await client.delete(
            settings.API_PATH + f"/transactions/{10**6}", headers=jwt_header
        )
        assert resp.status_code == 404, resp.text


class TestUpdateTransaction:
    async def test_update_transaction(self, client: AsyncClient, create_user, create_transaction):
        user: User = await create_user()
        transaction: Transaction = await create_transaction(user=user)
        jwt_header = get_jwt_header(user)

        resp = await client.put(
            settings.API_PATH + f"/transactions/{transaction.id}",
            headers=jwt_header,
            json={"value": "new value"},
        )
        assert resp.status_code == 200, resp.text
        assert resp.json()["value"] == "new value"
