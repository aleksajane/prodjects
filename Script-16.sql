select "date"::date, "top_3_revenue"/"total_revenue" as "share" from (
	select "date", sum("revenue") as "top_3_revenue" from (
		select date_trunc('month', "dateId") as "date", "brand", sum("salesRub") as "revenue", rank() over (partition by date_trunc('month', "dateId") order by sum("salesRub") desc) as "rank" from distributor.sales inner join distributor.item using("itemId")
		group by "brand", "date"
	)
	where "rank" <= 3
	group by "date"
)
inner join (
	select date_trunc('month', "dateId") as "date", sum("salesRub") as "total_revenue" from distributor.sales
	group by date_trunc('month', "dateId")) using("date")