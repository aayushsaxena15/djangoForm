from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.template import loader
from .models import Station, Strategy
def articlespage(request):
	template = loader.get_template('polls/home.html')
	cluster_list = Station.objects.all()
	context = {}
	context['cl'] = []
	#output = ', '.join([q.cluster_id for q in cluster_list])
	#print(output)
	cluster_choices_list = (())
	for cluster in cluster_list:
		temp =(str(cluster),str(cluster))
		context['cl'].append((str(cluster).split('(')[1].split(')')[0]))

		cluster_choices_list = (temp,) + cluster_choices_list
		

	print(cluster_choices_list)

	strategy_list = Strategy.objects.all()
	context['sl'] = []
	#output = ', '.join([q.cluster_id for q in cluster_list])
	#print(output)
	strategy_choices_list = (())
	for strategy in strategy_list:
		temp =(str(strategy),str(strategy))
		context['sl'].append((str(strategy).split(' ')[1]))

		strategy_choices_list = (temp,) + cluster_choices_list
		

	print(strategy_choices_list)


	


	return HttpResponse(template.render(context, request))

"""
def success(request):
	return HttpResponse("Success.")


from django.shortcuts import render

def articlespage(request):
    return render(request, 'Articles/home.html')

"""
def successpage(request):
    cluster= request.POST.get('cluster')

    strategy = request.POST.get('strategy')

    trucks = request.POST.get('trucks')

    
    context= {'cluster':cluster, 'strategy' : strategy, 'trucks': trucks}
    template = loader.get_template('polls/successpage.html')
    file = open ("/home/aayush/my_django15_project/polls/data/" + cluster + "_" + strategy + "_" + trucks, "r")
    context['fileData'] = file.read()
    #return render(request, 'polls/successpage.html', context)
    return HttpResponse(template.render(context, request))