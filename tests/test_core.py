from pathlib import Path

from countries.core import CountryData, load_country, merge_database


def test_CountryData():
    can = CountryData(
        alpha2_code="CA",
        alpha3_code="CAN",
        numeric_code="124",
        name="Canada",
    )

    assert can.lookup("name") == can.name == "Canada"


def test_merge_database():
    can = load_country("CAN")
    assert can.name == "Canada"

    assert can.lookup("flag") is None, "flag is not loaded yet"
    merge_database(Path(__file__).parent / "custom")
    assert can.lookup("flag") == "🇨🇦", "flag is loaded"
