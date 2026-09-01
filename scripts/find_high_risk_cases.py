
import sys
import json
import random
from pathlib import Path


# =========================================================
# PROJECT ROOT
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from app.models.prediction_request import PredictionRequest
from app.services.prediction_service import PredictionService


# =========================================================
# CONFIGURATION
# =========================================================

NUMBER_OF_CASES = 1000

OUTPUT_DIR = (
    PROJECT_ROOT
    / "reports"
    / "test_cases"
)

OUTPUT_FILE = (
    OUTPUT_DIR
    / "prediction_test_cases.json"
)


# =========================================================
# GENERATE RANDOM CASE
# =========================================================

def generate_case():

    return {
        "age": random.randint(15, 30),

        "gender": random.choice([
            "Male",
            "Female"
        ]),

        "education_level": random.choice([
            "High School",
            "Undergraduate",
            "Graduate"
        ]),

        "social_media_hours": round(
            random.uniform(0, 16),
            2
        ),

        "ai_usage_hours": round(
            random.uniform(0, 12),
            2
        ),

        "sleep_hours": round(
            random.uniform(3, 14),
            2
        ),

        "physical_activity_hours": round(
            random.uniform(0, 8),
            2
        ),

        "mental_health_score": round(
            random.uniform(0, 100),
            2
        ),

        "physical_health_score": round(
            random.uniform(0, 100),
            2
        ),

        "social_isolation_score": round(
            random.uniform(0, 100),
            2
        ),

        "burnout_level": random.choice([
            "Low",
            "Medium",
            "High"
        ]),

        "academic_performance_score": round(
            random.uniform(0, 100),
            2
        )
    }


# =========================================================
# CREATE PREDICTION REQUEST
# =========================================================

def create_request(data):

    return PredictionRequest(
        age=data["age"],
        gender=data["gender"],
        education_level=data["education_level"],
        social_media_hours=data["social_media_hours"],
        ai_usage_hours=data["ai_usage_hours"],
        sleep_hours=data["sleep_hours"],
        physical_activity_hours=data[
            "physical_activity_hours"
        ],
        mental_health_score=data[
            "mental_health_score"
        ],
        physical_health_score=data[
            "physical_health_score"
        ],
        social_isolation_score=data[
            "social_isolation_score"
        ],
        burnout_level=data[
            "burnout_level"
        ],
        academic_performance_score=data[
            "academic_performance_score"
        ]
    )


# =========================================================
# CREATE TEST CASE RESULT
# =========================================================

def create_test_case(
    case_id,
    data,
    result
):

    probability = None

    if result.probability is not None:

        probability = round(
            float(result.probability),
            2
        )

    return {
        "test_case_id": case_id,

        "input": data,

        "expected_result": {
            "prediction": result.prediction,
            "risk_level": result.risk_level,
            "probability": probability
        }
    }


# =========================================================
# SAVE ALL TEST CASES
# =========================================================

def save_test_cases(test_cases):

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    output = {
        "test_cases_count": len(test_cases),
        "test_cases": test_cases
    }

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            output,
            file,
            indent=4,
            ensure_ascii=False
        )


# =========================================================
# MAIN
# =========================================================

def main():

    # -----------------------------------------------------
    # LOAD PREDICTION SERVICE
    # -----------------------------------------------------

    service = PredictionService()

    test_cases = []

    # -----------------------------------------------------
    # GENERATE + PREDICT ALL CASES
    # -----------------------------------------------------

    for index in range(
        NUMBER_OF_CASES
    ):

        data = generate_case()

        request = create_request(
            data
        )

        result = service.predict(
            request
        )

        case_id = (
            f"PREDICTION_{index + 1:05d}"
        )

        test_case = create_test_case(
            case_id,
            data,
            result
        )

        test_cases.append(
            test_case
        )

    # -----------------------------------------------------
    # SAVE
    # -----------------------------------------------------

    save_test_cases(
        test_cases
    )


# =========================================================
# ENTRY POINT
# =========================================================

if __name__ == "__main__":

    main()
