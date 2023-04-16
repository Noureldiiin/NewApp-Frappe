# Copyright (c) 2023, Nour and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from docx import Document as docx
from docxtpl import DocxTemplate

class NewDoctype(Document):
	
	@frappe.whitelist()
	def get_details(doc,method = None):
		try:
			filee = frappe.get_doc("File", doc.template)
			frappe.msgprint(filee.get_full_path())
			template = DocxTemplate(filee.get_full_path())
			to_fill_in = {
				"full_name" : "nour"
			}
			template.render(to_fill_in)

			# save the modified document
			template.save('./dcode.com/public/files/test.docx')
			
			frappe.msgprint("GOOD")
		except:
			frappe.throw("Hello")

