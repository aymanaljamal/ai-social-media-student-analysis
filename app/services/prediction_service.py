from pathlib import Path

import joblib
import pandas as pd

from app.models.prediction_request import PredictionRequest
from app.models.prediction_result import PredictionResult


class PredictionService:

    # =========================================================
    # CONSTANTS
    # =========================================================

    MODEL_FILE = "random_forest_model.pkl"
    PREPROCESSOR_FILE = "preprocessor.pkl"

    # =========================================================
    # INITIALIZATION
    # =========================================================

    def __init__(self):

        # Project root:
        #
        # data-analysis-project/
        # ├── app/
        # │   └── services/
        # │       └── prediction_service.py
        # └── models/
        #
        project_root = Path(__file__).resolve().parents[2]

        self.model_path = (
            project_root
            / "models"
            / self.MODEL_FILE
        )

        self.preprocessor_path = (
            project_root
            / "models"
            / self.PREPROCESSOR_FILE
        )

        # -----------------------------------------------------
        # CHECK FILES
        # -----------------------------------------------------

        if not self.model_path.exists():

            raise FileNotFoundError(
                "Random Forest model not found:\n"
                f"{self.model_path}"
            )

        if not self.preprocessor_path.exists():

            raise FileNotFoundError(
                "Preprocessor not found:\n"
                f"{self.preprocessor_path}"
            )

        # -----------------------------------------------------
        # LOAD MODEL
        # -----------------------------------------------------

        print("=" * 60)
        print("LOADING MACHINE LEARNING MODEL")
        print("=" * 60)

        self.model = joblib.load(
            self.model_path
        )

        print(
            f"Model loaded successfully:\n"
            f"{self.model_path}"
        )

        # -----------------------------------------------------
        # LOAD PREPROCESSOR
        # -----------------------------------------------------

        self.preprocessor = joblib.load(
            self.preprocessor_path
        )

        print(
            f"Preprocessor loaded successfully:\n"
            f"{self.preprocessor_path}"
        )

        print("=" * 60)

    # =========================================================
    # PREDICT
    # =========================================================

    def predict(
        self,
        request: PredictionRequest
    ) -> PredictionResult:

        # -----------------------------------------------------
        # CREATE DATAFRAME
        # -----------------------------------------------------

        dataframe = self._build_dataframe(
            request
        )

        print("\n" + "=" * 60)
        print("PREDICTION INPUT")
        print("=" * 60)

        print(
            dataframe.to_string(
                index=False
            )
        )

        print("=" * 60)

        # -----------------------------------------------------
        # PREPROCESS
        # -----------------------------------------------------

        processed_data = self.preprocessor.transform(
            dataframe
        )

        print(
            "Preprocessing completed successfully."
        )

        # -----------------------------------------------------
        # MODEL PREDICTION
        # -----------------------------------------------------

        prediction = self.model.predict(
            processed_data
        )[0]

        prediction = int(
            prediction
        )

        print(
            f"Raw prediction: {prediction}"
        )

        # -----------------------------------------------------
        # PREDICTION PROBABILITY
        # -----------------------------------------------------

        probability = self._get_probability(
            processed_data,
            prediction
        )

        # -----------------------------------------------------
        # RISK LEVEL
        # -----------------------------------------------------

        risk_level = self._get_risk_level(
            prediction,
            probability
        )

        # -----------------------------------------------------
        # RESULT
        # -----------------------------------------------------

        result = PredictionResult(
            prediction=prediction,
            risk_level=risk_level,
            probability=probability
        )

        print("\n" + "=" * 60)
        print("PREDICTION RESULT")
        print("=" * 60)

        print(
            f"Prediction : {result.prediction}"
        )

        print(
            f"Risk Level : {result.risk_level}"
        )

        if result.probability is not None:

            print(
                f"Probability: "
                f"{result.probability:.2f}%"
            )

        print("=" * 60)

        return result

    # =========================================================
    # BUILD DATAFRAME
    # =========================================================

    def _build_dataframe(
        self,
        request: PredictionRequest
    ) -> pd.DataFrame:

        # -----------------------------------------------------
        # FEATURE ENGINEERING
        # -----------------------------------------------------
        #
        # The training pipeline created:
        #
        # Uses_AI_Tools
        # Is_Social_Media_User
        # Is_Physically_Active
        #
        # These are binary indicators derived from the
        # corresponding usage/activity hours.
        # -----------------------------------------------------

        uses_ai_tools = (
            1
            if request.ai_usage_hours > 0
            else 0
        )

        is_social_media_user = (
            1
            if request.social_media_hours > 0
            else 0
        )

        is_physically_active = (
            1
            if request.physical_activity_hours > 0
            else 0
        )

        # -----------------------------------------------------
        # EDUCATION VALUE
        # -----------------------------------------------------
        #
        # GUI:
        #
        # Undergraduate
        # Graduate
        #
        # Dataset:
        #
        # College
        # University
        # High School
        #
        # -----------------------------------------------------

        education_level = (
            self._normalize_education_level(
                request.education_level
            )
        )

        # -----------------------------------------------------
        # BURNOUT VALUE
        # -----------------------------------------------------
        #
        # GUI may use Medium
        # Dataset uses Moderate
        #
        # -----------------------------------------------------

        burnout_level = (
            self._normalize_burnout_level(
                request.burnout_level
            )
        )

        # -----------------------------------------------------
        # DATAFRAME
        # -----------------------------------------------------

        data = {

            # Required categorical identifier.
            #
            # Student_ID is treated as a categorical feature
            # by the saved preprocessor.
            #
            "Student_ID":
                "PREDICTION_00001",

            # Numerical features
            "Age":
                request.age,

            # Categorical features
            "Gender":
                request.gender,

            "Education_Level":
                education_level,

            # Numerical features
            "Daily_Social_Media_Hours":
                request.social_media_hours,

            "Daily_AI_Tool_Usage_Hours":
                request.ai_usage_hours,

            "Sleep_Hours":
                request.sleep_hours,

            "Physical_Activity_Hours":
                request.physical_activity_hours,

            "Mental_Health_Score":
                request.mental_health_score,

            "Physical_Health_Score":
                request.physical_health_score,

            "Social_Isolation_Score":
                request.social_isolation_score,

            # Categorical
            "Burnout_Level":
                burnout_level,

            # Numerical
            "Academic_Performance_Score":
                request.academic_performance_score,

            # Engineered numerical features
            "Uses_AI_Tools":
                uses_ai_tools,

            "Is_Social_Media_User":
                is_social_media_user,

            "Is_Physically_Active":
                is_physically_active
        }

        dataframe = pd.DataFrame(
            [data]
        )

        # -----------------------------------------------------
        # IMPORTANT
        # -----------------------------------------------------
        #
        # Make sure columns are in the same order as the
        # original dataset/preprocessor.
        #
        # -----------------------------------------------------

        expected_columns = [

            "Student_ID",

            "Age",

            "Gender",

            "Education_Level",

            "Daily_Social_Media_Hours",

            "Daily_AI_Tool_Usage_Hours",

            "Sleep_Hours",

            "Physical_Activity_Hours",

            "Mental_Health_Score",

            "Physical_Health_Score",

            "Social_Isolation_Score",

            "Burnout_Level",

            "Academic_Performance_Score",

            "Uses_AI_Tools",

            "Is_Social_Media_User",

            "Is_Physically_Active"
        ]

        dataframe = dataframe[
            expected_columns
        ]

        return dataframe

    # =========================================================
    # NORMALIZE EDUCATION
    # =========================================================

    @staticmethod
    def _normalize_education_level(
        education_level: str
    ) -> str:

        education = (
            education_level
            .strip()
            .lower()
        )

        mapping = {

            "high school":
                "High School",

            "highschool":
                "High School",

            "undergraduate":
                "College",

            "college":
                "College",

            "graduate":
                "University",

            "university":
                "University"
        }

        if education in mapping:

            return mapping[
                education
            ]

        # If the value already matches one of the
        # training categories, keep it.

        valid_values = [
            "High School",
            "College",
            "University"
        ]

        for value in valid_values:

            if education == value.lower():

                return value

        raise ValueError(
            "Unsupported education level: "
            f"{education_level}\n\n"
            "Expected one of:\n"
            "High School\n"
            "College\n"
            "University"
        )

    # =========================================================
    # NORMALIZE BURNOUT
    # =========================================================

    @staticmethod
    def _normalize_burnout_level(
        burnout_level: str
    ) -> str:

        burnout = (
            burnout_level
            .strip()
            .lower()
        )

        mapping = {

            "low":
                "Low",

            "medium":
                "Moderate",

            "moderate":
                "Moderate",

            "high":
                "High"
        }

        if burnout in mapping:

            return mapping[
                burnout
            ]

        valid_values = [
            "Low",
            "Moderate",
            "High"
        ]

        for value in valid_values:

            if burnout == value.lower():

                return value

        raise ValueError(
            "Unsupported burnout level: "
            f"{burnout_level}\n\n"
            "Expected one of:\n"
            "Low\n"
            "Moderate\n"
            "High"
        )

    # =========================================================
    # PROBABILITY
    # =========================================================

    def _get_probability(
        self,
        processed_data,
        prediction: int
    ):

        if not hasattr(
            self.model,
            "predict_proba"
        ):

            return None

        probabilities = (
            self.model.predict_proba(
                processed_data
            )[0]
        )

        # -----------------------------------------------------
        # Find probability for class 1.
        #
        # We don't want max(probabilities), because the UI
        # should show the probability of ACADEMIC FAILURE,
        # not the probability of whichever class happens
        # to be predicted.
        # -----------------------------------------------------

        classes = getattr(
            self.model,
            "classes_",
            []
        )

        for index, class_value in enumerate(
            classes
        ):

            if int(class_value) == 1:

                return float(
                    probabilities[index] * 100
                )

        # -----------------------------------------------------
        # Fallback
        # -----------------------------------------------------

        return float(
            probabilities[-1] * 100
        )

    # =========================================================
    # RISK LEVEL
    # =========================================================

    @staticmethod
    def _get_risk_level(
        prediction: int,
        probability
    ):

        # -----------------------------------------------------
        # Risk classification is based on probability of
        # academic failure.
        # -----------------------------------------------------

        if probability is not None:

            if probability >= 70:

                return "High"

            if probability >= 40:

                return "Medium"

            return "Low"

        # -----------------------------------------------------
        # Fallback when model doesn't support probability
        # -----------------------------------------------------

        if prediction == 1:

            return "High"

        return "Low"