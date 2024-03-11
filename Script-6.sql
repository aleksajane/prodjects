select rank() over(order by sum("salesRub") desc), "brand", round(sum("salesRub")) as "total_sales" from distributor.sales inner join distributor.item using("itemId")
where extract(year from "dateId") = 2013
group by "brand"
limit 3