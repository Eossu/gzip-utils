from typing import MutableSequence
from typing import Union

import pytest

from gzip_utils import CompressedJsonList


json_data_str = [
    '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}',
    '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}',
    '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}',
    '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}',
    '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}',
    '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}',
    '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}',
    '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}',
    '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}',
]

json_data_dict = [
    {"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78},
    {"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78},
    {"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78},
    {"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78},
    {"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78},
    {"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78},
    {"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78},
    {"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78},
    {"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78},
]

json_data_mixed: MutableSequence[Union[str, dict]] = [
    '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}',
    {"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78},
    '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}',
    '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}',
    {"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78},
    '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}',
    '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}',
    '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}',
    '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}',
]


@pytest.fixture
def str_list() -> MutableSequence[str]:
    return json_data_str.copy()


@pytest.fixture
def dict_list() -> MutableSequence[dict]:
    return json_data_dict.copy()


@pytest.fixture
def mixed_list() -> MutableSequence[Union[str, dict]]:
    return json_data_mixed


@pytest.fixture
def comp() -> CompressedJsonList:
    return CompressedJsonList(400)
