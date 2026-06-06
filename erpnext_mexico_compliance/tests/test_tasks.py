from unittest.mock import MagicMock, patch

import frappe
from frappe.tests.utils import FrappeTestCase

from erpnext_mexico_compliance.tasks import PENDING_CANCELLATION_FILTERS, check_cancellation_status

EXPECTED_FILTERS = PENDING_CANCELLATION_FILTERS


class TestCheckCancellationStatus(FrappeTestCase):
	@patch("erpnext_mexico_compliance.tasks.frappe.get_doc")
	@patch("erpnext_mexico_compliance.tasks.frappe.get_all")
	def test_sales_invoice_filters(self, mock_get_all, mock_get_doc):
		mock_get_all.return_value = []

		check_cancellation_status()

		mock_get_all.assert_any_call(
			"Sales Invoice",
			fields=["name"],
			filters=EXPECTED_FILTERS,
		)

	@patch("erpnext_mexico_compliance.tasks.frappe.get_doc")
	@patch("erpnext_mexico_compliance.tasks.frappe.get_all")
	def test_payment_entry_filters(self, mock_get_all, mock_get_doc):
		mock_get_all.return_value = []

		check_cancellation_status()

		mock_get_all.assert_any_call(
			"Payment Entry",
			fields=["name"],
			filters=EXPECTED_FILTERS,
		)

	@patch("erpnext_mexico_compliance.tasks.frappe.get_doc")
	@patch("erpnext_mexico_compliance.tasks.frappe.get_all")
	def test_calls_update_cancellation_status_for_each_document(self, mock_get_all, mock_get_doc):
		mock_get_all.side_effect = [
			[frappe._dict({"name": "SI-001"}), frappe._dict({"name": "SI-002"})],
			[frappe._dict({"name": "PE-001"})],
		]
		mock_doc = MagicMock()
		mock_get_doc.return_value = mock_doc

		check_cancellation_status()

		self.assertEqual(mock_get_doc.call_count, 3)
		mock_get_doc.assert_any_call("Sales Invoice", "SI-001")
		mock_get_doc.assert_any_call("Sales Invoice", "SI-002")
		mock_get_doc.assert_any_call("Payment Entry", "PE-001")
		self.assertEqual(mock_doc.update_cancellation_status.call_count, 3)

	@patch("erpnext_mexico_compliance.tasks.frappe.get_doc")
	@patch("erpnext_mexico_compliance.tasks.frappe.get_all")
	def test_filter_excludes_unstamped_documents(self, mock_get_all, mock_get_doc):
		mock_get_all.return_value = []

		check_cancellation_status()

		for call in mock_get_all.call_args_list:
			filters = call.kwargs["filters"]
			self.assertEqual(filters["mx_stamped_xml"], ["is", "set"])
			self.assertEqual(filters["cancellation_acknowledgement"], ["is", "set"])
			self.assertEqual(filters["docstatus"], 1)
