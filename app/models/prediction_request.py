from dataclasses import dataclass


@dataclass
class PredictionRequest:
    age: float
    gender: str
    education_level: str
    social_media_hours: float
    ai_usage_hours: float
    sleep_hours: float
    physical_activity_hours: float
    mental_health_score: float
    physical_health_score: float
    social_isolation_score: float
    burnout_level: str
    academic_performance_score: float