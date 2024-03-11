select "branchName", "year", "month",sum("summ"*"basePrice") as "cost", "currency" from(
	select distinct "branchName", "year", "month", "summ" from(
		select extract(year from "dateId") as "year", extract(month from "dateId") as "month", "branchId" from distributor.sales
	)
	inner join(
	select sum("remains") as "summ", extract(year from "dateId") as "year", extract(month from "dateId") as "month", "branchId" from distributor.remains
	group by "month", "year", "branchId"
	) 
	using("year","month", "branchId") inner join distributor.branch using("branchId"))
inner join 
(select "monthId" as "month", "yearId" as "year" , "basePrice", "currency" from distributor.ddp
where "basePrice" is not null)
using("month", "year")
where "currency" is not null
group by "branchName", "year", "month", "currency"