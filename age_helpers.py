import datetime

def get_winery_age():
    today = datetime.datetime.now()
    foundation_year = datetime.datetime(year=1920, month=1, day=1)
    return str((today - foundation_year).days // 365)
    
  
def get_winery_age_form(age: str):
    if age.endswith(tuple([str(a) for a in range(11, 15)])):
        return 'лет'
    elif age.endswith('1'):
        return 'год'
    elif age.endswith(tuple('234')):
        return 'года'
    else:
        return 'лет'
        
        
    if str(age).endswith(tuple([str(a) for a in range(11, 15)])):
        print(f'{i} лет')
    elif str(age).endswith('1'):
        print(f'{i} год')
    elif str(age).endswith(tuple('234')):
        print(f'{i} года')
    else:
        print(f'{i} лет')
        