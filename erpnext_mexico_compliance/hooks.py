app_name = "erpnext_mexico_compliance"
app_title = "ERPNext Mexico Compliance"
app_publisher = "TI Sin Problemas"
app_description = "ERPNext app to serve as base to comply with Mexican Rules and Regulations"
app_email = "info@tisinproblemas.com"
app_license = "MIT"
app_home = "/desk/mexico-compliance"
required_apps = ["erpnext"]

web_include_js = "/assets/erpnext_mexico_compliance/js/portal_invoice.js"

doctype_js = {
	"Sales Invoice": "public/js/sales_invoice.js",
	"Payment Entry": "public/js/payment_entry.js",
}

after_migrate = [
	"erpnext_mexico_compliance.migrate.set_sales_invoices_uuid",
	"erpnext_mexico_compliance.migrate.set_payment_entries_uuid",
	"erpnext_mexico_compliance.migrate.enqueue_sat_catalogs_update",
	"erpnext_mexico_compliance.migrate.set_cfdi_settings",
]

override_doctype_class = {
	"Customer": "erpnext_mexico_compliance.overrides.customer.Customer",
	"Employee": "erpnext_mexico_compliance.overrides.employee.Employee",
	"Payment Entry": "erpnext_mexico_compliance.overrides.payment_entry.PaymentEntry",
	"Sales Invoice": "erpnext_mexico_compliance.overrides.sales_invoice.SalesInvoice",
	"Sales Invoice Item": "erpnext_mexico_compliance.overrides.sales_invoice_item.SalesInvoiceItem",
}

scheduler_events = {
	"hourly": ["erpnext_mexico_compliance.tasks.check_cancellation_status"],
}

export_python_type_annotations = True

fixtures = [
	{"doctype": "Custom Field", "filters": [{"module": "ERPNext Mexico Compliance"}]},
	{
		"doctype": "Property Setter",
		"filters": [{"module": "ERPNext Mexico Compliance"}],
	},
	{
		"doctype": "Cancellation Reason",
	},
]
