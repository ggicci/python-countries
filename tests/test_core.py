from pathlib import Path

from countries.core import CountryData, load_country, merge_database
from countries.country import countries


def test_CountryData():
    can = CountryData(
        locale="en",
        alpha2_code="CA",
        alpha3_code="CAN",
        numeric_code="124",
        name="Canada",
    )

    assert can.lookup("name") == can.name == "Canada"


def test_CountryData_to_locale():
    can = load_country("CAN")
    assert can.name == "Canada"

    can_zh = can.to_locale("zh")
    assert can_zh.name == "加拿大"


def test_load_country():
    can = load_country("CAN")
    assert can.locale == "en"
    assert can.alpha2_code == "CA"
    assert can.alpha3_code == "CAN"
    assert can.numeric_code == "124"
    assert can.name == "Canada"

    can_zh = load_country("CAN", locale="zh")
    assert can_zh.locale == "zh"
    assert can.alpha2_code == "CA"
    assert can.alpha3_code == "CAN"
    assert can.numeric_code == "124"
    assert can_zh.name == "加拿大"


def test_merge_database():
    can = load_country("CAN")
    assert can.name == "Canada"

    assert can.lookup("flag") == "", "flag is not loaded yet"
    merge_database(Path(__file__).parent / "custom")
    assert can.lookup("flag") == "🇨🇦", "flag is loaded"


def test_merge_database_reload():
    assert countries().USA.name == "United States of America (the)"
    merge_database(Path(__file__).parent / "custom", reload=False)
    assert countries().USA.name == "United States of America (the)"
    merge_database(Path(__file__).parent / "custom", reload=True)
    assert countries().USA.name == "United States"
