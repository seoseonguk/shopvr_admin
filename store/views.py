from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import TimeSales, Store, DailySales, NaverSearching
# Create your views here.
from selenium import webdriver
from time import sleep
import datetime
import os
from django.conf import settings
from .time_sales_crawler import get_daily_time_sales_for_all_store, get_token_kiosk
from .daily_sales_crawler import update,update_everything
from django.db.models import Sum
import csv




class DailySalesForAllStoreListView(ListView):
    model = DailySales
    template_name = "store/dailysales_all.html"

    def get_queryset(self):
        date = self.request.GET.get('datepickerforsales')
        try:
            dt = datetime.datetime.strptime(date,'%Y-%m')
        except:
            dt = datetime.datetime.now()
        daily_sales_q = DailySales.objects.filter(date__month=dt.month, date__year=dt.year).order_by('date').first()
        print(daily_sales_q)
        return DailySales.objects.filter(date__month=dt.month, date__year=dt.year).order_by('date')


class DailySalesListView(ListView):
    model = DailySales
    template_name = "store/dailysales_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        if self.request.GET.get('radGroupBtn1_1'):
            q = self.request.GET.get('radGroupBtn1_1')
        else:
            q = 'hd1'
        date = self.request.GET.get('datepickerforsales')
        try:
            dt = datetime.datetime.strptime(date,'%Y-%m')
        except:
            dt = datetime.datetime.now()
        self.store = get_object_or_404(Store, slug=q)
        context['dailysales_list'] = DailySales.objects.filter(store=self.store, date__month=dt.month, date__year=dt.year)
        context['aggregated_data'] = DailySales.objects.filter(store=self.store, date__month=dt.month, date__year=dt.year).aggregate(Sum('pos_cash_sales'),Sum('pos_card_sales'),Sum('kiosk_cash_sales'),Sum('kiosk_card_sales'),Sum('total_sales'))
        return context


class SCDailySalesListView(ListView):
    model = DailySales
    template_name = "store/dailysales_list_single_company.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        date = self.request.GET.get('datepickerforsales')
        try:
            dt = datetime.datetime.strptime(date,'%Y-%m')
        except:
            dt = datetime.datetime.now()
        self.store = get_object_or_404(Store, slug='sc')
        context['dailysales_list'] = DailySales.objects.filter(store=self.store, date__month=dt.month, date__year=dt.year)
        context['aggregated_data'] = DailySales.objects.filter(store=self.store, date__month=dt.month, date__year=dt.year).aggregate(Sum('pos_cash_sales'),Sum('pos_card_sales'),Sum('kiosk_cash_sales'),Sum('kiosk_card_sales'),Sum('total_sales'))
        return context

class BPDailySalesListView(ListView):
    model = DailySales
    template_name = "store/dailysales_list_single_company.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        date = self.request.GET.get('datepickerforsales')
        try:
            dt = datetime.datetime.strptime(date,'%Y-%m')
        except:
            dt = datetime.datetime.now()
        self.store = get_object_or_404(Store, slug='bp')
        context['dailysales_list'] = DailySales.objects.filter(store=self.store, date__month=dt.month, date__year=dt.year)
        context['aggregated_data'] = DailySales.objects.filter(store=self.store, date__month=dt.month, date__year=dt.year).aggregate(Sum('pos_cash_sales'),Sum('pos_card_sales'),Sum('kiosk_cash_sales'),Sum('kiosk_card_sales'),Sum('total_sales'))
        return context

class DailySalesAnalysisView(ListView):
    model = DailySales
    template_name = "store/dailysales_analysis.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        day_string = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

        if self.request.GET.get('radGroupBtn1_1'):
            q = self.request.GET.get('radGroupBtn1_1')
        else:
            q = 'hd1'
        date = self.request.GET.get('datepickerforsales')
        try:
            dt = datetime.datetime.strptime(date,'%Y-%m-%d')
        except:
            dt = datetime.datetime.now()
        self.store = get_object_or_404(Store, slug=q)
        print(q, dt)
        print(self.store)
        print(DailySales.objects.filter(
            store=self.store))
        context['dailysales_list'] = DailySales.objects.filter(
            store=self.store,
            weekday=day_string[dt.weekday()]).filter(
            date__lte=dt + datetime.timedelta(days=28),
            date__gte=dt + datetime.timedelta(days=-28))\
            .order_by("date")
        context['timesales_list'] = TimeSales.objects.filter(
            store=self.store,
            time__year=dt.year,
            time__month=dt.month,
            time__day=dt.day)
        context['naver_searching_list'] = NaverSearching.objects.filter(
            store=self.store.slug,
            date=dt)
        context['searched_date'] = dt
        print(context)
        return context

class TimeSalesListView(ListView):
    model = TimeSales
    def get_queryset(self):
        if self.request.GET.get('radGroupBtn1_1'):
            q = self.request.GET.get('radGroupBtn1_1')
        else:
            q = 'hd1'
        self.store = get_object_or_404(Store, slug=q)
        dt = datetime.datetime.now()
        return TimeSales.objects.filter(store=self.store, time__year=dt.year, time__month=dt.month, time__day=dt.day)


class NaverSearchingListView(ListView):
    model = NaverSearching
    def get_queryset(self):
        if self.request.GET.get('radGroupBtn1_1'):
            q = self.request.GET.get('radGroupBtn1_1')
        else:
            q = 'hd1'
        self.store = get_object_or_404(Store, slug=q).slug
        date = self.request.GET.get('datepickerforsales')
        try:
            dt = datetime.datetime.strptime(date,'%Y-%m-%d')
        except:
            dt = datetime.datetime.now()
        dt = datetime.datetime.now()
        return NaverSearching.objects.filter(store=self.store, date=dt)


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

    # update_everything(token, driver,driver_sh)
    update(token, driver, driver_sh)
    driver.close()
    driver_sh.close()

    return redirect('store:daily_sales_list')



def update_naver_crawling_data(request):
    store_list = ['hd1', 'hd2', 'sc', 'sw', 'bp', 'sh']
    for store in store_list:
        path_dir = os.path.join(settings.BASE_DIR,'sales_data/shopvr_'+store+'/naver_blog_share/')
        file_list = os.listdir(path_dir)
        for file in file_list:
            if ".csv" in file:
                file_add = os.path.join(path_dir,file)
                with open(file_add) as f:
                    date = file.replace('.csv','')
                    reader = csv.reader(f)
                    header = next(reader)
                    print(header)
                    for row in reader:
                        store = store
                        keyword = row[0]
                        occupied = row[2] + ' , ' +row[4] + ' , '  + row[6] + ' , '  + row[8] + ' , '  + row[10]
                        percent_first_page = row[1]
                        percent_for_all = (float(row[1]) + float(row[3]) + float(row[5]) + float(row[7]) + float(row[9]))/5
                        print(date,keyword,occupied,percent_first_page,percent_for_all)
                        NaverSearching.objects.get_or_create(
                            store = store,
                            date = date,
                            keyword= keyword,
                            occupied= occupied,
                            percent_first_page = percent_first_page,
                            percent_for_all = percent_for_all
                        )
    return redirect('store:naver_blog_list')
