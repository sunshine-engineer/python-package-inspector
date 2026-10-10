# requests 2.32.3

## Inspection environment

```text
Python: D:\projects\GCP_Deployments\package_discovery\reviewed_examples\.venvs\requests-2.32.3-81ut82qk\Scripts\python.exe
Environment: D:\projects\GCP_Deployments\package_discovery\reviewed_examples\.venvs\requests-2.32.3-81ut82qk
```

Cleanup was requested for the temporary environment after generation. The paths above record the inspection environment; recreate the package environment before running manual queries if cleanup succeeds.

## Scope and limitations

This documents the installed distribution in this Python environment. Source inspection does not execute package code. Runtime mode executes imports and is not a security sandbox. Signatures and docstrings are evidence, not generated usage examples. Return behavior is only known when annotations or documentation describe it. Dynamic APIs, unavailable source, editable installs, and missing optional dependencies can leave gaps. Private names are included.

## Installation metadata

````json
{
  "Metadata-Version": [
    "2.1"
  ],
  "Name": [
    "requests"
  ],
  "Version": [
    "2.32.3"
  ],
  "Summary": [
    "Python HTTP for Humans."
  ],
  "Home-page": [
    "https://requests.readthedocs.io"
  ],
  "Author": [
    "Kenneth Reitz"
  ],
  "Author-email": [
    "me@kennethreitz.org"
  ],
  "License": [
    "Apache-2.0"
  ],
  "Project-URL": [
    "Documentation, https://requests.readthedocs.io",
    "Source, https://github.com/psf/requests"
  ],
  "Classifier": [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Software Development :: Libraries"
  ],
  "Requires-Python": [
    ">=3.8"
  ],
  "Description-Content-Type": [
    "text/markdown"
  ],
  "License-File": [
    "LICENSE"
  ],
  "Requires-Dist": [
    "charset-normalizer <4,>=2",
    "idna <4,>=2.5",
    "urllib3 <3,>=1.21.1",
    "certifi >=2017.4.17",
    "PySocks !=1.5.7,>=1.5.6 ; extra == 'socks'",
    "chardet <6,>=3.0.2 ; extra == 'use_chardet_on_py3'"
  ],
  "Provides-Extra": [
    "security",
    "socks",
    "use_chardet_on_py3"
  ],
  "Description": [
    "# Requests\n\n**Requests** is a simple, yet elegant, HTTP library.\n\n```python\n>>> import requests\n>>> r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))\n>>> r.status_code\n200\n>>> r.headers['content-type']\n'application/json; charset=utf8'\n>>> r.encoding\n'utf-8'\n>>> r.text\n'{\"authenticated\": true, ...'\n>>> r.json()\n{'authenticated': True, ...}\n```\n\nRequests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your `PUT` & `POST` data — but nowadays, just use the `json` method!\n\nRequests is one of the most downloaded Python packages today, pulling in around `30M downloads / week`— according to GitHub, Requests is currently [depended upon](https://github.com/psf/requests/network/dependents?package_id=UGFja2FnZS01NzA4OTExNg%3D%3D) by `1,000,000+` repositories. You may certainly put your trust in this code.\n\n[![Downloads](https://static.pepy.tech/badge/requests/month)](https://pepy.tech/project/requests)\n[![Supported Versions](https://img.shields.io/pypi/pyversions/requests.svg)](https://pypi.org/project/requests)\n[![Contributors](https://img.shields.io/github/contributors/psf/requests.svg)](https://github.com/psf/requests/graphs/contributors)\n\n## Installing Requests and Supported Versions\n\nRequests is available on PyPI:\n\n```console\n$ python -m pip install requests\n```\n\nRequests officially supports Python 3.8+.\n\n## Supported Features & Best–Practices\n\nRequests is ready for the demands of building robust and reliable HTTP–speaking applications, for the needs of today.\n\n- Keep-Alive & Connection Pooling\n- International Domains and URLs\n- Sessions with Cookie Persistence\n- Browser-style TLS/SSL Verification\n- Basic & Digest Authentication\n- Familiar `dict`–like Cookies\n- Automatic Content Decompression and Decoding\n- Multi-part File Uploads\n- SOCKS Proxy Support\n- Connection Timeouts\n- Streaming Downloads\n- Automatic honoring of `.netrc`\n- Chunked HTTP Requests\n\n## API Reference and User Guide available on [Read the Docs](https://requests.readthedocs.io)\n\n[![Read the Docs](https://raw.githubusercontent.com/psf/requests/main/ext/ss.png)](https://requests.readthedocs.io)\n\n## Cloning the repository\n\nWhen cloning the Requests repository, you may need to add the `-c\nfetch.fsck.badTimezone=ignore` flag to avoid an error about a bad commit (see\n[this issue](https://github.com/psf/requests/issues/2690) for more background):\n\n```shell\ngit clone -c fetch.fsck.badTimezone=ignore https://github.com/psf/requests.git\n```\n\nYou can also apply this setting to your global Git config:\n\n```shell\ngit config --global fetch.fsck.badTimezone ignore\n```\n\n---\n\n[![Kenneth Reitz](https://raw.githubusercontent.com/psf/requests/main/ext/kr.png)](https://kennethreitz.org) [![Python Software Foundation](https://raw.githubusercontent.com/psf/requests/main/ext/psf.png)](https://www.python.org/psf)\n"
  ]
}
````

