select "top", "brand", "year", "itemName" as "top_3" from 
(select brand, extract(year from "dateId") as "year", "itemName", row_number() over(partition by brand, extract(year from "dateId") order by sum("salesRub") desc) as "top" 
from distributor.sales inner join distributor.item using("itemId")
group by brand, "itemName", extract(year from "dateId"))
where "top" in (1, 2, 3)