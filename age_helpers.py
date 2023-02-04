import datetime

def get_winery_age():
    today = datetime.datetime.now()
    return str((today.year - 1920))
    
  
def get_winery_age_form(age: str):
    if age.endswith(tuple([str(a) for a in range(11, 15)])):
        return 'лет'
    elif age.endswith('1'):
        return 'год'
    elif age.endswith(tuple('234')):
        return 'года'
    else:
        return 'лет'
        