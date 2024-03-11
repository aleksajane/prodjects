select count(*) as "Кол-во неликвидного товара", 
(select count(*) from distributor.item) as "Общее кол-во товара" 
from distributor.item left join (select "itemId", max("dateId") as max_date 
from distributor.sales group by "itemId") using("itemId")
where '2014-01-01'::date - max_date > 180 or max_date is null