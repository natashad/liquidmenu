import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
tsv_filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), "samkeenoodlemenu.tsv"))
from django.core.management import setup_environ
import liquidmenu.settings
setup_environ(liquidmenu.settings)

from menus.models import MenuItem, Menu

import csv
dataReader = csv.reader(open(tsv_filepath), dialect='excel-tab')

samkee = Menu.objects.all()[0]
for row in dataReader:
	if len(row) == 3:
		print row[0] + ":" + row[1] + ":" + row[2]
		menuitem = MenuItem(order_id=row[0], name=row[1], price=row[2], menu=samkee)
		menuitem.save()
