select "exclusive_sales"/"total" as "share", "date"::date
from (
		select date_trunc('month', "dateId") as "date", sum("salesRub") as "exclusive_sales"
		from distributor.sales s 
		inner join distributor.item i using("itemId")
		where lower(category) like '%обои%' and "exclusive" = 'Да'
		group by "date"
	)
inner join (
			select sum("salesRub") as "total", date_trunc('month', "dateId") as "date"
			from distributor.sales s 
			inner join distributor.item i using("itemId")
			where lower(category) like '%обои%'
			group by "date"
		) using ("date")
limit 100