select "date", "manager", avg("average_check") over(partition by "manager" order by "date" rows between 3 preceding and 1 preceding) as "av_check_last_3_months" from (
	select date_trunc('month', "dateId")::date as "date", fullname as "manager", avg("salesRub") as "average_check" from distributor.sales inner join distributor.salesmanager using("salesManagerId")
	where "salesManagerId" is not null
	group by date_trunc('month', "dateId"), fullname
)
order by "date"