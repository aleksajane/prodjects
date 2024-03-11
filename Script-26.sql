select "date", "fabrica1", "sales"/"total"*100 as "share"
from (	select date_trunc('month', "dateId") as "date", coalesce(fabrica, 'else') as "fabrica1", 
	sum("salesRub") as "sales"
	from distributor.sales s 
	inner join distributor.item i using("itemId")
	group by "date", "fabrica")
inner join (select date_trunc('month', "dateId") as "date", sum("salesRub") as "total"
	from distributor.sales s
	group by "date") using("date")