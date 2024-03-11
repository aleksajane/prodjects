select "companyId","itemId", date_trunc('month',"dateId") as "date",
case
	when max("dateId")-min("dateId") = 1 then 'new'
	when max("dateId")-min("dateId") <= 2 and max("dateId")-min("dateId") > 1 then 'permanent'
	when max("dateId")-min("dateId") > 2 and max("dateId")-min("dateId") <= 4 then 'potentially lost'
	when max("dateId")-min("dateId") > 4 then 'lost'
end as status
from distributor.sales s 
group by "companyId","itemId", "date"