--/*
select fullname, "branchName", "month"::date, round("total") --18
from( 
		select fullname, "branchName" , date_trunc('month', "dateId") as "month", 
		sum("salesRub") as "total", 
		row_number() over (partition by "branchName", date_trunc('month', "dateId") order by sum("salesRub") desc  )
		from distributor.sales s 
		inner join distributor.branch b using("branchId")
		inner join distributor.salesmanager s2 using("salesManagerId")
		where "branchName" notnull and fullname notnull
		group by fullname, "branchName", "month"
		order by "branchName", "month") as t
where row_number <3
-- */
 /*
select fullname, "branchName", "year"::date, round("total")
from( 
		select fullname, "branchName" , date_trunc('year', "dateId") as "year", 
		sum("salesRub") as "total", 
		row_number() over (partition by "branchName", date_trunc('year', "dateId") order by sum("salesRub") desc  )
		from distributor.sales s 
		inner join distributor.branch b using("branchId")
		inner join distributor.salesmanager s2 using("salesManagerId")
		where "branchName" notnull and fullname notnull
		group by fullname, "branchName", "year"
		order by "branchName", "year") as t
where row_number <3
*/