from dataclasses import dataclass

@dataclass(frozen=True)
class Run:
    id: str
    name: str
    number_range: range

all_runs = [
    Run("LDA", "Lauf der Asse", range(1, 3)),
    Run("JDML5", "5 KM Jedermannslauf", range(1, 6)),
    Run("JDML10", "10 KM Jedermannslauf", range(1, 11)),
    Run("KL", "Kinderlauf", range(1, 11)),
]