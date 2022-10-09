from dataclasses import dataclass

from countries.core import CountryProperties, Property
from countries.country import CountryProperties, load_countries


@dataclass(frozen=True)
class CustomCountryData(CountryProperties):
    age: Property


@dataclass(frozen=True)
class MyIndex:
    USA: CustomCountryData
    CAN: CustomCountryData


def test_load_countries():
    ct = load_countries()

    # assert countries().CHN.name == "China"
    # assert countries().CHN.name.to_locale("zh") == "中国"

    # assert countries().CAN.name == "Canada"
    # assert countries().CAN.name.to_locale("zh") == "加拿大"
    # assert countries().CAN.name.to_locale("invalid-translation") == ""
