from src.imports import pd


DATA_PATH = "data/raw/AI_SocialMedia_Student_Health_Dataset_clean.csv"


def load_data(file_path=DATA_PATH):
    """
    Load the student dataset from a CSV file.

    Args:
        file_path (str): Path to the CSV dataset.

    Returns:
        pd.DataFrame: Loaded dataset.
    """

    try:
        df = pd.read_csv(file_path)

        print(f"Dataset loaded successfully: {file_path}")
        print(f"Dataset shape: {df.shape}")

        return df

    except FileNotFoundError:
        print(f"Error: Dataset not found at: {file_path}")
        return None

    except Exception as e:
        print(f"Error while loading dataset: {e}")
        return None