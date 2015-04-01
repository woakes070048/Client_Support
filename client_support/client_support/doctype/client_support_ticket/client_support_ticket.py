# Copyright (c) 2013, Makarand Bauskar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname
from frappe.utils import now_datetime, now
from frappe import msgprint
import datetime
import time

class ClientSupportTicket(Document):
	
	def autoname(self):
		frappe.errprint("autoname")
		
		project_name = self.project[:3]
		self.name = make_autoname(project_name + ".####")

	def validate(self):
		frappe.errprint("validate")
		
		if not self.project:
			msgprint("Please select the project")

	def on_update(self):
		# if status is closed then set closing date
	
		if self.status == "Open":
			# if status is open then set opening date
			# check if opening_date is already set if not then set the value

			odt = frappe.db.get_value("Client Support Ticket","opening_date","opening_date")
			if not odt:
				self.opening_date = datetime.datetime.strptime(now(),'%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d %H:%M:%S')
			else:
				self.opening_date = odt 

		elif self.status == "Close":
			self.closing_date = datetime.datetime.strptime(now(),'%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d %H:%M:%S')