from app.helpers.get_fields import get_from_json_str


def test_get_fields_from_google():
    name, age, city = get_from_json_str('{"name": "John", "age": 30, "city": "New York"}', "name", "age", "city")
    assert name == "John"
    assert age == 30
    assert city == "New York"
                      