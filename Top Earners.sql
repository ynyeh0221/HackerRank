select (salary * months) as e, count(*) from employee group by e having e = max(salary * months) order by e desc limit 1;
