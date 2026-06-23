# Write your MySQL query statement below
Select name as Customers
from Customers
Left Join Orders on Customers.id = Orders.customerId
where Orders.customerId is NULL;