# iRacing API Client

A simple client for the iRacing API.

## Installation

The following sets up a virtual environment and installs dependencies with `pip`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

To run the example simple execute:
```
python3 example.py --config "./dev.config"
```

## Notes

The iRacing API provides a documentation end point. This has been included here in `documentation.json` for convenience. Note that the actual documentation may change at any point.

Configuration options are specified in a config file, passed in via the `--config` argument. An example is included in `dev.config`.
