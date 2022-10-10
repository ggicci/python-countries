from dataclasses import asdict, dataclass, fields, is_dataclass
from typing import Dict, Generic, Type, TypeVar

from .core import (
    CountryProperties,
    T_CountryProperties,
    default_dataloader,
    load_country_generic,
)
from .dataloader import DataLoader


@dataclass(frozen=True)
class FullCountryIndex(Generic[T_CountryProperties]):
    AFG: T_CountryProperties
    ALB: T_CountryProperties
    DZA: T_CountryProperties
    ASM: T_CountryProperties
    AND: T_CountryProperties
    AGO: T_CountryProperties
    AIA: T_CountryProperties
    ATA: T_CountryProperties
    ATG: T_CountryProperties
    ARG: T_CountryProperties
    ARM: T_CountryProperties
    ABW: T_CountryProperties
    AUS: T_CountryProperties
    AUT: T_CountryProperties
    AZE: T_CountryProperties
    BHS: T_CountryProperties
    BHR: T_CountryProperties
    BGD: T_CountryProperties
    BRB: T_CountryProperties
    BLR: T_CountryProperties
    BEL: T_CountryProperties
    BLZ: T_CountryProperties
    BEN: T_CountryProperties
    BMU: T_CountryProperties
    BTN: T_CountryProperties
    BOL: T_CountryProperties
    BES: T_CountryProperties
    BIH: T_CountryProperties
    BWA: T_CountryProperties
    BVT: T_CountryProperties
    BRA: T_CountryProperties
    IOT: T_CountryProperties
    BRN: T_CountryProperties
    BGR: T_CountryProperties
    BFA: T_CountryProperties
    BDI: T_CountryProperties
    CPV: T_CountryProperties
    KHM: T_CountryProperties
    CMR: T_CountryProperties
    CAN: T_CountryProperties
    CYM: T_CountryProperties
    CAF: T_CountryProperties
    TCD: T_CountryProperties
    CHL: T_CountryProperties
    CHN: T_CountryProperties
    CXR: T_CountryProperties
    CCK: T_CountryProperties
    COL: T_CountryProperties
    COM: T_CountryProperties
    COD: T_CountryProperties
    COG: T_CountryProperties
    COK: T_CountryProperties
    CRI: T_CountryProperties
    HRV: T_CountryProperties
    CUB: T_CountryProperties
    CUW: T_CountryProperties
    CYP: T_CountryProperties
    CZE: T_CountryProperties
    CIV: T_CountryProperties
    DNK: T_CountryProperties
    DJI: T_CountryProperties
    DMA: T_CountryProperties
    DOM: T_CountryProperties
    ECU: T_CountryProperties
    EGY: T_CountryProperties
    SLV: T_CountryProperties
    GNQ: T_CountryProperties
    ERI: T_CountryProperties
    EST: T_CountryProperties
    SWZ: T_CountryProperties
    ETH: T_CountryProperties
    FLK: T_CountryProperties
    FRO: T_CountryProperties
    FJI: T_CountryProperties
    FIN: T_CountryProperties
    FRA: T_CountryProperties
    GUF: T_CountryProperties
    PYF: T_CountryProperties
    ATF: T_CountryProperties
    GAB: T_CountryProperties
    GMB: T_CountryProperties
    GEO: T_CountryProperties
    DEU: T_CountryProperties
    GHA: T_CountryProperties
    GIB: T_CountryProperties
    GRC: T_CountryProperties
    GRL: T_CountryProperties
    GRD: T_CountryProperties
    GLP: T_CountryProperties
    GUM: T_CountryProperties
    GTM: T_CountryProperties
    GGY: T_CountryProperties
    GIN: T_CountryProperties
    GNB: T_CountryProperties
    GUY: T_CountryProperties
    HTI: T_CountryProperties
    HMD: T_CountryProperties
    VAT: T_CountryProperties
    HND: T_CountryProperties
    HKG: T_CountryProperties
    HUN: T_CountryProperties
    ISL: T_CountryProperties
    IND: T_CountryProperties
    IDN: T_CountryProperties
    IRN: T_CountryProperties
    IRQ: T_CountryProperties
    IRL: T_CountryProperties
    IMN: T_CountryProperties
    ISR: T_CountryProperties
    ITA: T_CountryProperties
    JAM: T_CountryProperties
    JPN: T_CountryProperties
    JEY: T_CountryProperties
    JOR: T_CountryProperties
    KAZ: T_CountryProperties
    KEN: T_CountryProperties
    KIR: T_CountryProperties
    PRK: T_CountryProperties
    KOR: T_CountryProperties
    KWT: T_CountryProperties
    KGZ: T_CountryProperties
    LAO: T_CountryProperties
    LVA: T_CountryProperties
    LBN: T_CountryProperties
    LSO: T_CountryProperties
    LBR: T_CountryProperties
    LBY: T_CountryProperties
    LIE: T_CountryProperties
    LTU: T_CountryProperties
    LUX: T_CountryProperties
    MAC: T_CountryProperties
    MDG: T_CountryProperties
    MWI: T_CountryProperties
    MYS: T_CountryProperties
    MDV: T_CountryProperties
    MLI: T_CountryProperties
    MLT: T_CountryProperties
    MHL: T_CountryProperties
    MTQ: T_CountryProperties
    MRT: T_CountryProperties
    MUS: T_CountryProperties
    MYT: T_CountryProperties
    MEX: T_CountryProperties
    FSM: T_CountryProperties
    MDA: T_CountryProperties
    MCO: T_CountryProperties
    MNG: T_CountryProperties
    MNE: T_CountryProperties
    MSR: T_CountryProperties
    MAR: T_CountryProperties
    MOZ: T_CountryProperties
    MMR: T_CountryProperties
    NAM: T_CountryProperties
    NRU: T_CountryProperties
    NPL: T_CountryProperties
    NLD: T_CountryProperties
    NCL: T_CountryProperties
    NZL: T_CountryProperties
    NIC: T_CountryProperties
    NER: T_CountryProperties
    NGA: T_CountryProperties
    NIU: T_CountryProperties
    NFK: T_CountryProperties
    MNP: T_CountryProperties
    NOR: T_CountryProperties
    OMN: T_CountryProperties
    PAK: T_CountryProperties
    PLW: T_CountryProperties
    PSE: T_CountryProperties
    PAN: T_CountryProperties
    PNG: T_CountryProperties
    PRY: T_CountryProperties
    PER: T_CountryProperties
    PHL: T_CountryProperties
    PCN: T_CountryProperties
    POL: T_CountryProperties
    PRT: T_CountryProperties
    PRI: T_CountryProperties
    QAT: T_CountryProperties
    MKD: T_CountryProperties
    ROU: T_CountryProperties
    RUS: T_CountryProperties
    RWA: T_CountryProperties
    REU: T_CountryProperties
    BLM: T_CountryProperties
    SHN: T_CountryProperties
    KNA: T_CountryProperties
    LCA: T_CountryProperties
    MAF: T_CountryProperties
    SPM: T_CountryProperties
    VCT: T_CountryProperties
    WSM: T_CountryProperties
    SMR: T_CountryProperties
    STP: T_CountryProperties
    SAU: T_CountryProperties
    SEN: T_CountryProperties
    SRB: T_CountryProperties
    SYC: T_CountryProperties
    SLE: T_CountryProperties
    SGP: T_CountryProperties
    SXM: T_CountryProperties
    SVK: T_CountryProperties
    SVN: T_CountryProperties
    SLB: T_CountryProperties
    SOM: T_CountryProperties
    ZAF: T_CountryProperties
    SGS: T_CountryProperties
    SSD: T_CountryProperties
    ESP: T_CountryProperties
    LKA: T_CountryProperties
    SDN: T_CountryProperties
    SUR: T_CountryProperties
    SJM: T_CountryProperties
    SWE: T_CountryProperties
    CHE: T_CountryProperties
    SYR: T_CountryProperties
    TWN: T_CountryProperties
    TJK: T_CountryProperties
    TZA: T_CountryProperties
    THA: T_CountryProperties
    TLS: T_CountryProperties
    TGO: T_CountryProperties
    TKL: T_CountryProperties
    TON: T_CountryProperties
    TTO: T_CountryProperties
    TUN: T_CountryProperties
    TUR: T_CountryProperties
    TKM: T_CountryProperties
    TCA: T_CountryProperties
    TUV: T_CountryProperties
    UGA: T_CountryProperties
    UKR: T_CountryProperties
    ARE: T_CountryProperties
    GBR: T_CountryProperties
    UMI: T_CountryProperties
    USA: T_CountryProperties
    URY: T_CountryProperties
    UZB: T_CountryProperties
    VUT: T_CountryProperties
    VEN: T_CountryProperties
    VNM: T_CountryProperties
    VGB: T_CountryProperties
    VIR: T_CountryProperties
    WLF: T_CountryProperties
    ESH: T_CountryProperties
    YEM: T_CountryProperties
    ZMB: T_CountryProperties
    ZWE: T_CountryProperties
    ALA: T_CountryProperties

    def asdict(self) -> Dict[str, T_CountryProperties]:
        return asdict(self)


T_CountryIndex = TypeVar("T_CountryIndex", bound=dataclass)


def load_countries_generic(
    index_cls: Type[T_CountryIndex],
    locale: str = "en",
    loader: DataLoader = default_dataloader,
) -> T_CountryIndex:
    orig_index_cls = index_cls
    country_cls = None

    # Unfold generic types.
    if hasattr(index_cls, "__origin__"):
        orig_index_cls = getattr(index_cls, "__origin__")
        generic_args = getattr(index_cls, "__args__", tuple())
        assert (
            len(generic_args) == 1
        ), "only generic types with 1 parameter are allowed in this context"
        country_cls = generic_args[0]

    if not is_dataclass(orig_index_cls):
        raise ValueError(f"`{orig_index_cls}` must be a dataclass")

    kwargs = {}
    for fld in fields(orig_index_cls):
        kwargs[fld.name] = load_country_generic(
            country_cls or fld.type,
            fld.name,
            locale=locale,
            loader=loader,
        )

    return index_cls(**kwargs)


def load_countries(locale: str = "en", loader: DataLoader = default_dataloader):
    return load_countries_generic(
        FullCountryIndex[CountryProperties], locale=locale, loader=loader
    )
