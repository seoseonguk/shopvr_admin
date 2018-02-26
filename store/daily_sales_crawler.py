from store.models import DailySales, Store
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlencode
import datetime

store_list = ['hd1', 'hd2', 'sc', 'sw', 'bp', 'sh']
store_dic = {
    'hd1': 1000,
    'hd2': 1001,
    'sc': 1002,
    'sw': 1003,
    'sh': 1001
}
store_dic_kiosk = {
    'hd1': '107',
    'bp': '118'
}

def get_monthly_sales_for_pos(driver, driver_sh, store, year, month):
    month = int(month)
    month = '{0:02d}'.format(month)
    params = {
        'PGIDX': '2',  # 일간 매출 선택
        'searYY': year,  # 선택 년도
        'searMM': month,  # 선택 월
        'searRCT_CODE': store_dic[store],  # 선택 매장
    }
    q = urlencode(params)
    if store == 'sh':
        driver_sh.get(('http://m.posbank.co.kr/content_frame.html?' + q))
        html = driver_sh.page_source
    else:
        driver.get(('http://m.posbank.co.kr/content_frame.html?' + q))
        html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser').select('.grid_table tbody')[0]
    sales_list = {}
    date = 1
    for tr_tag in soup.select('tr'):
        try:
            td_temp = tr_tag.select('td')
            sale_dic = {}
            sale_dic['date'] = (str(year) + '-' + str(month) + '-' + '{0:02d}'.format(date))
            #             sale_dic['p_total_sales'] = td_temp[1].text.replace(',','')
            sale_dic['p_cash'] = td_temp[2].text.replace(',', '')
            sale_dic['p_card'] = td_temp[3].text.replace(',', '')
            sales_list[sale_dic['date']] = sale_dic
            date = date + 1
        except:
            print("No Data")
    return sales_list


# Kiosk

