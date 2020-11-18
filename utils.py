import pandas as pd
import calendar
import ast
from datetime import datetime, timedelta


def get_str_of_list(values):
    list_vals = ast.literal_eval(values)
    return ', '.join(list_vals)


def get_day_of_week():
    datetime.today().weekday()


def is_weekday():
    day_of_week = datetime.today().weekday()   # 0 = Monday, 6 = Sunday
    if day_of_week < 5:
        return True


def is_weekend():
    day_of_week = datetime.today().weekday()  # 0 = Monday, 6 = Sunday
    if day_of_week >= 5:
        return True


def is_monday():
    return datetime.today().weekday() == 0


def get_day_of_week_eng(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d").date()
    return calendar.day_name[dt.weekday()][:3]


def get_day(num_days_back: int):
    today = datetime.now()
    target_day = today - timedelta(num_days_back)
    return datetime.strftime(target_day, '%Y-%m-%d')


def get_yesterday():
    return datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')


def get_today():
    today = datetime.now()
    tdy = today.strftime("%Y-%m-%d %H:%M:%S")
    # tdy = today.strftime("%Y_%b_%d")
    print("TODAY =", tdy)
    return tdy


def lookup(s):
    """
    This is an extremely fast approach to datetime parsing.
    For large data, the same dates are often repeated. Rather than
    re-parse these, we store all unique dates, parse them, and
    use a lookup to convert all dates.
    """
    dates = {date:pd.to_datetime(date) for date in s.unique()}
    return s.map(dates)


def create_tsv_row(list_of_str):
    result = ""
    for value in list_of_str:
        result += str(value) + '\t'
    return result[:-2] + '\n'



# def create_tsv_files_with_header(tdy, total_num_restaurants):
#     fp = '../files/' + tdy + '_' + str(total_num_restaurants) + '_'
#     with open(fp+'region.tsv', 'w+', encoding='utf-8') as f:
#         f.write(Region.get_region_tsv_header())
#     with open(fp+'restaurant.tsv', 'w+', encoding='utf-8') as f:
#         f.write(Restaurant.get_restaurant_tsv_header())
#     with open(fp+'item.tsv', 'w+', encoding='utf-8') as f:
#         f.write(Item.get_item_tsv_header())


def write_tsv(tdy, total_num_restaurants, region):
    fp = '../files/' + tdy + '_' + str(total_num_restaurants) + '_'
    write_tsv_item(fp+'item.tsv', region)

    fp_completed_regions = '../files/' + tdy + '_' + str(total_num_restaurants) + '_completed_regions.csv'
    with open(fp_completed_regions, 'a+', encoding='utf-8') as f:
        f.write(str(region.id) + '. ' + str(region.name) + ' (' + str(len(region.restaurants)) + '), ')


def write_tsv_item(fp, region):
    menu_tsv_full = ""
    for restaurant in region.restaurants:
        menu_tsv_full += restaurant.get_items_tsv_full()
    with open(fp, "a+", encoding='utf-8') as f:
        f.write(menu_tsv_full)


# if __name__ == '__main__':
#     get_list_of_categories()
