from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import TimeSales, Store, DailySales, NaverSearching
import datetime
from django.db.models import Sum
from django.conf import settings
import boto3


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
            dt = datetime.datetime.strptime(date,'%D/%M/%Y')
        except:
            dt = datetime.datetime.now()
        self.store = get_object_or_404(Store, slug=q)

        bucket_name= settings.AWS_STORAGE_BUCKET_NAME
        region = settings.AWS_S3_REGION_NAME
        session = boto3.session.Session(region_name=region)
        s3 = session.client('s3', config=boto3.session.Config(signature_version='s3v4'))
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': bucket_name,
                'Key': 'data/shopvr_'+q+'/'+q+'-'+ dt.strftime("%Y-%m")+'.csv'
            }
        )

        print(url)
        context['download_link'] = url

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
            dt = datetime.datetime.strptime(date,'%d/%m/%Y')
        except:
            dt = datetime.datetime.now()
        self.store = get_object_or_404(Store, slug=q)
        print(q, dt, date)

        bucket_name= settings.AWS_STORAGE_BUCKET_NAME


        region = settings.AWS_S3_REGION_NAME
        session = boto3.session.Session(region_name=region)
        s3 = session.client('s3', config=boto3.session.Config(signature_version='s3v4'))
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': bucket_name,
                'Key': 'data/shopvr_'+q+'/time_sale/'+dt.strftime("%Y-%m")+"/"+q+'_timesale_'+ dt.strftime("%Y-%m-%d")+'.csv'
            }
        )

        print(url)
        context['download_link'] = url
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
        return context



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
            dt = datetime.datetime.strptime(date,'%D/%M/%Y')
        except:
            dt = datetime.datetime.now()
        dt = datetime.datetime.now()
        return NaverSearching.objects.filter(store=self.store, date=dt)


class SCDailySalesListView(ListView):
    model = DailySales
    template_name = "store/dailysales_list_single_company.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        date = self.request.GET.get('datepickerforsales')
        try:
            dt = datetime.datetime.strptime(date,'%D/%M/%Y')
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
            dt = datetime.datetime.strptime(date,'%D/%M/%Y')
        except:
            dt = datetime.datetime.now()
        self.store = get_object_or_404(Store, slug='bp')
        context['dailysales_list'] = DailySales.objects.filter(store=self.store, date__month=dt.month, date__year=dt.year)
        context['aggregated_data'] = DailySales.objects.filter(store=self.store, date__month=dt.month, date__year=dt.year).aggregate(Sum('pos_cash_sales'),Sum('pos_card_sales'),Sum('kiosk_cash_sales'),Sum('kiosk_card_sales'),Sum('total_sales'))
        return context
