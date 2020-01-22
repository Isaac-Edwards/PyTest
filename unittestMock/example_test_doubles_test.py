from line_reader import read_from_file
from unittest.mock import MagicMock
import pytest

@pytest.fixture()
def mock_open(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="test line")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    return mock_open

def test_returns_correct_string(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value= True)
    monkeypatch.setattr("os.path.exists", mock_exists)
    result = read_from_file("blah")
    mock_open.assert_called_once_with("blah", "r")
    assert result == "test line"

def test_throws_exception_if_file_does_not_exist(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exists)
    with pytest.raises(Exception):
        result = read_from_file("blah")