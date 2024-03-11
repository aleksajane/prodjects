select "branchName", date_trunc('month', "dateId") as "date", "category" from distributor.sales s 
inner join distributor.branch b using("branchId")  
inner join distributor.item i using("itemId")
group by "branchName", "date", "category"
order by "branchName", "date", "category"