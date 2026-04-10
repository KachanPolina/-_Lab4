def calculate_nights_total(number_of_nights, night_price):
    if number_of_nights <= 0 or night_price <= 0:
        return 0
    return number_of_nights * night_price


def add_city_tax(number_of_nights, night_price, city_tax):
    if calculate_nights_total(number_of_nights, night_price) <= 0:
        return 0
    return calculate_nights_total(number_of_nights, night_price) + city_tax


def main():
    number_of_nights = int(input("Введіть кількість ночей: "))
    night_price = int(input("Введіть ціну за ніч: "))
    city_tax = int(input("Введіть міський податок: "))
    hotel_accommodation_cost = add_city_tax(number_of_nights, night_price, city_tax)
    print(f"Ціна проживання в готелі становить: {hotel_accommodation_cost}")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
