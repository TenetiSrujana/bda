bash
start-all.sh
jps

rm -rf metastore_db
rm -f derby.log
schematool -dbType derby -initSchema

nano temp.txt
19-01-2024,500001,25
20-01-2024,500003,24
21-01-2024,500045,35
22-01-2024,500014,23
23-01-2024,500017,28

pwd
hive

CREATE TABLE temp_data(
dt STRING,
pincode INT,
temp INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';

LOAD DATA LOCAL INPATH '/home/hadoop/temp.txt' INTO TABLE temp_data;

SELECT * FROM temp_data;

SELECT dt, MAX(temp)
FROM temp_data
GROUP BY dt;
