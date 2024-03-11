select "branchName", date_trunc('month', "dateId")::date as "date", "brand", round(sum("salesRub")) from distributor.sales s 
inner join distributor.branch b using("branchId")
inner join distributor.item i using("itemId")
group by "branchName", "date", "brand"
order by "branchName", "date", "brand"