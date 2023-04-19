# Copyright (c) 2023, Nour and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from docx import Document as docx
from docxtpl import DocxTemplate
from frappe.utils import get_site_name 

class NewDoctype(Document):
	
	@frappe.whitelist()
	def get_details(doc,method = None):
		get_template = frappe.db.sql(f"""
				select * from `tabTemplate`
				join `tabTemplate Table` on `tabTemplate`.name = `tabTemplate Table`.parent
				where `tabTemplate Table`.doctype_name = '{doc.doctype}'
				and `tabTemplate Table`.template_file IS NOT NULL
		""",as_dict = 1)
		if get_template is None:
			frappe.throw("There is no such template for this doctype")
		
		
		

		try:
			filee = frappe.get_doc("File", get_template[0].template_file)
			template = DocxTemplate(filee.get_full_path())
			to_fill_in = {
				"full_name" : doc.test_name
			}
			template.render(to_fill_in)

			# save the modified document
			template.save('/home/nour/Downloads/test.docx')
			
			frappe.msgprint("Downloaded!"+'\n'+'You can find it in the downloads file')
		except:
			frappe.throw("Something went wrong")

