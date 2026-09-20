from datetime import datetime

# Define the zodiac sign ranges
zodiac_signs = {
    'Capricorn': ((1, 1), (1, 19)),
    'Aquarius': ((1, 20), (2, 18)),
    'Pisces': ((2, 19), (3, 20)),
    'Aries': ((3, 21), (4, 19)),
    'Taurus': ((4, 20), (5, 20)),
    'Gemini': ((5, 21), (6, 20)),
    'Cancer': ((6, 21), (7, 22)),
    'Leo': ((7, 23), (8, 22)),
    'Virgo': ((8, 23), (9, 22)),
    'Libra': ((9, 23), (10, 22)),
    'Scorpio': ((10, 23), (11, 21)),
    'Sagittarius': ((11, 22), (12, 21)),
    'Capricorn': ((12, 22), (12, 31)),
}

def get_zodiac_sign(day, month):
    for sign, ((start_month, start_day), (end_month, end_day)) in zodiac_signs.items():
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            return sign
    return None

# Get the user's birthdate
birthdate_str = input("Enter your birthdate (MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%m-%d")
day = birthdate.day
month = birthdate.month

# Determine the zodiac sign
zodiac_sign = get_zodiac_sign(day, month)
if zodiac_sign:
    print(f"Your zodiac sign is {zodiac_sign}.")
else:
    print("Invalid date. Please enter a valid birthdate in MM-DD format.")
