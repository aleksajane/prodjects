select * from distributor.sales inner join distributor.specification using("itemId") inner join distributor.item using("itemId")
where category = 'Обои'