import QuantLib as ql

calendar = ql. SouthKorea()

# 1. fixing date
fixing_date = ql.Date(1, 1, 2021)
today = ql.Date(2, 1, 2024)

print(calendar.adjust(fixing_date, ql.Preceding))
print(calendar.adjust(today))

days = calendar.businessDaysBetween(calendar.adjust(fixing_date, ql.Preceding), today)

print(days)
print(calendar.advance(today, -days, ql.Days))

print(calendar.adjust(fixing_date, ql.Preceding) - calendar.advance(today, -days, ql.Days))
# print(calendar.advance(today, -(days+1), ql.Days, ql.Preceding))