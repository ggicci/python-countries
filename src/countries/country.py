from dataclasses import dataclass, fields
from typing import Generic, Type, TypeVar

from countries.dataloader import DataLoader

from .core import (
    CountryData,
    CountryDataType,
    CustomCountryData,
    default_dataloader,
    load_country,
)

__countries: "FullCountryIndex"


def countries() -> "FullCountryIndex[CountryData]":
    """Get the index of all countries."""
    return __countries


@dataclass(frozen=True)
class FullCountryIndex(Generic[CountryDataType]):
    AFG: CountryDataType
    ALB: CountryDataType
    DZA: CountryDataType
    ASM: CountryDataType
    AND: CountryDataType
    AGO: CountryDataType
    AIA: CountryDataType
    ATA: CountryDataType
    ATG: CountryDataType
    ARG: CountryDataType
    ARM: CountryDataType
    ABW: CountryDataType
    AUS: CountryDataType
    AUT: CountryDataType
    AZE: CountryDataType
    BHS: CountryDataType
    BHR: CountryDataType
    BGD: CountryDataType
    BRB: CountryDataType
    BLR: CountryDataType
    BEL: CountryDataType
    BLZ: CountryDataType
    BEN: CountryDataType
    BMU: CountryDataType
    BTN: CountryDataType
    BOL: CountryDataType
    BES: CountryDataType
    BIH: CountryDataType
    BWA: CountryDataType
    BVT: CountryDataType
    BRA: CountryDataType
    IOT: CountryDataType
    BRN: CountryDataType
    BGR: CountryDataType
    BFA: CountryDataType
    BDI: CountryDataType
    CPV: CountryDataType
    KHM: CountryDataType
    CMR: CountryDataType
    CAN: CountryDataType
    CYM: CountryDataType
    CAF: CountryDataType
    TCD: CountryDataType
    CHL: CountryDataType
    CHN: CountryDataType
    CXR: CountryDataType
    CCK: CountryDataType
    COL: CountryDataType
    COM: CountryDataType
    COD: CountryDataType
    COG: CountryDataType
    COK: CountryDataType
    CRI: CountryDataType
    HRV: CountryDataType
    CUB: CountryDataType
    CUW: CountryDataType
    CYP: CountryDataType
    CZE: CountryDataType
    CIV: CountryDataType
    DNK: CountryDataType
    DJI: CountryDataType
    DMA: CountryDataType
    DOM: CountryDataType
    ECU: CountryDataType
    EGY: CountryDataType
    SLV: CountryDataType
    GNQ: CountryDataType
    ERI: CountryDataType
    EST: CountryDataType
    SWZ: CountryDataType
    ETH: CountryDataType
    FLK: CountryDataType
    FRO: CountryDataType
    FJI: CountryDataType
    FIN: CountryDataType
    FRA: CountryDataType
    GUF: CountryDataType
    PYF: CountryDataType
    ATF: CountryDataType
    GAB: CountryDataType
    GMB: CountryDataType
    GEO: CountryDataType
    DEU: CountryDataType
    GHA: CountryDataType
    GIB: CountryDataType
    GRC: CountryDataType
    GRL: CountryDataType
    GRD: CountryDataType
    GLP: CountryDataType
    GUM: CountryDataType
    GTM: CountryDataType
    GGY: CountryDataType
    GIN: CountryDataType
    GNB: CountryDataType
    GUY: CountryDataType
    HTI: CountryDataType
    HMD: CountryDataType
    VAT: CountryDataType
    HND: CountryDataType
    HKG: CountryDataType
    HUN: CountryDataType
    ISL: CountryDataType
    IND: CountryDataType
    IDN: CountryDataType
    IRN: CountryDataType
    IRQ: CountryDataType
    IRL: CountryDataType
    IMN: CountryDataType
    ISR: CountryDataType
    ITA: CountryDataType
    JAM: CountryDataType
    JPN: CountryDataType
    JEY: CountryDataType
    JOR: CountryDataType
    KAZ: CountryDataType
    KEN: CountryDataType
    KIR: CountryDataType
    PRK: CountryDataType
    KOR: CountryDataType
    KWT: CountryDataType
    KGZ: CountryDataType
    LAO: CountryDataType
    LVA: CountryDataType
    LBN: CountryDataType
    LSO: CountryDataType
    LBR: CountryDataType
    LBY: CountryDataType
    LIE: CountryDataType
    LTU: CountryDataType
    LUX: CountryDataType
    MAC: CountryDataType
    MDG: CountryDataType
    MWI: CountryDataType
    MYS: CountryDataType
    MDV: CountryDataType
    MLI: CountryDataType
    MLT: CountryDataType
    MHL: CountryDataType
    MTQ: CountryDataType
    MRT: CountryDataType
    MUS: CountryDataType
    MYT: CountryDataType
    MEX: CountryDataType
    FSM: CountryDataType
    MDA: CountryDataType
    MCO: CountryDataType
    MNG: CountryDataType
    MNE: CountryDataType
    MSR: CountryDataType
    MAR: CountryDataType
    MOZ: CountryDataType
    MMR: CountryDataType
    NAM: CountryDataType
    NRU: CountryDataType
    NPL: CountryDataType
    NLD: CountryDataType
    NCL: CountryDataType
    NZL: CountryDataType
    NIC: CountryDataType
    NER: CountryDataType
    NGA: CountryDataType
    NIU: CountryDataType
    NFK: CountryDataType
    MNP: CountryDataType
    NOR: CountryDataType
    OMN: CountryDataType
    PAK: CountryDataType
    PLW: CountryDataType
    PSE: CountryDataType
    PAN: CountryDataType
    PNG: CountryDataType
    PRY: CountryDataType
    PER: CountryDataType
    PHL: CountryDataType
    PCN: CountryDataType
    POL: CountryDataType
    PRT: CountryDataType
    PRI: CountryDataType
    QAT: CountryDataType
    MKD: CountryDataType
    ROU: CountryDataType
    RUS: CountryDataType
    RWA: CountryDataType
    REU: CountryDataType
    BLM: CountryDataType
    SHN: CountryDataType
    KNA: CountryDataType
    LCA: CountryDataType
    MAF: CountryDataType
    SPM: CountryDataType
    VCT: CountryDataType
    WSM: CountryDataType
    SMR: CountryDataType
    STP: CountryDataType
    SAU: CountryDataType
    SEN: CountryDataType
    SRB: CountryDataType
    SYC: CountryDataType
    SLE: CountryDataType
    SGP: CountryDataType
    SXM: CountryDataType
    SVK: CountryDataType
    SVN: CountryDataType
    SLB: CountryDataType
    SOM: CountryDataType
    ZAF: CountryDataType
    SGS: CountryDataType
    SSD: CountryDataType
    ESP: CountryDataType
    LKA: CountryDataType
    SDN: CountryDataType
    SUR: CountryDataType
    SJM: CountryDataType
    SWE: CountryDataType
    CHE: CountryDataType
    SYR: CountryDataType
    TWN: CountryDataType
    TJK: CountryDataType
    TZA: CountryDataType
    THA: CountryDataType
    TLS: CountryDataType
    TGO: CountryDataType
    TKL: CountryDataType
    TON: CountryDataType
    TTO: CountryDataType
    TUN: CountryDataType
    TUR: CountryDataType
    TKM: CountryDataType
    TCA: CountryDataType
    TUV: CountryDataType
    UGA: CountryDataType
    UKR: CountryDataType
    ARE: CountryDataType
    GBR: CountryDataType
    UMI: CountryDataType
    USA: CountryDataType
    URY: CountryDataType
    UZB: CountryDataType
    VUT: CountryDataType
    VEN: CountryDataType
    VNM: CountryDataType
    VGB: CountryDataType
    VIR: CountryDataType
    WLF: CountryDataType
    ESH: CountryDataType
    YEM: CountryDataType
    ZMB: CountryDataType
    ZWE: CountryDataType
    ALA: CountryDataType


CountryIndexType = TypeVar("CountryIndexType")


def load_countries(
    locale: str = "en",
    data_cls: Type[CountryIndexType] = FullCountryIndex[CountryData],
) -> CountryIndexType:
    kwargs = {}
    print(".....load countries, type(data_cls)=", type(data_cls))
    for fld in fields(data_cls):
        kwargs[fld.name] = load_country(fld.name, locale=locale)

    return data_cls(**kwargs)


@dataclass(frozen=True)
class MyIndex:
    USA: CustomCountryData
    CAN: CustomCountryData


# load_countries()


def __reload_countries():
    global __countries
    __countries = load_countries(data_cls=FullCountryIndex[CountryData])


__reload_countries()
default_dataloader.register_reload_callback(__reload_countries)
