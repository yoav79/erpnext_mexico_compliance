from frappe import _
from frappe.tests.utils import FrappeTestCase

from erpnext_mexico_compliance.overrides.sales_invoice_item import SalesInvoiceItem


class TestSalesInvoiceItemServiceDuration(FrappeTestCase):
	def _make_item(self, **kwargs) -> SalesInvoiceItem:
		data = {"doctype": "Sales Invoice Item", "idx": 1}
		data.update(kwargs)
		return SalesInvoiceItem(data)

	def _expected_duration_display(
		self, service_start_date: str | None = None, service_end_date: str | None = None
	) -> str:
		start_date = _("From {}").format(service_start_date) if service_start_date else ""
		end_date = _("To {}").format(service_end_date) if service_end_date else ""
		return f"{start_date} {end_date}".strip()

	def test_service_duration_display_without_dates(self):
		item = self._make_item()
		self.assertEqual(item.service_duration_display, self._expected_duration_display())

	def test_service_duration_display_with_start_date_only(self):
		item = self._make_item(service_start_date="2024-01-01")
		self.assertEqual(
			item.service_duration_display,
			self._expected_duration_display(service_start_date="2024-01-01"),
		)

	def test_service_duration_display_with_end_date_only(self):
		item = self._make_item(service_end_date="2024-06-01")
		self.assertEqual(
			item.service_duration_display,
			self._expected_duration_display(service_end_date="2024-06-01"),
		)

	def test_service_duration_display_with_both_dates(self):
		item = self._make_item(service_start_date="2024-01-01", service_end_date="2024-06-01")
		self.assertEqual(
			item.service_duration_display,
			self._expected_duration_display(
				service_start_date="2024-01-01",
				service_end_date="2024-06-01",
			),
		)
