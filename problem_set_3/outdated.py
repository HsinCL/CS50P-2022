def main():

    calender = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date = input("Date: ")
        if '/' in date:
            month, day, year = date.split('/')
        else:
            month, day, year = date.split(' ')
            day = day[:-1]
            if month not in calender:
                continue
            else:
                month = calender.index(month) + 1

        
        if print_date(year, month, day):
            break


def print_date(year, month, day):
    month = int(month)
    day = int(day)
    if (1 <= month <= 12) and (1<= day <= 31):
        print(f"{year:04}-{month:02}-{day:02}")
        return True
    else:
        return False


main()