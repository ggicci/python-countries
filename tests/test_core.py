import pytest
from countries.core import Property, load_country, load_country_generic
from countries.dataloader import DataLoader

from .helper import CUSTOM_DATA_DIR, CustomCountry


class InvalidCountryProperties:
    color: Property


def test_load_country():
    can = load_country("CAN")
    assert can.locale == "en"
    assert can.alpha2_code == "CA"
    assert can.alpha3_code == "CAN"
    assert can.numeric_code == "124"
    assert can.name == "Canada"


def test_load_country_by_using_alpha2_code():
    can = load_country("CA")
    assert can.locale == "en"
    assert can.alpha2_code == "CA"
    assert can.alpha3_code == "CAN"
    assert can.numeric_code == "124"
    assert can.name == "Canada"


def test_load_country_with_locale():
    can_zh = load_country("CAN", locale="zh")
    assert can_zh.locale == "zh"
    assert can_zh.alpha2_code == "CA"
    assert can_zh.alpha3_code == "CAN"
    assert can_zh.numeric_code == "124"
    assert can_zh.name == "加拿大"


def test_country_to_locale():
    can = load_country("CAN")
    assert can.locale == "en"
    assert can.name == "Canada"

    can_zh = can.to_locale("zh")
    assert can_zh.locale == "zh"
    assert can_zh.name == "加拿大"


def test_load_country_generic():
    loader = DataLoader()
    loader.merge_database(CUSTOM_DATA_DIR)
    v = load_country_generic(CustomCountry, "US", loader=loader)
    assert v.flag == "🇺🇸"


def test_load_country_generic_with_invalid_type():
    with pytest.raises(ValueError, match=r".+must be a frozen dataclass") as ex:
        load_country_generic(InvalidCountryProperties, "US")


def test_load_country_with_unknown_country_code():
    with pytest.raises(KeyError, match=r".+not found"):
        load_country("ZZZ")
