 #2. Silver Layer — Clean data and set correct data types

from pyspark.sql.functions import col, to_timestamp, trim, when, year, current_date

routes_silver = (
    routes_bronze
    .dropDuplicates(["route_id"])
    .dropna(subset=["route_id", "route_name"])
    .withColumn("route_name", trim(col("route_name")))
)

stations_silver = (
    stations_bronze
    .dropDuplicates(["station_id"])
    .dropna(subset=["station_id", "station_name", "route_id"])
    .withColumn("station_name", trim(col("station_name")))
)

vehicles_silver = (
    vehicles_bronze
    .dropDuplicates(["vehicle_id"])
    .dropna(subset=["vehicle_id", "capacity", "manufacture_year"])
    .withColumn("capacity", col("capacity").cast("int"))
    .withColumn("manufacture_year", col("manufacture_year").cast("int"))
    .withColumn("vehicle_age", year(current_date()) - col("manufacture_year"))
)

trips_silver = (
    trips_bronze
    .dropDuplicates(["trip_id"])
    .dropna(subset=["trip_id", "route_id", "vehicle_id"])
    .withColumn("scheduled_time", to_timestamp(col("scheduled_time")))
    .withColumn("actual_time", to_timestamp(col("actual_time")))
    .withColumn("delay_minutes", col("delay_minutes").cast("int"))
    .withColumn("on_time_status", when(col("delay_minutes") <= 5, "On Time").otherwise("Delayed"))
)

ridership_silver = (
    ridership_bronze
    .dropDuplicates(["ridership_id"])
    .dropna(subset=["ridership_id", "trip_id", "station_id"])
    .withColumn("boardings", col("boardings").cast("int"))
    .withColumn("alightings", col("alightings").cast("int"))
    .withColumn("passenger_load_after_stop", col("passenger_load_after_stop").cast("int"))
    .withColumn("vehicle_capacity", col("vehicle_capacity").cast("int"))
)

routes_silver.write.format("delta").mode("overwrite").saveAsTable("workspace.default.silver_routes")
stations_silver.write.format("delta").mode("overwrite").saveAsTable("workspace.default.silver_stations")
vehicles_silver.write.format("delta").mode("overwrite").saveAsTable("workspace.default.silver_vehicles")
trips_silver.write.format("delta").mode("overwrite").saveAsTable("workspace.default.silver_trips")
ridership_silver.write.format("delta").mode("overwrite").saveAsTable("workspace.default.silver_ridership")

print("Silver tables created.")

