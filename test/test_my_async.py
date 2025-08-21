import pytest
import asyncio
from python.my_async import fetch_data

@pytest.mark.asyncio
async def test_fetch_data():
    result = await fetch_data()
    assert isinstance(result, dict)
    assert result["data"] == 123
