"""pytest-wide test isolation (Session 2.63).

Many modules open their log file at import time (logging.FileHandler on
logs/<name>.log). Tests that exercise their failure paths ("boom", "simulated
network failure") therefore wrote fake errors into the REAL logs, which are
committed and read as operational history. This redirects every FileHandler
that would write inside the repo's logs/ folder to a throwaway temp folder
for the whole pytest session. It patches logging.FileHandler before any test
module is imported, so it also covers handlers created later inside run().

Direct runs (`python test_x.py`) do not load this file; the tests that
matter there isolate themselves (see test_ingest_pickem.py).
"""

import atexit
import logging
import shutil
import tempfile
from pathlib import Path

_REAL_LOGS_DIR = (Path(__file__).resolve().parent / "logs").resolve()
_TEST_LOGS_DIR = Path(tempfile.mkdtemp(prefix="market_betting_test_logs_"))
atexit.register(shutil.rmtree, _TEST_LOGS_DIR, ignore_errors=True)

_RealFileHandler = logging.FileHandler


class _IsolatedFileHandler(_RealFileHandler):
    def __init__(self, filename, *args, **kwargs):
        path = Path(filename).resolve()
        if _REAL_LOGS_DIR in path.parents:
            filename = _TEST_LOGS_DIR / path.name
        super().__init__(filename, *args, **kwargs)


logging.FileHandler = _IsolatedFileHandler
