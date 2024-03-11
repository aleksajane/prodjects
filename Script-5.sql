select 
	(select sum("total_salesRub") as "four_sum" from(
		select "branchName", date_trunc('month', "dateId")::date as "date", "brand", round(sum("salesRub")) as "total_salesRub" from distributor.sales s 
		inner join distributor.branch b using("branchId")
		inner join distributor.item i using("itemId")
		group by "branchName", "date", "brand"
	order by "branchName", "date", "brand"
		)	 
	)
	-
	(select sum("total_salesRub") as "two_sum" from(
		select "branchId", date_trunc('month', "dateId")::date as "date", round(sum("salesRub")) as "total_salesRub" from distributor.sales s2  
		group by "branchId", "date"
		order by "branchId", "date"
		)
	)
as "difference"
