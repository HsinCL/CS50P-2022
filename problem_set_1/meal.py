def main():
    t = input("What time is it? ")
    # string to float
    t = convert(t)
    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")
    else:
        return 0


def convert(time):
    hr_min = time.split(':')
    return float(int(hr_min[0]) + int(hr_min[1])/60)


if __name__ == "__main__":
    main()