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
limit 3;

-- q4 
select day_tabl.entity_id from(
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
as night_tabl

-- q5 
-- select reported_lat,reported_lon 
-- from intel_signals
-- where entity_id =  'TGT-001';