def get_token_kiosk():
    url = 'http://api-kms.nicetcm.co.kr/api/login'
    user_json = {
        'userId': "bluebake",
        'userSecret': "123456"
    }
    headers = {
        'Authorization': 'Basic Mjg0MWUxM2QtNGE2Yi00ZjJlLTk4NWItYTdiNTAxMmE4MThlOkcoaHsybkY/NUJiPmwrKlo7NDJdQjY2KC84en1ATkoy',
        'Referer': 'https://m-kms.nicetcm.co.kr/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    auth_response = requests.post(url, json=user_json, headers=headers).json()
    return auth_response['accessToken']


def get_monthly_sales_for_kiosk(token, store, year, month):
    headers = {
        'Authorization': 'Bearer ' + token,
        'Referer': 'http://kms.nicetcm.co.kr/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    start_date = datetime.date(year, month, 1)
    if month == 12:
        end_date = datetime.date(year, month, 31)
    else:
        end_date = datetime.date(year, month + 1, 1) + datetime.timedelta(-1)
    params = {
        'headOfficeId': '117',
        'franchiseId': store_dic_kiosk[store],
        'startDate': start_date.strftime('%y-%m-%d'),
        'endDate': end_date.strftime('%y-%m-%d')
    }
    sales_json = requests.get('http://api-kms.nicetcm.co.kr/api/sales/by-day?', params=params, headers=headers).json()
    sales_list = {}
    sale_dic = {}
    for daily_sale in sales_json['sales']:
        if daily_sale['SALE_DATE'] in sales_list:
            sale_dic = sales_list[daily_sale['SALE_DATE']]
            sale_dic['k_card'] = sale_dic['k_card'] + daily_sale['CARD_AMOUNT']
            sale_dic['k_cash'] = sale_dic['k_cash'] + daily_sale['CASH_AMOUNT']
        else:
            sale_dic = {}
            sale_dic['date'] = daily_sale['SALE_DATE']
            sale_dic['k_card'] = daily_sale['CARD_AMOUNT']
            sale_dic['k_cash'] = daily_sale['CASH_AMOUNT']
        sales_list[daily_sale['SALE_DATE']] = sale_dic

    return sales_list


# 통합 계산 코드

def get_monthly_sales(token, driver, driver_sh, store, year, month):
    day_string = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    store_id = Store.objects.get(slug=store)
    if store in store_dic_kiosk:
        k_sales = get_monthly_sales_for_kiosk(token, store, year, month)
        keys = k_sales.keys()
    if store in store_dic:
        p_sales = get_monthly_sales_for_pos(driver, driver_sh, store, year, month)
        keys = p_sales.keys()
    for key in keys:
        date = datetime.datetime.strptime(key, "%Y-%m-%d")
        d_sales, is_exist = DailySales.objects.get_or_create(store=store_id, date=date)
        weekday = day_string[date.weekday()]
        try:
            k_card = int(k_sales[key]['k_card'])
            k_cash = int(k_sales[key]['k_cash'])
        except:
            k_card = 0
            k_cash = 0
        try:
            p_card = int(p_sales[key]['p_card'])
            p_cash = int(p_sales[key]['p_cash'])
        except:
            p_card = 0
            p_cash = 0
        total_sales = p_card + p_cash + k_card + k_cash

        d_sales.pos_cash_sales = p_cash
        d_sales.pos_card_sales = p_card
        d_sales.kiosk_cash_sales = k_cash
        d_sales.kiosk_cash_saels = k_card
        d_sales.total_sales = total_sales
        d_sales.weekday = weekday
        d_sales.save()

        print(d_sales)
## 계산용 함수

def get_monthly_sales_for_all_store(token, driver, driver_sh, year, month):
    for store in store_list:
        total_sales_con_dict = {}
        get_monthly_sales(token, driver, driver_sh, store, year, month)


def update_all_term_sales(token, driver, driver_sh, store):
    dt = datetime.datetime.now()
    open_year = {
        'hd1': 2016,
        'hd2': 2017,
        'sc': 2017,
        'sw': 2017,
        'bp': 2017,
        'sh': 2017
    }
    open_month = {
        'hd1': 11,
        'hd2': 4,
        'sc': 7,
        'sw': 11,
        'bp': 12,
        'sh': 7
    }

    for y in range(open_year[store], (dt.year + 1)):
        if y == open_year[store]:
            for m in range(open_month[store], 13):
                get_monthly_sales(token, driver, driver_sh, store, y, m)
        elif y == dt.year:
            for m in range(1, dt.month + 1):
                get_monthly_sales(token, driver, driver_sh, store, y, m)
        else:
            for m in range(1, 13):
                get_monthly_sales(token, driver, driver_sh, store, y, m)



def update_everything(token, driver, driver_sh):
    for store in store_list:
        update_all_term_sales(token, driver, driver_sh, store)
    print('finished')


def update(token, driver, driver_sh):
    dt = datetime.datetime.now()
    get_monthly_sales_for_all_store(token, driver, driver_sh, dt.year, dt.month)
    print('finished')


def get_monthly_sales(token, driver, driver_sh, store, year, month):
    day_string = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    store_id = Store.objects.get(slug=store)
    if store in store_dic_kiosk:
        k_sales = get_monthly_sales_for_kiosk(token, store, year, month)
        keys = k_sales.keys()
    if store in store_dic:
        p_sales = get_monthly_sales_for_pos(driver, driver_sh, store, year, month)
        keys = p_sales.keys()
    for key in keys:
        date = datetime.datetime.strptime(key, "%Y-%m-%d")
        d_sales, is_exist = DailySales.objects.get_or_create(store=store_id, date=date)
        weekday = day_string[date.weekday()]
        try:
            k_card = int(k_sales[key]['k_card'])
            k_cash = int(k_sales[key]['k_cash'])
        except:
            k_card = 0
            k_cash = 0
        try:
            p_card = int(p_sales[key]['p_card'])
            p_cash = int(p_sales[key]['p_cash'])
        except:
            p_card = 0
            p_cash = 0
        total_sales = p_card + p_cash + k_card + k_cash

        d_sales.pos_cash_sales = p_cash
        d_sales.pos_card_sales = p_card
        d_sales.kiosk_cash_sales = k_cash
        d_sales.kiosk_card_sales = k_card
        d_sales.total_sales = total_sales
        d_sales.weekday = weekday
        d_sales.save()

        print(d_sales)