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
    "youtube_data_india_updated.csv"
)


OUTPUT_FILE = os.path.join(
    BASE_DIR,
    "datasets",
    "youtube_channel_stats.csv"
)


df = pd.read_csv(INPUT_FILE)


mysql_df = df[
    [
        "channel_id",
        "channel_name",
        "total_subscribers",
        "total_views",
        "total_videos"
    ]
].copy()


mysql_df["total_subscribers"] = (
    pd.to_numeric(
        mysql_df["total_subscribers"],
        errors="coerce"
    )
    .round()
    .astype("Int64")
)


mysql_df["total_views"] = (
    pd.to_numeric(
        mysql_df["total_views"],
        errors="coerce"
    )
    .round()
    .astype("Int64")
)


mysql_df["total_videos"] = (
    pd.to_numeric(
        mysql_df["total_videos"],
        errors="coerce"
    )
    .round()
    .astype("Int64")
)


mysql_df.to_csv(
    OUTPUT_FILE,
    index=False
)


print("MySQL dataset created successfully!")
print()
print(mysql_df.head(10))
print()
print("Shape:", mysql_df.shape)
print()
print("Columns:")
print(mysql_df.columns.tolist())
print()
print("Saved to:")
print(OUTPUT_FILE)