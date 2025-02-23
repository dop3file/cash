import asyncio
import json

import pytest
from loguru import logger

from tests.conftest import Client


@pytest.mark.asyncio
async def test_get_and_set(client: Client):
    await client.execute_query("SET x 1")
    result = await client.execute_query("GET x")
    assert result == {"error": None, "result": 1}


@pytest.mark.asyncio
async def test_keys(client: Client):
    result = await client.execute_query("KEYS")
    assert result == {"error": None, "result": ["x"]}


@pytest.mark.asyncio
async def test_delete(client: Client):
    await client.execute_query("DEL x")
    result = await client.execute_query("KEYS")
    assert result == {"error": None, "result": []}


@pytest.mark.asyncio
async def test_dummy_delete(client: Client):
    result = await client.execute_query("DEL")
    assert result["error"] == "Not enough arguments(one or more)."


@pytest.mark.asyncio
async def test_flushall(client: Client):
    await client.execute_query("SET x 1")
    result = await client.execute_query("FLUSHALL")