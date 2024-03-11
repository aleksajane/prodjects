select "branchId", date_trunc('month', "dateId")::date as "date", round(sum("salesRub")) as "total_salesRub" from distributor.sales s2  
group by "branchId", "date"
order by "branchId", "date"