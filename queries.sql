use digital_hunter;

-- q1
select entity_id,target_name,priority_level,movement_distance_km 
from targets
where movement_distance_km > 5
and priority_level in (1 , 2);

-- q2
select signal_type,count(*) number_of_occurrences 
from intel_signals
group by signal_type
order by number_of_occurrences desc;

-- q3
select entity_id ,count(*) number_of_occurrences
from intel_signals
group by entity_id,priority_level
having priority_level = 99 
or entity_id like '%UNKNOWN%'
order by number_of_occurrences desc
limit 3

-- q4 








