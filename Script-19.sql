select "date", "manager", avg(round("revenue")) over(partition by "manager" order by "date" rows between 3 preceding and 1 preceding) as "revenue_last_3_months" from (
	select date_trunc('month', "dateId")::date as "date", fullname as "manager", sum("salesRub") as "revenue" from distributor.sales inner join distributor.salesmanager using("salesManagerId")
	where "salesManagerId" is not null
	group by date_trunc('month', "dateId"), fullname
	)
order by "date"