"""NBA team identifiers.

Provides an immutable dataclass `Team` exposing NBA teams as class attributes
mapping standard abbreviations (e.g., `OKC`) to full team names (e.g.,
"Oklahoma City Thunder").
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Team:
    """Immutable mapping of NBA team abbreviations to full names.

    This dataclass exposes each NBA team as a class attribute where the
    attribute name is the team's standard abbreviation (e.g., `Team.OKC`),
    and the value is the full team name (e.g., "Oklahoma City Thunder").
    """

    ATL: str = "Atlanta Hawks"
    BOS: str = "Boston Celtics"
    BKN: str = "Brooklyn Nets"
    CHA: str = "Charlotte Hornets"
    CHI: str = "Chicago Bulls"
    CLE: str = "Cleveland Cavaliers"
    DAL: str = "Dallas Mavericks"
    DEN: str = "Denver Nuggets"
    DET: str = "Detroit Pistons"
    GSW: str = "Golden State Warriors"
    HOU: str = "Houston Rockets"
    IND: str = "Indiana Pacers"
    LAC: str = "Los Angeles Clippers"
    LAL: str = "Los Angeles Lakers"
    MEM: str = "Memphis Grizzlies"
    MIA: str = "Miami Heat"
    MIL: str = "Milwaukee Bucks"
    MIN: str = "Minnesota Timberwolves"
    NOP: str = "New Orleans Pelicans"
    NYK: str = "New York Knicks"
    OKC: str = "Oklahoma City Thunder"
    ORL: str = "Orlando Magic"
    PHI: str = "Philadelphia 76ers"
    PHX: str = "Phoenix Suns"
    POR: str = "Portland Trail Blazers"
    SAC: str = "Sacramento Kings"
    SAS: str = "San Antonio Spurs"
    TOR: str = "Toronto Raptors"
    UTA: str = "Utah Jazz"
    WAS: str = "Washington Wizards"
