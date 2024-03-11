select "fullname", "brand", sum("salesRub") as "total_sales" from distributor.sales 
inner join distributor.salesmanager s using("salesManagerId")
inner join distributor.item i using("itemId")
group by "fullname", "brand"
order by "fullname", "brand"