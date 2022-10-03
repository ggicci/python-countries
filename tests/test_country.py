from countries import countries


def test_country():
    assert countries().CHN.name == "China"
    assert countries().CHN.name.to_locale("zh") == "中国"

    assert countries().CAN.name == "Canada"
    assert countries().CAN.name.to_locale("zh") == "加拿大"
    assert countries().CAN.name.to_locale("invalid-translation") == ""
