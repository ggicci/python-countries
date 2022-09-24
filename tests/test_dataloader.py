from pathlib import Path

from countries.dataloader import DataLoader


def test_DataLoader():
    dataloader = DataLoader()
    assert dataloader.lookup("CAN", "name") == "Canada"
    assert dataloader.lookup("CHN", "name", locale="zh") == "中国"

    assert dataloader.lookup("Invalid-Code", "name") is None
    assert dataloader.lookup("Invalid-Code", "name", locale="de") is None

    assert dataloader.lookup("USA", "UnknownField") is None
    assert dataloader.lookup("USA", "UnknownField", locale="fr") is None


def test_DataLoader_merge_database():
    dataloader = DataLoader()
    dataloader.merge_database(Path(__file__).parent / "custom")
    assert len(dataloader.databases) == 2

    assert dataloader.lookup("CAN", "flag") == "🇨🇦"
    assert dataloader.lookup("CHN", "flag") == "🇨🇳"
    assert dataloader.lookup("USA", "flag") == "🇺🇸"
    assert dataloader.lookup("GBR", "flag") is None
    assert dataloader.lookup("CAN", "flag", locale="de") is None

    assert (
        dataloader.lookup("USA", "name", locale="fr") == "États-Unis d'Amérique (les)"
    )
    assert dataloader.lookup("CHN", "name", locale="fr") == "Chine"

    assert dataloader.lookup("USA", "name") == "United States"
    assert dataloader.lookup("GBR", "name") == "United Kingdom"
    assert dataloader.lookup("CHN", "name") == "China"


def test_DataLoader_merge_database_OverrideLevel_FIELD():
    dataloader = DataLoader()
    dataloader.merge_database(
        Path(__file__).parent / "custom", override_level=DataLoader.OverrideLevel.FIELD
    )
    assert dataloader.lookup("USA", "name") == "United States"
    assert dataloader.lookup("GBR", "name") == "United Kingdom"
    assert dataloader.lookup("CHN", "name") is None


def test_DataLoader_merge_database_OverrideLevel_LOCALE():
    dataloader = DataLoader()
    dataloader.merge_database(
        Path(__file__).parent / "custom", override_level=DataLoader.OverrideLevel.LOCALE
    )
    assert dataloader.lookup("USA", "name") == "United States"
    assert dataloader.lookup("GBR", "name") == "United Kingdom"
    assert dataloader.lookup("CHN", "name") is None
