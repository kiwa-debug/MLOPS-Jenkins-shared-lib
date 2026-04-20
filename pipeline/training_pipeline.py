import os
from src.data_processing import DataProcessing
from src.model_training import ModelTraining

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __name__=="__main__":
    processor = DataProcessing(
        os.path.join(ROOT_DIR, "artifacts", "raw", "data.csv"),
        os.path.join(ROOT_DIR, "artifacts", "processed")
    )
    processor.run()

    trainer = ModelTraining(
        os.path.join(ROOT_DIR, "artifacts", "processed"),
        os.path.join(ROOT_DIR, "artifacts", "models")
    )
    trainer.run()