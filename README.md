# Public Transit Performance and Ridership Analysis

## Project Goal
This project models a public bus transit system using synthetic data. It analyzes:
1. On-time performance by route
2. Ridership trends by time of day
3. Ridership by station zone
4. Peak-hour overcrowding
5. Relationship between vehicle age and delays

## Synthetic Data Files
- routes.csv: 8 routes
- stations.csv: 48 stations
- vehicles.csv: 30 vehicles
- trips.csv: 500 trips
- ridership.csv: 3,000 stop-level ridership records

## Databricks Architecture
Raw CSV files → Bronze Delta tables → Silver cleaned tables → Gold dashboard tables

## Upload Instructions
1. In Databricks, create a Volume named `public_transit_raw`.
2. Upload all five CSV files from the `data` folder.
3. Confirm the path:
   `/Volumes/workspace/default/public_transit_raw/`
4. Import `Public_Transit_Databricks_Notebook.py` as a Databricks notebook.
5. Run all cells from top to bottom.
6. Create a Databricks SQL dashboard using `dashboard_queries.sql`.

## Recommended Dashboard Layout
Top KPI cards:
- Total Trips
- Total Boardings
- Average Delay
- On-Time Percentage

Charts:
- Average Delay by Route — bar chart
- On-Time Percentage by Route — bar chart
- Boardings by Time of Day — column chart
- Boardings by Station Zone — pie/bar chart
- Overcrowding Percentage — heatmap/bar chart
- Vehicle Age vs Average Delay — scatter plot

## On-Time Rule
A trip is treated as on time when its delay is 5 minutes or less.
