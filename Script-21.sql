select "date", "manager", "client" from (
	select "date", "manager", "client", rank() over(partition by "date", "manager" order by "revenue_last_3_months" desc) as "rank" from(
		select "date", "manager", "client", sum("revenue") over(partition by "manager", "client" order by "date" rows between 2 preceding and current row) as "revenue_last_3_months" from(
			select date_trunc('month', "dateId")::date as "date", fullname as "manager", "companyName" as "client", sum("salesRub") as "revenue" from distributor.sales inner join distributor.company using("companyId") inner join distributor.salesmanager using("salesManagerId")
			group by date_trunc('month', "dateId"), fullname, "companyName"
		)
	)
)
where "rank" <= 5