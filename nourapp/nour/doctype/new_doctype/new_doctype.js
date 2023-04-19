// Copyright (c) 2023, Nour and contributors
// For license information, please see license.txt

frappe.ui.form.on('New Doctype', {
	// refresh: function(frm) {
		download_file: function(frm) {
			frm.doc.cows = []
			frappe.call({
				doc: frm.doc,
				method: "get_details",
				callback: function(r) {
					frm.refresh_fields();
					frm.refresh();
				}
			});
		}
	// }
});
