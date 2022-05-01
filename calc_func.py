from datetime import datetime
import calendar

c = calendar.TextCalendar(calendar.MONDAY)

week_days = {
    1: 'Dushanba',
    2: 'Seshanba',
    3: 'Chorshanba',
    4: 'Payshanba',
    5: 'Juma',
    6: 'Shanba',
    7: 'Yakshanba',
}


async def calculate_bdays(message):
    birthday_date = [int(n) for n in message.text.split('.')]  # message = '30.09.2001'
    current_date = [int(n) for n in datetime.now().strftime('%d.%m.%Y').split('.')]
    if birthday_date[0] > 31 or birthday_date[1] > 12:
        raise Exception
    elif datetime(
            birthday_date[2], birthday_date[1], birthday_date[0]
    ) >= datetime(
        current_date[2], current_date[1], current_date[0]
    ):
        raise Exception
    date = birthday_date.copy()
    day = date[0]
    days = 0
    stopp = True
    while stopp:
        if date[1] > 12:
            date[2] += 1
            date[1] = 1

        for d in c.itermonthdays(date[2], date[1]):
            if d != 0:
                days += 1
                date[0] = d
                if date == current_date:
                    stopp = False
                    print('FINISH')
                    break
        date[1] += 1

    if (days - day) % 7 == 0:
        week = f"<b>{(days - day) / 7}</b> hafta, to'g'rirogi"
    else:
        week = f"<b>{int((days - day) / 7)}</b> hafta va {(days - day) % 7} kun, to'gr'irogi"

    if current_date[1] == 1:
        months = ((current_date[2] - birthday_date[2]) * 12) - (birthday_date[1])
    else:
        months = ((current_date[2] - birthday_date[2]) * 12) - (birthday_date[1]) + current_date[1]

    b_weekday = [d[1] + 1 for d in c.itermonthdays2(birthday_date[2], birthday_date[1]) if birthday_date[0] == d[0]]
    c_weekday = [d[1] + 1 for d in c.itermonthdays2(current_date[2], birthday_date[1]) if birthday_date[0] == d[0]]
    n_weekday = [d[1] + 1 for d in c.itermonthdays2(current_date[2] + 1, birthday_date[1]) if birthday_date[0] == d[0]]

    text = f"Tug'ilgan sanangiz: {'-'.join(list(map(str,birthday_date)))}\n" + \
           f"Bugungi sana: {'-'.join(list(map(str,current_date)))}\n\n" + \
           f"Sizni tug'ilganingizga:\n<b>{days - day}</b> kun, yani\n{week}\n<b>{months}</b> oy bo'ldi)\n\n" + \
           f"Siz <b>{round(months/12,2)}</b> yoshdasiz\n\nSiz <b>{week_days[b_weekday[0]]}</b> kuni tug'ilgansiz, " + \
           f"Bu yil sizning tug'ilgan kuningiz <b>{week_days[c_weekday[0]]}</b> kuni " + \
           f"va kelyotgan yili esa <b>{week_days[n_weekday[0]]}</b> kuniga to'g'ri keladi"

    return text
