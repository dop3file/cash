import asyncio
import json

import pytest
from loguru import logger

from tests.conftest import Client


@pytest.mark.asyncio
async def test_get_and_set(client: Client):
    await client.execute_query("SET x 1")
    result = await client.execute_query("GET x")
    assert result == {"error": None, "result": 1, "message": None}


@pytest.mark.asyncio
async def test_keys(client: Client):
    result = await client.execute_query("KEYS")
    assert result == {"error": None, "result": ["x"], "message": None}


@pytest.mark.asyncio
async def test_delete(client: Client):
    await client.execute_query("DEL x")
    result = await client.execute_query("KEYS")
    assert result == {"error": None, "result": [], "message": None}


@pytest.mark.asyncio
async def test_dummy_delete(client: Client):
    result = await client.execute_query("DEL")
    assert result["error"] == "Not enough arguments(one or more)."


@pytest.mark.asyncio
async def test_flushall(client: Client):
    await client.execute_query("SET x 1")
    result = await client.execute_query("FLUSHALL")


@pytest.mark.asyncio
async def test_ping(client: Client):
    result = await client.execute_query("PING")
    assert result["message"] == "PONG"


@pytest.mark.asyncio
async def test_dummy_ping(client: Client):
    result = await client.execute_query("P1NG")
    assert result["error"] == "Invalid operator: P1NG"


@pytest.mark.asyncio
async def test_set_with_string(client: Client):
    await client.execute_query('SET x "TEST"')
    result = await client.execute_query("GET x")
    assert result["result"] == "TEST"


@pytest.mark.asyncio
async def test_dummy_set_with_string(client: Client):
    result = await client.execute_query('SET x TEST')
    assert result["error"] is not None