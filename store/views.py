from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from .models import TimeSales, Store, DailySales
# Create your views here.
from selenium import webdriver
from time import sleep
import datetime
import os
from django.conf import settings
from .time_sales_crawler import get_daily_time_sales_for_all_store, get_token_kiosk
from .daily_sales_crawler import update


class DailySalesListView(ListView):
    model = DailySales

    def get_queryset(self):
        if self.request.GET.get('radGroupBtn1_1'):
            q = self.request.GET.get('radGroupBtn1_1')
        else:
            q = 'hd1'
        self.store = get_object_or_404(Store, slug=q)
        dt = datetime.datetime.now()
        return DailySales.objects.filter(store=self.store, date__month=dt.month)

class TimeSalesListView(ListView):
    model = TimeSales

    def get_queryset(self):
        if self.request.GET.get('radGroupBtn1_1'):
            q = self.request.GET.get('radGroupBtn1_1')
        else:
            q = 'hd1'
        self.store = get_object_or_404(Store, slug=q)
        dt = datetime.datetime.now()
        return TimeSales.objects.filter(store=self.store, time__day=dt.day)



def update_time_sales(request):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    # if settings.DEBUG == True:
    driver_time = webdriver.Chrome(os.path.join(settings.BASE_DIR,'chromedriver'),chrome_options=options)
    # else:
    #     driver_time = webdriver.Chrome(os.path.join(settings.BASE_DIR,'chromedriver_linux'),chrome_options=options)
    driver_time.implicitly_wait(3)
    driver_time.get('http://asp.posbank.co.kr/')
    driver_time.find_element_by_name('c_id').send_keys('bake2673')
    driver_time.find_element_by_name('id').send_keys('10000000')
    driver_time.find_element_by_name('passwd').send_keys('bake0605')
    driver_time.find_element_by_xpath('//*[@id="vtab"]/div[1]/div[1]/form/div[3]/input[2]').click()
    sleep(0.5)
    print("POS CHROME OPEN _ TIME _ SALES _ HDSCSW")
    # if settings.DEBUG == True:
    driver_time_sh = webdriver.Chrome(os.path.join(settings.BASE_DIR,'chromedriver'),chrome_options=options)
    # else:
    # driver_time_sh = webdriver.Chrome(os.path.join(settings.BASE_DIR,'chromedriver_linux'),chrome_options=options)
    driver_time_sh.implicitly_wait(3)
    driver_time_sh.get('http://asp.posbank.co.kr/')
    driver_time_sh.find_element_by_name('c_id').send_keys('h00871')
    driver_time_sh.find_element_by_name('id').send_keys('10010000')
    driver_time_sh.find_element_by_name('passwd').send_keys('sh2242')
    driver_time_sh.find_element_by_xpath('//*[@id="vtab"]/div[1]/div[1]/form/div[3]/input[2]').click()
    sleep(0.5)
    print("POS CHROME OPEN _ TIME _ SALES _ SH")

    """
    여기까지는 크롤링을 위한 기본 로그인 작업
    """

    token = get_token_kiosk()
    print("GET TOKEN FOR KIOSK")



    dt = datetime.datetime.now()
    get_daily_time_sales_for_all_store(token, driver_time, driver_time_sh, dt.year,dt.month,dt.day)



    driver_time.close()
    driver_time_sh.close()
    print("CLOSED ALL CHROME")

    return redirect('store:time_sales_list')


def update_daily_sales(request):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    driver = webdriver.Chrome('/Users/seonguk-mac/chromedriver', chrome_options=options)
    driver.implicitly_wait(3)
    driver.get('http://m.posbank.co.kr/')
    driver.find_element_by_name('c_id').send_keys('bake2673')
    driver.find_element_by_name('id').send_keys('10000000')
    driver.find_element_by_name('passwd').send_keys('bake0605')
    driver.find_element_by_class_name('button').click()
    sleep(0.5)
    print("POS CHROME OPEN _ SALES _ HDSCSW")
    driver_sh = webdriver.Chrome('/Users/seonguk-mac/chromedriver', chrome_options=options)
    driver_sh.implicitly_wait(3)
    driver_sh.get('http://m.posbank.co.kr/')
    driver_sh.find_element_by_name('c_id').send_keys('h00871')
    driver_sh.find_element_by_name('id').send_keys('10010000')
    driver_sh.find_element_by_name('passwd').send_keys('sh2242')
    driver_sh.find_element_by_class_name('button').click()
    sleep(0.5)
    print("POS CHROME OPEN _ SALES _ SH")

    token = get_token_kiosk()
    print("GET TOKEN FOR KIOSK")

    update(token, driver, driver_sh)
    driver.close()
    driver_sh.close()

    return redirect('store:daily_sales_list')
