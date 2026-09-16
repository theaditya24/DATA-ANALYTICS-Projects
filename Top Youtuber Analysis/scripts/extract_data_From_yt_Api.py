import os
import pandas as pd
from dotenv import load_dotenv
from googleapiclient.discovery import build


# --------------------------------
# PROJECT PATHS
# --------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENV_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    ".env"
)

INPUT_FILE = os.path.join(
    BASE_DIR,
    "datasets",
    "youtube_data_india.csv"
)

OUTPUT_FILE = os.path.join(
    BASE_DIR,
    "datasets",
    "youtube_data_india_updated.csv"
)


# --------------------------------
# LOAD API KEY
# --------------------------------

load_dotenv(ENV_FILE)

API_KEY = os.getenv("YOUTUBE_API_KEY")

if not API_KEY:
    raise ValueError(
        "YOUTUBE_API_KEY not found in scripts/.env file"
    )


# --------------------------------
# CONNECT TO YOUTUBE API
# --------------------------------

youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)


# --------------------------------
# FUNCTION TO GET CHANNEL STATS
# --------------------------------

def get_channel_stats(youtube, channel_id):

    request = youtube.channels().list(
        part="snippet,statistics",
        id=channel_id
    )

    response = request.execute()

    if response["items"]:

        channel = response["items"][0]

        return {
            "channel_id": channel_id,
            "channel_name": channel["snippet"]["title"],
            "total_subscribers": channel["statistics"].get(
                "subscriberCount"
            ),
            "total_views": channel["statistics"].get(
                "viewCount"
            ),
            "total_videos": channel["statistics"].get(
                "videoCount"
            )
        }

    return {
        "channel_id": channel_id,
        "channel_name": None,
        "total_subscribers": None,
        "total_views": None,
        "total_videos": None
    }


# --------------------------------
# READ DATASET
# --------------------------------

print("Reading dataset...")

df = pd.read_csv(INPUT_FILE)

print(f"Total rows: {len(df)}")


# --------------------------------
# EXTRACT CHANNEL ID
# --------------------------------

df["channel_id"] = df["NAME"].str.extract(
    r"@(.+)$"
)


# --------------------------------
# GET UNIQUE CHANNEL IDs
# --------------------------------

channel_ids = (
    df["channel_id"]
    .dropna()
    .unique()
)

print(f"Unique channels found: {len(channel_ids)}")


# --------------------------------
# EXTRACT YOUTUBE DATA
# --------------------------------

channel_stats = []

for i, channel_id in enumerate(channel_ids, start=1):

    print(
        f"Processing {i}/{len(channel_ids)}: {channel_id}"
    )

    try:

        stats = get_channel_stats(
            youtube,
            channel_id
        )

        channel_stats.append(stats)

    except Exception as e:

        print(
            f"Error processing {channel_id}: {e}"
        )

        channel_stats.append({
            "channel_id": channel_id,
            "channel_name": None,
            "total_subscribers": None,
            "total_views": None,
            "total_videos": None
        })


# --------------------------------
# CREATE STATS DATAFRAME
# --------------------------------

stats_df = pd.DataFrame(channel_stats)


# --------------------------------
# MERGE DATA
# --------------------------------

combined_df = df.merge(
    stats_df,
    on="channel_id",
    how="left"
)


# --------------------------------
# SAVE UPDATED DATASET
# --------------------------------

combined_df.to_csv(
    OUTPUT_FILE,
    index=False
)


# --------------------------------
# DISPLAY RESULTS
# --------------------------------

print("\n--------------------------------")
print("DATA EXTRACTION COMPLETED")
print("--------------------------------")

print(f"\nOutput file:")
print(OUTPUT_FILE)

print("\nFinal columns:")
print(combined_df.columns.tolist())

print("\nFirst 10 rows:")
print(combined_df.head(10))