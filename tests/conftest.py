import os
import tempfile
import pytest
from Notice_Board import create_app
from Notice_Board.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')
