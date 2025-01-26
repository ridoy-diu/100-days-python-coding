def format_name(f, l):
    first = f.title()
    last = l.title() 
    return first+ " " +last

print(format_name("ridoy", "sazidul"))


# finding leap year

def leap_year(n):
    """find the leap year""" #docstrings
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
            else:
                return False
        else: 
            return True
    else:
        return False
    

print(leap_year(2000), leap_year(2100))