from typing import MutableSequence
from typing import Union

import pytest

from gzip_utils import CompressedJsonList
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
    assert comp.max_compressed_size == 400
    assert comp.compressed_size == 0
    assert comp.compression_ratio == 0.0
    assert comp.uncompressed_size == 0


def test_compress_str_list(comp: CompressedJsonList, str_list: MutableSequence[Union[str, dict]]):
    data = comp.get_compressed_json_array(str_list)

    assert comp.compressed_size == len(data)
    assert comp.compression_ratio > 0
    assert comp.uncompressed_size == 352
    assert comp.max_compressed_size == 400


def test_compress_all_str(comp: CompressedJsonList, str_list: MutableSequence[Union[str, dict]]):
    compress = list()
    while len(str_list) > 0:
        compressed = comp.get_compressed_json_array(str_list)
        compress.append(compressed)

    assert len(str_list) == 0


def test_compress_dict_list(comp: CompressedJsonList, dict_list: MutableSequence[Union[str, dict]]):
    data = comp.get_compressed_json_array(dict_list)

    assert comp.compressed_size == len(data)
    assert comp.compression_ratio > 0
    assert comp.uncompressed_size == 352
    assert comp.max_compressed_size == 400


def test_compress_all_dict(comp: CompressedJsonList, dict_list: MutableSequence[Union[str, dict]]):
    compress = list()
    while len(dict_list) > 0:
        compressed = comp.get_compressed_json_array(dict_list)
        compress.append(compressed)

    assert len(dict_list) == 0


def test_compress_mixed_list(comp: CompressedJsonList, mixed_list: MutableSequence[Union[str, dict]]):
    data = comp.get_compressed_json_array(mixed_list)

    assert comp.compressed_size == len(data)
    assert comp.compression_ratio > 0
    assert comp.uncompressed_size == 352
    assert comp.max_compressed_size == 400


def test_compress_all_mixed(comp: CompressedJsonList, mixed_list: MutableSequence[Union[str, dict]]):
    compress = list()
    while len(mixed_list) > 0:
        compressed = comp.get_compressed_json_array(mixed_list)
        compress.append(compressed)

    assert len(mixed_list) == 0


def test_raise_value_error(comp: CompressedJsonList):
    data = [3857, 37598]
    with pytest.raises(ValueError):
        comp.get_compressed_json_array(data)
