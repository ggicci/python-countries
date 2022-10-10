import pytest
from countries.country import FullCountryIndex, load_countries, load_countries_generic
from countries.dataloader import DataLoader

from .helper import CUSTOM_DATA_DIR, TOTAL_COUNTRIES, CustomCountry, CustomCountryIndex


class InvalidCountryIndex:
    USA: CustomCountry


def test_load_countries():
    country_index = load_countries()

    assert country_index.CHN.locale == "en"
    assert country_index.CHN.name == "China"
    assert country_index.CHN.name.to_locale("zh") == "中国"

    assert country_index.CAN.locale == "en"
    assert country_index.CAN.name == "Canada"
    assert country_index.CAN.name.to_locale("zh") == "加拿大"
    assert country_index.CAN.name.to_locale("invalid-translation") == ""


def test_load_countries_with_locale():
    country_index = load_countries(locale="zh")

    assert country_index.CHN.locale == "zh"
    assert country_index.CHN.name == "中国"
    assert country_index.CHN.name.to_locale("en") == "China"

    assert country_index.CAN.locale == "zh"
    assert country_index.CAN.name == "加拿大"
    assert country_index.CAN.name.to_locale("en") == "Canada"


def test_load_countries_generic_with_custom_index_cls():
    country_index = load_countries_generic(CustomCountryIndex)
    assert hasattr(country_index, "CHN") is False, "CHN should be missing"
    assert country_index.USA.flag == ""


def test_load_countries_generic_with_generic_index_cls():
    country_index = load_countries_generic(
        FullCountryIndex[CustomCountry], loader=DataLoader(CUSTOM_DATA_DIR)
    )
    assert len(country_index.asdict()) == TOTAL_COUNTRIES
    assert country_index.CHN.flag == "🇨🇳"
    assert country_index.USA.national_flower == "Rose"


def test_load_countries_generic_with_invalid_type():
    with pytest.raises(ValueError, match=r".+must be a dataclass"):
        v = load_countries_generic(InvalidCountryIndex)
        assert v is None
