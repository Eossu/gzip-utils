from typing import MutableSequence
from typing import Union

import pytest

from gzip_utils import CompressedJsonList
from gzip_utils import CompressionFull
from gzip_utils import SingleCompressionOnGoing
from gzip_utils import __version__


def test_version():
    """
    This should always be '0.0.0' since we are setting this
    when we build in Azure DevOps Pipelines.
    """
    assert __version__ == "0.0.0"


def test_creation_of_compression_output(comp: CompressedJsonList):
    """
    Testing basic object creation and its default values.
    """
    assert comp.compression_limit == 400
    assert comp.compressed_size == 0
    assert comp.compression_ratio == 0.0
    assert comp.uncompressed_size == 0


def test_change_max_compression_limit(comp: CompressedJsonList):
    comp.compression_limit = 300
    assert comp.compression_limit == 300


# ------------------------------------------------------------------------------------------------------------------------------
# Compress a list of strings og dicts
# ------------------------------------------------------------------------------------------------------------------------------


def test_compress_str_list(comp: CompressedJsonList, str_list: MutableSequence[Union[str, dict]]):
    data = comp.get_compressed_json_list(str_list)

    assert comp.compressed_size == len(data)
    assert comp.compression_ratio > 0
    assert comp.uncompressed_size == 352
    assert comp.compression_limit == 400


def test_compress_all_str(comp: CompressedJsonList, str_list: MutableSequence[Union[str, dict]]):
    compress = list()
    while len(str_list) > 0:
        compressed = comp.get_compressed_json_list(str_list)
        compress.append(compressed)

    assert len(str_list) == 0


def test_compress_dict_list(comp: CompressedJsonList, dict_list: MutableSequence[Union[str, dict]]):
    data = comp.get_compressed_json_list(dict_list)

    assert comp.compressed_size == len(data)
    assert comp.compression_ratio > 0
    assert comp.uncompressed_size == 352
    assert comp.compression_limit == 400


def test_compress_all_dict(comp: CompressedJsonList, dict_list: MutableSequence[Union[str, dict]]):
    compress = list()
    while len(dict_list) > 0:
        compressed = comp.get_compressed_json_list(dict_list)
        compress.append(compressed)

    assert len(dict_list) == 0


def test_compress_mixed_list(comp: CompressedJsonList, mixed_list: MutableSequence[Union[str, dict]]):
    data = comp.get_compressed_json_list(mixed_list)

    assert comp.compressed_size == len(data)
    assert comp.compression_ratio > 0
    assert comp.uncompressed_size == 352
    assert comp.compression_limit == 400


def test_compress_all_mixed(comp: CompressedJsonList, mixed_list: MutableSequence[Union[str, dict]]):
    compress = list()
    while len(mixed_list) > 0:
        compressed = comp.get_compressed_json_list(mixed_list)
        compress.append(compressed)

    assert len(mixed_list) == 0
    assert len(compress) > 0
    assert type(compress[0]) == bytes


def test_raise_value_error(comp: CompressedJsonList):
    data = [3857, 37598]
    with pytest.raises(ValueError):
        comp.get_compressed_json_list(data)  # type: ignore


# ------------------------------------------------------------------------------------------------------------------------------
# Compress a list of strings og dicts
# ------------------------------------------------------------------------------------------------------------------------------


def test_start_batch_compress(comp: CompressedJsonList):
    data_str = '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}'
    data_dict = {"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}

    comp.compress(data_str)
    comp.compress(data_dict)
    assert comp.uncompressed_size > 0

    comp_data = comp.get_data(True)
    assert type(comp_data) == bytes


def test_raises_compression_full(comp: CompressedJsonList):
    data = '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}'
    comp.compression_limit = 30

    with pytest.raises(CompressionFull):
        comp.compress(data)
        comp.compress(data)


def test_raises_cant_start_array_compress_with_batch_on_going(comp: CompressedJsonList):
    data = '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}'
    data_list: MutableSequence[Union[str, dict]] = [
        '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}',
        '{"variable": "test this", "data": "where to go next", "integer": 123453, "float": 34.78}',
    ]

    comp.compress(data)

    with pytest.raises(SingleCompressionOnGoing):
        comp.get_compressed_json_list(data_list)
