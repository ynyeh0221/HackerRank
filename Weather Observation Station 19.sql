select round(sqrt(abs(min(long_w) - min(lat_n)) * abs(min(long_w) - min(lat_n)) + abs(max(long_w) - max(lat_n)) * abs(max(long_w) - max(lat_n))),4) from station;
