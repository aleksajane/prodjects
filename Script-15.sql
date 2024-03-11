select (
	select sum("revenue") as "revenue_top_3" from (
		select "brand", sum("salesRub") as "revenue" from distributor.sales inner join distributor.item using("itemId")
		group by "brand"
		order by "revenue" desc 
		limit 3
	)
) / (select sum("salesRub") from distributor.sales) as "share"