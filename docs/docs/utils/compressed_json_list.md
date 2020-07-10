# Compressed Json List

This is a utility class to compress down an list of `JSON` strings.

The constuctor needs one parameter that says the maximum size of a compressed part
of the list.

```Python
from gzip_utils import CompressedJsonList

list_of_json = [
  {"key": "value", "new-key": 546},
  {"key": "value", "new-key": 5423},
  {"key": "value", "new-key": 124},
  {"key": "value", "new-key": 3452},
  {"key": "value", "new-key": 373},
]

compressor = CompressedJsonList(200)

while len(list_of_json) > 0:
  compressed = compressor.get_compressed_json_list(list_of_json)
  do_something_with_compressed_data(compressed)
```
