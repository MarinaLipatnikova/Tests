import pytest

from first import get_name, get_directory


@pytest.mark.parametrize(
    'doc_number, expected',
    (
        ["10006", "Аристарх Павлов"],
        ["101", "Документ не найден"]
    )
)
def test_get_name(doc_number, expected):
    result = get_name(doc_number)
    assert expected == result

@pytest.mark.parametrize(
    'doc_number, expected',
    (
        ["11-2", "1"],
        ["311 020204", "Полки с таким документом не найдено"],
    )
)
def test_get_directory(doc_number, expected):
    result = get_directory(doc_number)
    assert expected == result