## Dependencies

```text
charset-normalizer <4,>=2
idna <4,>=2.5
urllib3 <3,>=1.21.1
certifi >=2017.4.17
PySocks !=1.5.7,>=1.5.6 ; extra == 'socks'
chardet <6,>=3.0.2 ; extra == 'use_chardet_on_py3'
```

## Entry points

```json
[]
```

## Module pages

- [Raw metadata-INSTALLER](bundled/metadata-INSTALLER.md)

- [Raw metadata-METADATA](bundled/metadata-METADATA.md)

- [Raw metadata-RECORD](bundled/metadata-RECORD.md)

- [Raw metadata-REQUESTED](bundled/metadata-REQUESTED.md)

- [Raw metadata-top_level.txt](bundled/metadata-top_level.txt.md)

- [Raw metadata-WHEEL](bundled/metadata-WHEEL.md)

- [Bundled text: requests-2.32.3.dist-info/LICENSE](bundled/00001.md)

- [Bundled text: requests-2.32.3.dist-info/top_level.txt](bundled/00006.md)

- [requests (.py)](modules/00007-requests.md)

- [requests.__version__ (.py)](modules/00026-requests.__version__.md)

- [requests._internal_utils (.py)](modules/00027-requests._internal_utils.md)

- [requests.adapters (.py)](modules/00028-requests.adapters.md)

- [requests.api (.py)](modules/00029-requests.api.md)

- [requests.auth (.py)](modules/00030-requests.auth.md)

- [requests.certs (.py)](modules/00031-requests.certs.md)

- [requests.compat (.py)](modules/00032-requests.compat.md)

- [requests.cookies (.py)](modules/00033-requests.cookies.md)

- [requests.exceptions (.py)](modules/00034-requests.exceptions.md)

- [requests.help (.py)](modules/00035-requests.help.md)

- [requests.hooks (.py)](modules/00036-requests.hooks.md)

- [requests.models (.py)](modules/00037-requests.models.md)

- [requests.packages (.py)](modules/00038-requests.packages.md)

- [requests.sessions (.py)](modules/00039-requests.sessions.md)

- [requests.status_codes (.py)](modules/00040-requests.status_codes.md)

- [requests.structures (.py)](modules/00041-requests.structures.md)

- [requests.utils (.py)](modules/00042-requests.utils.md)

- [Runtime: requests](modules/runtime-00000.md)

- [Runtime: requests.__version__](modules/runtime-00001.md)

- [Runtime: requests._internal_utils](modules/runtime-00002.md)

- [Runtime: requests.adapters](modules/runtime-00003.md)

- [Runtime: requests.api](modules/runtime-00004.md)

- [Runtime: requests.auth](modules/runtime-00005.md)

- [Runtime: requests.certs](modules/runtime-00006.md)

- [Runtime: requests.compat](modules/runtime-00007.md)

- [Runtime: requests.cookies](modules/runtime-00008.md)

- [Runtime: requests.exceptions](modules/runtime-00009.md)

- [Runtime: requests.help](modules/runtime-00010.md)

- [Runtime: requests.hooks](modules/runtime-00011.md)

- [Runtime: requests.models](modules/runtime-00012.md)

- [Runtime: requests.packages](modules/runtime-00013.md)

- [Runtime: requests.sessions](modules/runtime-00014.md)

- [Runtime: requests.status_codes](modules/runtime-00015.md)

