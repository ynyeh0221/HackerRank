select COUNTRY.Continent, floor(avg(CITY.Population)) from city inner join country on CITY.CountryCode = COUNTRY.Code group by COUNTRY.Continent;
