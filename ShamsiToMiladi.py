def shamsi_To_Miladi(day,month,year):
    if day >= 11  and month >=10:
        year += 622
        print(f"your birthday is year {year}")
    else:
        year += 621
        print(f"your birthday is year {year}")
        

day = int(input("Please Enter your birthday: "))
month = int(input("Please Enter your month of birth: "))
year = int(input("Please Enter your year of birth: "))
shamsi_To_Miladi(day,month,year)