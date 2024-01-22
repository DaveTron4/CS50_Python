import pytest
import project

@pytest.fixture
def mock_input(monkeypatch):
    def mock_func():
        return "15"
    monkeypatch.setattr('builtins.input', mock_func)

def test_set_alarm():
    with pytest.raises(SystemExit):
        project.set_alarm("2023/12/12", "11:00 AM", "sound.mp3", "test")
    with pytest.raises(SystemExit):
        project.set_alarm("2023-12-12", "11:00AM", "sound.mp3", "test")
    with pytest.raises(SystemExit):
        project.set_alarm("2023-12-12", "11:00 AM", "sound_file_not_found.mp3", "test")

def test_convert():
    assert project.convert("11:00 AM") == "11:00"
    assert project.convert("12:00 AM") == "00:00"
    assert project.convert("11:00 PM") == "23:00"
    assert project.convert("12:00 PM") == "12:00"

def test_questions(mock_input):
    result = project.questions()
    assert result in [True, False], "questions() did not return True or False"

def test_is_number_string():
    assert project.is_number_string("123") == True
    assert project.is_number_string("-123") == True
    assert project.is_number_string("+123") == False
    assert project.is_number_string("abc") == False
    assert project.is_number_string("") == False
    assert project.is_number_string("12a") == False




