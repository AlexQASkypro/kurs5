import pytest  
from StringUtils import StringUtils  
  
# Инициализация объекта класса StringUtils  
string_utils = StringUtils()  
  
def test_capitilize():  
    assert string_utils.capitilize("skypro") == "Skypro"  
    assert string_utils.capitilize("123abc") == "123abc"  
    assert string_utils.capitilize("") == ""  
  
def test_trim():  
    assert string_utils.trim(" skypro") == "skypro"  
    assert string_utils.trim("   hello world  ") == "hello world  "  
    assert string_utils.trim("") == ""  
  
def test_to_list():  
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]  
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]  
    assert string_utils.to_list("") == []  
  
def test_contains():  
    assert string_utils.contains("SkyPro", "S") is True  
    assert string_utils.contains("SkyPro", "U") is False  
  
def test_delete_symbol():  
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"  
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"  
      
def test_starts_with():  
    assert string_utils.starts_with("SkyPro", "S") is True  
    assert string_utils.starts_with("SkyPro", "P") is False  
  
def test_end_with():  
    assert string_utils.end_with("SkyPro", "o") is True  
    assert string_utils.end_with("SkyPro", "y") is False  
  
def test_is_empty():  
    assert string_utils.is_empty("") is True  
    assert string_utils.is_empty(" ") is True  
    assert string_utils.is_empty("not empty") is False  
  
def test_list_to_string():  
    assert string_utils.list_to_string([1, 2, 3]) == "1, 2, 3"  
    assert string_utils.list_to_string(["a", "b"], "-") == "a-b" 