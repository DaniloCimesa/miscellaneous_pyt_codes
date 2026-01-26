
def is_leap_year(year):
    """Determine if a given year is a leap year."""
    return(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))


def days_in_month(year,month):
    """Return the number of days in a given month of a given year"""
    
    if month<1 or month>12:
        return None
    
    days_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    
    if is_leap_year(year) and month==2:
        return 29
    else:
        return days_in_month[month]
    

def day_of_year(year, month, day):
    """Return the day of the year for a given date"""
    
    if days_in_month(year, month)is None:
        return None
    
    if day<1 or day>days_in_month(year, month):
        return None
    
    day_count = 0
    for m in range(1,month):
        day_count+=days_in_month(year,m)
    
    day_count+=day
    
    return day_count

print(day_of_year(2026,1,26))