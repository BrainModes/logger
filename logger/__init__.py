import sys

from logger.logger_factory import LoggerFactory

if sys.version_info >= (3, 8):
    from importlib import metadata
else:
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)

__all__ = [
    'LoggerFactory',
]
