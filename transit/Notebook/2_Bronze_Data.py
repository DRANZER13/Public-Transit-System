
# Update this path after uploading the data folder to a Databricks Volume.
base_path = "/Volumes/workspace/default/public_transit_raw"

routes_path = f"{base_path}/routes.csv"
stations_path = f"{base_path}/stations.csv"
vehicles_path = f"{base_path}/vehicles.csv"
trips_path = f"{base_path}/trips.csv"
ridership_path = f"{base_path}/ridership.csv"

 ## 1. Bronze Layer — Load raw CSV files

routes_bronze = spark.read.option("header", True).option("inferSchema", True).csv(routes_path)
stations_bronze = spark.read.option("header", True).option("inferSchema", True).csv(stations_path)
vehicles_bronze = spark.read.option("header", True).option("inferSchema", True).csv(vehicles_path)
trips_bronze = spark.read.option("header", True).option("inferSchema", True).csv(trips_path)
ridership_bronze = spark.read.option("header", True).option("inferSchema", True).csv(ridership_path)

routes_bronze.write.format("delta").mode("overwrite").saveAsTable("workspace.default.bronze_routes")
stations_bronze.write.format("delta").mode("overwrite").saveAsTable("workspace.default.bronze_stations")
vehicles_bronze.write.format("delta").mode("overwrite").saveAsTable("workspace.default.bronze_vehicles")
trips_bronze.write.format("delta").mode("overwrite").saveAsTable("workspace.default.bronze_trips")
ridership_bronze.write.format("delta").mode("overwrite").saveAsTable("workspace.default.bronze_ridership")

print("Bronze tables created.")

