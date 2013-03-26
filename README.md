Getting the database into the app
    http://stackoverflow.com/questions/2230354/any-way-to-pre-populate-core-data/2230417#2230417

Note on timestamps:
    They are all stored as Unix timestamps in the database (integer number of
    seconds since Jan 1, 1970). To get this on iOS, see here:
    http://stackoverflow.com/questions/2997062/how-to-convert-nsdate-into-unix-timestamp-iphone-sdk

    Times in the database range from 4/19/12 to 1/15/13.

List of locations
    select name, id from locations;

List of tanks for location
    select distinct(tank), fluid_type from events where location_id = ?;

Level of tank over time
    select level, datetime(time, 'unixepoch') from events where tank = ? order by time desc;

Number of transactions per tank
    select tank, count() from events where type = "TRANSACTION" group by tank;

List of transactions
    select change, duration, range, datetime(time, 'unixepoch') from events where type = 'TRANSACTION';

Range queries need to exclude "MISSING SENSOR ALARM"

List of alarms:
    select * from events where type like '%alarm%' order by time desc;

