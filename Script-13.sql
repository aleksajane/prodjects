select "top", "brand", "itemName" as "top_item" from (select "brand", "itemName", row_number() over(partition by "brand" order by sum("salesRub") desc) as "top" 
from distributor.sales inner join distributor.item using("itemId")
group by brand, "itemName")
where "top" in (1, 2, 3)