from bs4 import BeautifulSoup
import requests
from selenium.webdriver.support.ui import Select
import datetime
import pytz
from store.models import TimeSales, Store
from time import sleep
store_list = ['hd1','hd2','sc','sw','bp','sh']
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

# coding: utf-8

# # POS 크롤러

# In[39]:


def get_daily_time_sales_pos(driver_time, driver_time_sh, store, year, month, day):
    if store == 'sh':
        d = driver_time_sh
    else:
        d = driver_time
    date = datetime.date((int(year)+1900), month, day).strftime('%Y%m%d')
    d.get('http://asp.posbank.co.kr/a23812/PES/Pes13_Date_Report.php')
    select = Select(d.find_element_by_name("searRCT_CODE"))
    select.select_by_value(str(store_dic[store]))
    d_start = d.find_element_by_name("start_date")
    d_start.clear()
    d_start.send_keys(date)
    d_end = d.find_element_by_name("end_date")
    d_end.clear()
    d_end.send_keys(date)
    d.find_element_by_xpath('//*[@id="layout_right"]/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td[3]/input').click()
    html = d.page_source
    soup = BeautifulSoup(html,'html.parser').select('.page_inner2')

    sales_in_time_dic = {}
    for tr_tag in soup[0].select('tr'):
        sales_in_time = {}
        time = tr_tag.select('td')[0].text.strip()
        if time:
            sales_in_time['time'] = time
            sales_in_time['sale'] = tr_tag.select('td')[1].text.replace(',','').strip()
            if sales_in_time['sale'] == '':
                sales_in_time['sale'] = 0
            sales_in_time['count'] = tr_tag.select('td')[5].text.replace(',','').strip()[:-3]
            if sales_in_time['count'] == '':
                sales_in_time['count'] = 0
            sales_in_time_dic[time] = sales_in_time
    return sales_in_time_dic


# ## Kiosk 크롤러

# In[40]:


def get_token_kiosk():
    url = 'http://api-kms.nicetcm.co.kr/api/login'
    user_json = {
        'userId':"bluebake",
        'userSecret':"123456"
    }
    headers = {
        'Authorization':'Basic Mjg0MWUxM2QtNGE2Yi00ZjJlLTk4NWItYTdiNTAxMmE4MThlOkcoaHsybkY/NUJiPmwrKlo7NDJdQjY2KC84en1ATkoy',
        'Referer':'https://m-kms.nicetcm.co.kr/',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    auth_response = requests.post(url, json = user_json, headers=headers).json()
    return auth_response['accessToken']

def get_daily_time_sales_kiosk(token, store,year,month,day):
    headers = {
        'Authorization':'Bearer '+ token,
        'Referer':'http://kms.nicetcm.co.kr/',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    date = datetime.date(year,month,day)
    params = {
        'headOfficeId':'117',
        'franchiseId': store_dic_kiosk[store],
        'searchDate':date.strftime('%y-%m-%d'),
    }
    sales_json = requests.get('http://api-kms.nicetcm.co.kr/api/sales/by-hour?', params=params, headers= headers).json()
    sales_in_time_dic = {}

    for time_sale in sales_json['salesPerHour']:
        sales_in_time = {}
        time = time_sale['SALE_HOUR'][0:-1].strip()
        sales_in_time['time'] = time
        sales_in_time['sale'] = time_sale['CARD_AMOUNT'] + time_sale['CASH_AMOUNT'] + time_sale['CASH_RECEIPT_AMOUNT']
        sales_in_time['count'] = time_sale['CARD_COUNT'] + time_sale['CASH_COUNT'] + time_sale['CASH_RECEIPT_COUNT']
        sales_in_time_dic[time] = sales_in_time
    print(sales_in_time_dic)
    return sales_in_time_dic

# In[38]:


def get_daily_time_sales_for_all_store(token, driver_time, driver_time_sh, year,month,day):
    for store in store_list:
        get_daily_time_sales(token, driver_time, driver_time_sh, store, year,month,day)


# ## DB 저장 함수

# In[34]:


def get_daily_time_sales(token, driver_time, driver_time_sh, store, year, month, day):
    p_sales= {}
    k_sales= {}
    # try:
    store_id = Store.objects.get(slug=store)
    keys=['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
    if store in store_dic_kiosk:
        k_sales = get_daily_time_sales_kiosk(token, store,year,month,day)
    if store in store_dic:
        p_sales = get_daily_time_sales_pos(driver_time, driver_time_sh, store,year,month,day)
    for key in keys:
        try:
            k_sales[key]
        except:
            k_sales[key] = {'sale':0,'count':0,'time':key}
        try:
            p_sales[key]
        except:
            p_sales[key] = {'sale':0,'count':0,'time':key}
        dt = datetime.datetime(year, month, day, int(key), tzinfo=pytz.UTC)
        t_sales, is_exist = TimeSales.objects.get_or_create(time=dt, store=store_id)
        t_sales.sales = int(k_sales[key]['sale'])+int(p_sales[key]['sale'])
        t_sales.count = int(k_sales[key]['count'])+int(p_sales[key]['count'])
        print(t_sales)
        t_sales.save()
# except:
#     print("There is no store for sales data")
