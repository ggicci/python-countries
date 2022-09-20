from countries.dataloader import DataLoader, Property


def test_dataloader():
    dataloader = DataLoader()
    assert dataloader.lookup(Property("CAN", "name")) == "Canada"
    assert dataloader.lookup(Property("CHN", "name"), locale="zh") == "中国"

    assert dataloader.lookup(Property("Invalid-Code", "name")) is None
    assert dataloader.lookup(Property("Invalid-Code", "name"), locale="de") is None

    assert dataloader.lookup(Property("USA", "UnknownField")) is None
    assert dataloader.lookup(Property("USA", "UnknownField"), locale="fr") is None
