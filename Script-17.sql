select count("itemId") as "count1", "date", lead (count("itemId"), 1) over (order by "date") as "count2",
(count("itemId") - lead (count("itemId"), 1) over (order by "date")) as "delta"
from (
	select "itemId", date_trunc('month', "dateId") as "date" from distributor.sales s
	where "dateId" <= '2014-01-14'
	group by "itemId" , "date"
	having date_part('day', '2014-01-14' - max("dateId")::timestamp)<=180
)
group by "date"