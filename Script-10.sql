select "branchId" as "branch", date_trunc('month', "dateId")::date as "date", "brand" as "brand", round(sum("salesRub")) as "revenue" from distributor.sales inner join distributor.item using("itemId")
group by "branchId", date_trunc('month', "dateId"), "brand"
order by "branch", "date", "brand"