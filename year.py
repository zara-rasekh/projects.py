day=int(input('please enter a day: '))
month=int(input('please enter a month: '))
year=int(input('please enter a year: '))

def myfunc(year,month,day):
    if month<10 or month<10 and day<=10:
        n_year=year+621

    else:
        n_year=year+622   
    print(f'the year is: {n_year}')

myfunc(year,month,day)   