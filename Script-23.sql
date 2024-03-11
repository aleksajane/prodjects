select date_part('month', "dateId") as "month",  date_part('year', "dateId") as "year",
		sum("remains")/(sum("remains") + sum("freeRemains")) as "share"
from distributor.remains r 
group by "month", "year"