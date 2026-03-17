import mysql.connector
from maps_data.DigitalHunter_map import plot_map_with_geometry

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="digital_hunter"
)

cursor = mydb.cursor()

def q1():
    result = []
    cursor.execute("""select entity_id,target_name,priority_level,movement_distance_km 
                      from targets
                      where movement_distance_km > 5
                      and priority_level in (1 , 2);""")
    fetch= cursor.fetchall()
    for x in fetch:
        result.append(x)
    return result

def q2():
    result = []
    cursor.execute("""select signal_type,count(*) number_of_occurrences 
                      from intel_signals
                      group by signal_type
                      order by number_of_occurrences desc;""")
    fetch = cursor.fetchall()
    for x in fetch:
        result.append(x)
    return result

def q3():
    result = []
    cursor.execute("""select entity_id ,count(*) number_of_occurrences
                      from intel_signals
                      group by entity_id,priority_level
                      having priority_level = 99 
                      or entity_id like '%UNKNOWN%'
                      order by number_of_occurrences desc
                      limit 3""")
    fetch = cursor.fetchall()
    for x in fetch:
        result.append(x)
    return result

def q4():
    result = []
    cursor.execute("""  select day_tabl.entity_id from(
                            select entity_id 
                            from intel_signals
                            where hour(timestamp) between 8 and 20
                            group by entity_id 
                            having sum(distance_from_last) = 0) 
                        as day_tabl
                        inner join (
                            select entity_id 
                            from intel_signals
                            where hour(timestamp) not between 8 and 20
                            group by entity_id 
                            having sum(distance_from_last) > 10) 
                        as night_tabl""")
    fetch = cursor.fetchall()
    for x in fetch:
        result.append(x)
    return result

def q5(entity_id):
    result = []
    cursor.execute("""select reported_lat,reported_lon 
                      from intel_signals
                      where entity_id =  %s""",[entity_id])
    fetch = cursor.fetchall()
    for x in fetch:
        result.append(x)
    plot_map_with_geometry(result)

