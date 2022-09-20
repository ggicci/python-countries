from countries.country import Country


def test_country():
    assert Country.CHN.name == "China"
    assert Country.CHN.name.to_locale("zh") == "中国"

    assert Country.CAN.name == "Canada"
    assert Country.CAN.name.to_locale("zh") == "加拿大"
    assert Country.CAN.name.to_locale("invalid-translation") is None