- [Runtime: requests.structures](modules/runtime-00016.md)

- [Runtime: requests.utils](modules/runtime-00017.md)

## Installed files

```json
[
  {
    "path": "requests-2.32.3.dist-info/INSTALLER",
    "size": 4,
    "hash": "<FileHash mode: sha256 value: zuuue4knoyJ-UwPPXg8fezS7VCrXJQrAP7zeNuwvFQg>"
  },
  {
    "path": "requests-2.32.3.dist-info/LICENSE",
    "size": 10142,
    "hash": "<FileHash mode: sha256 value: CeipvOyAZxBGUsFoaFqwkx54aPnIKEtm9a5u2uXxEws>"
  },
  {
    "path": "requests-2.32.3.dist-info/METADATA",
    "size": 4610,
    "hash": "<FileHash mode: sha256 value: ZY7oRUweLnb7jCEnEW9hFWs7IpQbNVnAA4ncpwA4WBo>"
  },
  {
    "path": "requests-2.32.3.dist-info/RECORD",
    "size": null,
    "hash": null
  },
  {
    "path": "requests-2.32.3.dist-info/REQUESTED",
    "size": 0,
    "hash": "<FileHash mode: sha256 value: 47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU>"
  },
  {
    "path": "requests-2.32.3.dist-info/WHEEL",
    "size": 92,
    "hash": "<FileHash mode: sha256 value: GJ7t_kWBFywbagK5eo9IoUwLW6oyOeTKmQ-9iHFVNxQ>"
  },
  {
    "path": "requests-2.32.3.dist-info/top_level.txt",
    "size": 9,
    "hash": "<FileHash mode: sha256 value: fMSVmHfb5rbGOo6xv-O_tUX6j-WyixssE-SnwcDRxNQ>"
  },
  {
    "path": "requests/__init__.py",
    "size": 5072,
    "hash": "<FileHash mode: sha256 value: 4xaAERmPDIBPsa2PsjpU9r06yooK-2mZKHTZAhWRWts>"
  },
  {
    "path": "requests/__pycache__/__init__.cpython-314.pyc",
    "size": null,
    "hash": null
  },
  {
    "path": "requests/__pycache__/__version__.cpython-314.pyc",
    "size": null,
    "hash": null
  },
  {
    "path": "requests/__pycache__/_internal_utils.cpython-314.pyc",
    "size": null,
    "hash": null
  },
  {
    "path": "requests/__pycache__/adapters.cpython-314.pyc",
    "size": null,
    "hash": null
  },
  {
    "path": "requests/__pycache__/api.cpython-314.pyc",
    "size": null,
    "hash": null
  },
  {
    "path": "requests/__pycache__/auth.cpython-314.pyc",
    "size": null,
    "hash": null
  },
  {
    "path": "requests/__pycache__/certs.cpython-314.pyc",
    "size": null,
    "hash": null
  },
  {
    "path": "requests/__pycache__/compat.cpython-314.pyc",
    "size": null,
    "hash": null
  },
  {
    "path": "requests/__pycache__/cookies.cpython-314.pyc",
    "size": null,
    "hash": null
  },
  {
    "path": "requests/__pycache__/exceptions.cpython-314.pyc",
    "size": null,
    "hash": null
  },
  {
    "path": "requests/__pycache__/help.cpython-314.pyc",
    "size": null,
    "hash": null
  },
  {
    "path": "requests/__pycache__/hooks.cpython-314.pyc",
    "size": null,
    "hash": null
  },
  {
    "path": "requests/__pycache__/models.cpython-314.pyc",
    "size": null,
    "hash": null
  },
  {
    "path": "requests/__pycache__/packages.cpython-314.pyc",
    "size": null,
    "hash": null
  },
  {
    "path": "requests/__pycache__/sessions.cpython-314.pyc",
    "size": null,
    "hash": null
  },
  {
    "path": "requests/__pycache__/status_codes.cpython-314.pyc",
    "size": null,
    "hash": null
  },
  {
    "path": "requests/__pycache__/structures.cpython-314.pyc",
    "size": null,
    "hash": null
  },
  {
    "path": "requests/__pycache__/utils.cpython-314.pyc",
    "size": null,
    "hash": null
  },
  {
    "path": "requests/__version__.py",
    "size": 435,
    "hash": "<FileHash mode: sha256 value: FVfglgZmNQnmYPXpOohDU58F5EUb_-VnSTaAesS187g>"
  },
  {
    "path": "requests/_internal_utils.py",
    "size": 1495,
    "hash": "<FileHash mode: sha256 value: nMQymr4hs32TqVo5AbCrmcJEhvPUh7xXlluyqwslLiQ>"
  },
  {
    "path": "requests/adapters.py",
    "size": 27451,
    "hash": "<FileHash mode: sha256 value: KIcecscqam6reOCXRl4DwP4jX8Jcl8sd57ft17KR2cQ>"
  },
  {
    "path": "requests/api.py",
    "size": 6449,
    "hash": "<FileHash mode: sha256 value: _Zb9Oa7tzVIizTKwFrPjDEY9ejtm_OnSRERnADxGsQs>"
  },
  {
    "path": "requests/auth.py",
    "size": 10186,
    "hash": "<FileHash mode: sha256 value: kF75tqnLctZ9Mf_hm9TZIj4cQWnN5uxRz8oWsx5wmR0>"
  },
  {
    "path": "requests/certs.py",
    "size": 429,
    "hash": "<FileHash mode: sha256 value: Z9Sb410Anv6jUFTyss0jFFhU6xst8ctELqfy8Ev23gw>"
  },
  {
    "path": "requests/compat.py",
    "size": 1817,
    "hash": "<FileHash mode: sha256 value: C5w_DPLSurXPgcdWU78fora0APmbYkX2G89QvH5xzPA>"
  },
  {
    "path": "requests/cookies.py",
    "size": 18590,
    "hash": "<FileHash mode: sha256 value: bNi-iqEj4NPZ00-ob-rHvzkvObzN3lEpgw3g6paS3Xw>"
  },
  {
    "path": "requests/exceptions.py",
    "size": 4260,
    "hash": "<FileHash mode: sha256 value: jJPS1UWATs86ShVUaLorTiJb1SaGuoNEWgICJep-VkY>"
  },
  {
    "path": "requests/help.py",
    "size": 3875,
    "hash": "<FileHash mode: sha256 value: gPX5d_H7Xd88aDABejhqGgl9B1VFRTt5BmiYvL3PzIQ>"
  },
  {
    "path": "requests/hooks.py",
    "size": 733,
    "hash": "<FileHash mode: sha256 value: CiuysiHA39V5UfcCBXFIx83IrDpuwfN9RcTUgv28ftQ>"
  },
  {
    "path": "requests/models.py",
    "size": 35418,
    "hash": "<FileHash mode: sha256 value: k42roXzC8u_OagAPQi9U4MkfO7i4r2FdaqvMqstPehc>"
  },
  {
    "path": "requests/packages.py",
    "size": 904,
    "hash": "<FileHash mode: sha256 value: _g0gZ681UyAlKHRjH6kanbaoxx2eAb6qzcXiODyTIoc>"
  },
  {
    "path": "requests/sessions.py",
    "size": 30495,
    "hash": "<FileHash mode: sha256 value: ykTI8UWGSltOfH07HKollH7kTBGw4WhiBVaQGmckTw4>"
  },
  {
    "path": "requests/status_codes.py",
    "size": 4322,
    "hash": "<FileHash mode: sha256 value: iJUAeA25baTdw-6PfD0eF4qhpINDJRJI-yaMqxs4LEI>"
  },
  {
    "path": "requests/structures.py",
    "size": 2912,
    "hash": "<FileHash mode: sha256 value: -IbmhVz06S-5aPSZuUthZ6-6D9XOjRuTXHOabY041XM>"
  },
  {
    "path": "requests/utils.py",
    "size": 33619,
    "hash": "<FileHash mode: sha256 value: HiQC6Nq_Da3ktaMiFzQkh-dCk3iQHHKEsYS5kDc-8Cw>"
  }
]
```

## Manual distribution queries

```python
from importlib import metadata
d = metadata.distribution('requests')
d.version
list(d.metadata.items())
d.requires
list(d.entry_points)
list(d.files or [])
d.read_text('METADATA')
d.read_text('entry_points.txt')
```

## Inspection gaps and errors

```text
No inspection errors recorded. This does not prove complete API coverage.
```

## Python reference

- https://docs.python.org/3/library/importlib.metadata.html
- https://docs.python.org/3/library/inspect.html
- https://docs.python.org/3/library/ast.html
- https://docs.python.org/3/library/functions.html#help
