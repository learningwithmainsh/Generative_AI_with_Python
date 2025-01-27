
"""# Python Third-Party Module

[![PyPI version](https://badge.fury.io/py/module-name.svg)](https://pypi.org/project/module-name/) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview

**module-name** is a Python library designed to simplify [describe the purpose of the module]. It provides [list main features] and is compatible with Python 3.7+.

## Features

- Feature 1: [Brief description of feature 1]
- Feature 2: [Brief description of feature 2]
- Feature 3: [Brief description of feature 3]

## Installation

You can install the library via pip:

```bash
pip install module-name
```

## Usage

Here is a quick example of how to use **module-name**:

```python
from module_name import some_function

# Example usage
result = some_function(parameters)
print(result)
```

## Documentation

Detailed documentation is available [here](https://github.com/username/module-name/wiki) (replace with actual link).

## Requirements

- Python 3.7+
- [Other dependencies, if any]

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, feel free to [open an issue](https://github.com/username/module-name/issues).

## Acknowledgements

[Optional section to thank contributors or libraries used.]

---

⭐️ Star this repo if you find it useful!

"""

# request -HHTP libary for API Request

import requests

# Making a GET request to a public API
response = requests.get("https://github.com/")

# Checking if the request was successful
if response.status_code == 200:
    try:
        # Accessing the JSON content
        data = response.json()
        print("API DATA:", data)
    except ValueError:
        # If the response is not JSON
        print("The response is not in JSON format.")
else:
    print("Failed to retrieve data. Status code:", response.status_code)











