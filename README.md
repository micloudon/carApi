# Under Construction

source venv/bin/activate
pip freeze > requirements.txt

LOAD DATA INFILE '/home/mic/Documents/DjangoWorkBench/djangoApi/car_data - car_data.csv' 
INTO TABLE discounts 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


c = Car(make='bmw', model='3 series', year=1993, fuelType="premium", horsePower=200, cylinders=6, driveTrain='rwd', numDoors=4, size='compact, style='sedan', highwayMpg=28, cityMpg=22, msrp=5000)