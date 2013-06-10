# Create your views here.

from menus.models import *
from django.http import HttpResponse
from django.template import Context, loader


def front_page(request):
	template = loader.get_template('frontpage.html')

	all_menus = Menu.objects.all()

	context = Context(
		{
			'all_menus' : all_menus,
		}
	)
	return HttpResponse(template.render(context))

def menu_filter(request, menu_id):
	template = loader.get_template('menu_filter.html')
	all_menus = Menu.objects.all()
	this_menu = Menu.objects.filter(id=menu_id)[0]
	menu_items_in_menu = MenuItem.objects.filter(menu=this_menu)

	context = Context (
		{
			'menu' : this_menu,
			'menu_items_in_menu' : menu_items_in_menu,
		}
	)
	return HttpResponse(template.render(context))
