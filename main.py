from pathlib import Path

from pipeline.ingest import ingest
from pipeline.validate import validate
from pipeline.transform import transform
from pipeline.train import train
from pipeline.evaluate import evaluate


def _init_dirs():
    for d in ["data/raw", "data/validated", "data/transformed", "data/models"]:
        Path(d).mkdir(parents=True, exist_ok=True)


def main():
    _init_dirs()
    ingest.run()
    validate.run()
    transform.run()
    train.run()
    evaluate.run()


if __name__ == "__main__":
    main()
