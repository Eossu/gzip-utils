import pytest

from json_utils import CompressedJsonArray


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

json_data_mixed = [
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
def str_list():
    return json_data_str


@pytest.fixture
def dict_list():
    return json_data_dict


@pytest.fixture
def mixed_list():
    return json_data_mixed


@pytest.fixture
def comp():
    return CompressedJsonArray(400)
