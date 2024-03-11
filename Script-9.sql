select "Год", "Выручка" - "Издержки" as "Транзакционная выручка" from (select extract(year from "dateId") as "Год", sum("salesRub") as "Выручка" from sales
group by extract(year from "dateId"))
left join
(select "yearId" as "Год", sum("basePrice" * value) as "Издержки" from ddp inner join currency on ddp."monthId" = extract(month from currency."dateId") and ddp."yearId" = extract(year from currency."dateId") and extract(day from currency."dateId") = 28 and ddp.currency = currency.currency
group by "yearId") using("Год")