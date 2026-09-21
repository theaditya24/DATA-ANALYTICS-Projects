CREATE DATABASE youtube_analysis;

-- Select the database
USE youtube_analysis;


-- Create the Table
CREATE TABLE youtube_channel_stats_raw (
    channel_id VARCHAR(100),
    channel_name VARCHAR(255),
    total_subscribers BIGINT,
    total_views BIGINT,
    total_videos INT
);

-- Rename the table
ALTER TABLE youtube_channel_stats_raw
RENAME TO yt_stats;

DROP TABLE IF EXISTS yt_stats;

CREATE TABLE yt_Stats (
    channel_id VARCHAR(100),
    channel_name VARCHAR(255),
    total_subscribers BIGINT,
    total_views BIGINT,
    total_videos INT
);

SET GLOBAL local_infile = 1;

LOAD DATA LOCAL INFILE "C:/Projects/PowerBi Projects/Top Youtuber Analysis/datasets/youtube_channel_stats_utf8.csv"
INTO TABLE yt_stats
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(channel_id, channel_name, total_subscribers, total_views, total_videos);


-- Check the table structure
DESCRIBE yt_stats;

-- Check total number of records
SELECT COUNT(*) AS total_rows
FROM yt_stats;

-- Look at the complete data
SELECT * FROM yt_stats;


-- Check NULL values
SELECT
    COUNT(*) AS total_rows,
    SUM(channel_id IS NULL) AS missing_channel_id,
    SUM(channel_name IS NULL) AS missing_channel_name,
    SUM(total_subscribers IS NULL) AS missing_subscribers,
    SUM(total_views IS NULL) AS missing_views,
    SUM(total_videos IS NULL) AS missing_videos
FROM yt_stats;


-- Check blank values
SELECT *
FROM yt_stats
WHERE TRIM(channel_id) = ''
   OR TRIM(channel_name) = '';
   
   
-- Check duplicate channel IDs
SELECT
    channel_id,
    COUNT(*) AS duplicate_count
FROM yt_stats
GROUP BY channel_id
HAVING COUNT(*) > 1;


-- Check negative values
SELECT *
FROM yt_stats
WHERE total_subscribers < 0
   OR total_views < 0
   OR total_videos < 0;
   
   
-- Check zero values
SELECT *
FROM yt_stats
WHERE total_subscribers = 0
   OR total_views = 0
   OR total_videos = 0;
   
   
-- Check the data types
DESCRIBE yt_stats;


-- Step 1 — Whitespace & Text Cleaning
-- First Check for whitespace issues
SELECT
    channel_id,
    channel_name
FROM yt_stats
WHERE channel_id <> TRIM(channel_id)
   OR channel_name <> TRIM(channel_name);
-- Since it does not return any value so it means no rows have any record who contains leading/trailing spaces.
-- If there was a row which contains this spaces then we have used 'UPDATE TABLE-NAME SET COLUMN-NAME = TRIM(COLUMN-NAME);'

-- Check for blank strings
SELECT *
FROM yt_stats
WHERE TRIM(channel_id) = ''
   OR TRIM(channel_name) = '';
   
SET SQL_SAFE_UPDATES = 0;

-- Updating null values to blank strings
UPDATE yt_stats
SET
    channel_id = NULLIF(TRIM(channel_id), ''),
    channel_name = NULLIF(TRIM(channel_name), '')
WHERE
    TRIM(channel_id) <> channel_id
    OR TRIM(channel_name) <> channel_name
    OR TRIM(channel_id) = ''
    OR TRIM(channel_name) = '';

SET SQL_SAFE_UPDATES = 1;

SELECT *
FROM yt_stats
WHERE TRIM(channel_id) = ''
   OR TRIM(channel_name) = '';
   
-- Step 2 - Handling NULL values
-- Counting Null Values First
SELECT
    COUNT(*) AS total_rows,
    SUM(channel_id IS NULL) AS missing_channel_id,
    SUM(channel_name IS NULL) AS missing_channel_name,
    SUM(total_subscribers IS NULL) AS missing_subscribers,
    SUM(total_views IS NULL) AS missing_views,
    SUM(total_videos IS NULL) AS missing_videos
FROM yt_stats;

-- Rows that contains Null Values
SELECT *
FROM yt_stats
WHERE channel_id IS NULL
   OR channel_name IS NULL
   OR total_subscribers IS NULL
   OR total_views IS NULL
   OR total_videos IS NULL;

-- here we saw that only channel_name for 4 channel_id has null values rest column are containing 0 so we have to replace that with 'null'.

SET SQL_SAFE_UPDATES = 0;

UPDATE yt_stats
SET
    total_subscribers = NULL,
    total_views = NULL,
    total_videos = NULL
WHERE channel_name IS NULL
  AND total_subscribers = 0
  AND total_views = 0
  AND total_videos = 0;

SET SQL_SAFE_UPDATES = 1;

SELECT *
FROM yt_stats
WHERE channel_name IS NULL
   OR total_subscribers IS NULL
   OR total_views IS NULL
   OR total_videos IS NULL;
   
