#
#
#
try:
    from importlib.metadata import PackageNotFoundError, version
except ImportError:  # pragma: no cover
    from importlib_metadata import PackageNotFoundError, version  # type: ignore

try:
    __version__ = version(__package__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0"


from ._compressed_json_array import CompressedJsonArray

__all__ = ["CompressedJsonArray"]
