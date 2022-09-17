

# Transform minutes into years and days

num_of_minutes=3456789
min_to_hour=60
hour_to_day=24
day_to_year=365

years=num_of_minutes//min_to_hour//hour_to_day//day_to_year
days=num_of_minutes//min_to_hour//hour_to_day%day_to_year

print(3456789, "minutes equals to", years,"years and", days, "days")





















