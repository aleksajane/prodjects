select extract ('isodow' from "dateId") as "day",
		(sum("salesRub")/ 
			(select sum("salesRub")
			from distributor.sales s 
			inner join distributor.item i using("itemId")
			where lower(category) like '%обои%'))*100 as "week_coef_money"
from distributor.sales s 
inner join distributor.item i using("itemId")
where lower(category) like '%обои%'
group by extract (isodow from "dateId")