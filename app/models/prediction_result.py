from dataclasses import dataclass


@dataclass
class PredictionResult:
    prediction: int
    risk_level: str
    probability: float