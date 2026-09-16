import os
import pandas as pd


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

INPUT_FILE = os.path.join(
    BASE_DIR,
    "datasets",
    "youtube_channel_stats.csv"
)

OUTPUT_FILE = os.path.join(
    BASE_DIR,
    "datasets",
    "youtube_channel_stats_utf8.csv"
)


encodings = [
    "utf-8",
    "utf-8-sig",
    "cp1252",
    "latin1"
]


df = None

for encoding in encodings:

    try:

        print(f"Trying encoding: {encoding}")

        df = pd.read_csv(
            INPUT_FILE,
            encoding=encoding
        )

        print(
            f"Successfully read file using {encoding}"
        )

        break

    except UnicodeDecodeError:

        print(
            f"Failed with {encoding}"
        )


if df is None:

    raise ValueError(
        "Could not decode the CSV using the available encodings."
    )


df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8-sig"
)


print()
print("CSV converted successfully!")
print()
print(f"Output file: {OUTPUT_FILE}")
print()
print("Shape:", df.shape)
print()
print("Columns:")
print(df.columns.tolist())