select extract('year' from "dateId") as "year", "fullname", count("companyId") from distributor.sales s
inner join distributor.salesmanager using("salesManagerId")
group by "companyId", "year", "fullname"
