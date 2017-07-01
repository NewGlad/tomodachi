import uvloop
import asyncio
import pytest
from typing import Generator


@pytest.yield_fixture(scope='module')
def loop() -> Generator:
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    l = asyncio.new_event_loop()
    asyncio.set_event_loop(l)
    yield l
