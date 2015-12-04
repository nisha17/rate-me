from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import CreateView
from django.db.models import Avg
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
import pdb

from .models import *
from .forms import  RatingForm, LocalityFilterForm, BrokerFilterForm




# Create your views here.
class IndexView(generic.ListView):
    template_name = 'brokerhome/home.html'
    context_object_name = 'latest_city'

    def get_queryset(self):
        return City.objects.order_by('city_id')


# def contact(request):
# 	form = ContactForm(request.POST or None)
# 	context = {
# 		"form":form,
# 		"title":"contact us"
# 	}

# 	# if form.is_valid():
# 	# 	print form.cleaned_data

# 	return render(request,"brokerhome/contact.html", context)


# class DetailView1(generic.DetailView):
#     model = City
#     template_name = 'brokerhome/city_details.html'

#     def get_context_data(self, **kwargs):
#         context = super(DetailView, self).get_context_data(**kwargs)

#         context['broker_list'] = BrokerLocale.objects.filter(city_id=self.object.city_id).values_list(
#                                 'broker_id', flat=True).distinct()

#         context['broker_data'] = []
#         context['broker_locale'] = []
#         count = 0
#         for broker in context['broker_list']:

#             count += 1
#             #pdb.set_trace()
#             details = BrokerDetails.objects.filter(broker_id=broker).values()[0]

#             details['rating'] = BrokerRating.objects.filter(broker_id=broker).aggregate(Avg('rating')).values()[0]
#             details['locale'] = [loc.encode("utf8") for loc in BrokerLocale.objects.filter(broker_id=broker, city_id=self.object.city_id).values_list(
#                                 'locale_id__locale', flat=True)]
#             context['broker_data'].append(details)

#         return context


class RatingView(CreateView):
    template_name = 'brokerhome/submit_rating.html'
    form_class = RatingForm
    #success_url = '/brokers/' #can provide  get_absolute_url() instead in the model

    #after login
    # def form_valid(self, form):
    #     form.instance.user_id = self.request.user
    #     return super(RatingView, self).form_valid()

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            try:
                broker = BrokerDetails.objects.get(broker_id =self.kwargs['broker_id'])
                broker_record = BrokerRating.objects.get(broker_id=broker)
                
                form = self.form_class({'rating':broker_record.rating, 'review': broker_record.review})
            except ObjectDoesNotExist:
                form = self.form_class()

        return render(request, self.template_name, {'form' : form})

    def post(self, request, *args, **kwargs):        
        user_id = self.request.user
            
        if request.method == 'POST':
            try:
                broker = BrokerDetails.objects.get(broker_id =self.kwargs['broker_id'])
                broker_record = BrokerRating.objects.get(broker_id=broker)
                form = self.form_class(request.POST, instance =  broker_record)
            except ObjectDoesNotExist:
                form = self.form_class(request.POST or None)
        
            #pdb.set_trace()
            if form.is_valid():
                # print form.cleaned_data
                #form.Meta.fields['broker_id'] = self.kwargs['broker_id']

                new_rating = form.save(commit=False)
            
                new_rating.broker_id =  broker #'3905222'
                new_rating.user_id = user_id
                new_rating.save()
 #               pdb.set_trace()

                return HttpResponseRedirect(self.request.GET['next'])

        

        #context = {'form': form}
        return render(request, self.template_name, {'form' : form})

    def get_success_url(self):
        redirect_to=self.request.POST['next']
        print redirect_to
        return reverse('/brokers/')

@login_required
def user_profile(request):
    user = request.user
    context = {
        'user' : user
    }
    template = 'brokerhome/profile.html'
    return render(request,template,context)


# def locality_list(request):
    
#     qs = Locality.objects.order_by('city_id')
#     form = LocalityFilterForm(data = request.REQUEST)

#     facets = {
#         'selected': {},
#         'categories': {
#             'cities': City.objects.all(),

#         },
#     }

#     if form.is_valid():
#         city = form.cleaned_data['city']
#         if city:
#             facets['selected']['city'] = city
#             qs = qs.filter(city_id=city).distinct()

#     context = {
#         'form': form,
#         'facets': facets,
#         'object_list': qs,
#     }
#     return render(request, "brokerhome/locality.html", context)


class DetailView(generic.DetailView):
    model = City
    template_name = 'brokerhome/city_details.html'
    paginate_by = 15

    def get_page(self, request, qs):
        paginator = Paginator(qs, self.paginate_by)

        page_number = request.GET.get('page')
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            # If page is not an integer, show first page.
            page = paginator.page(1)
        except EmptyPage:
            # If page is out of range, show last existing page.
            page = paginator.page(paginator.num_pages)
        return page

   

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        form = BrokerFilterForm(data = self.request.GET)

        facets = {
            'selected': {},
            'categories': {
                'localities': Locality.objects.filter(city_id=self.object.city_id),},
            }

        
        broker_list = BrokerLocale.objects.filter(city_id=self.object.city_id).values_list(
                                'broker_id', flat=True).distinct()

        if form.is_valid():
            locale = form.cleaned_data['locale']
        if locale:
            facets['selected']['locale'] = locale
            broker_list = broker_list.filter(locale_id=locale).values_list(
                                'broker_id', flat=True).distinct()
        
        page = self.get_page(self.request, broker_list)


        broker_list = page
        context['broker_data'] = []
        
        count = 0
        for broker in broker_list:
            count += 1
            #pdb.set_trace()
            details = BrokerDetails.objects.filter(broker_id=broker).values()[0]

            details['rating'] = BrokerRating.objects.filter(broker_id=broker).aggregate(Avg('rating')).values()[0]
            details['locale'] = [loc.encode("utf8") for loc in BrokerLocale.objects.filter(broker_id=broker, city_id=self.object.city_id).values_list(
                                'locale_id__locale', flat=True)]
            context['broker_data'].append(details)

        context['form'] = form
        context['facets'] = facets

        return context
