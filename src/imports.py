# ============================================================
# IMPORTS
# ============================================================


# =========================
# Data Manipulation
# =========================

import pandas as pd
import numpy as np


# =========================
# Data Visualization
# =========================

import matplotlib.pyplot as plt
import seaborn as sns


# =========================
# Machine Learning
# =========================

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import (
    LabelEncoder,
    StandardScaler,
    OneHotEncoder
)

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor
)