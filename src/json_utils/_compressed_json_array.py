#
#
#
import json
import logging
from io import BytesIO
from typing import List, Union
from gzip import GzipFile

logger = logging.getLogger(__name__)


class CompressedJsonArray:
    """
    Compresses a `list` of json strings or dictionaries to an gziped compressed json array of json
    objects.

    Arguments:
        max_compressed_size [int]: This is the max compression size needed for one batch.
    """

    def __init__(self, max_compressed_size: int) -> None:
        self._max_compressed_size = max_compressed_size
        self._uncompressed_size: int = 0
        self._compressed_size: int = 0

    @property
    def uncompressed_size(self) -> int:
        return self._uncompressed_size

    @property
    def compressed_size(self) -> int:
        return self._compressed_size

    @property
    def compression_ratio(self) -> float:
        return self.compressed_size / self.uncompressed_size * 100.0

    def get_compressed_json_array(self, json_data: List[Union[str, dict]]) -> bytes:
        """Get a compressed array of json objects

        Args:
            data (Union[List[str], List[dict]]): List of json string or python dictonaries to compress

        Returns:
            bytearray: The array of compressed bytes
        """
        compressed = None
        unzipped_chars = 1
        gzip_metadata_size = 20

        try:
            byte_stream = BytesIO()
            gzip_stream = GzipFile(mode="wb", fileobj=byte_stream)

            gzip_stream.write(b'[')
            data_written = 0

            for data in json_data:
                if isinstance(data, dict):
                    data = json.dumps(data)

                bytes = data.encode("utf-8")

                if (gzip_stream.size + len(bytes) + unzipped_chars + gzip_metadata_size) > self._max_compressed_size:  # type: ignore
                    gzip_stream.flush()
                    unzipped_chars = 0

                if (gzip_stream.size + len(bytes) + gzip_metadata_size) >= self._max_compressed_size and data_written > 0:  # type: ignore
                    break

                json_data.remove(data)
                if data_written > 0:
                    gzip_stream.write(b',')
                gzip_stream.write(bytes)

                unzipped_chars += len(bytes)
                self._uncompressed_size += len(bytes)

            gzip_stream.write(b']')
            gzip_stream.close()
            compressed = byte_stream.getvalue()
            self._compressed_size = len(byte_stream.getvalue())

            return compressed

        except Exception as e:
            logger.exception("Got an exception", exc_info=e)
            raise e
