from frappe.tests.utils import FrappeTestCase

from erpnext_mexico_compliance.controllers.validators import is_valid_curp, is_valid_rfc


class TestValidators(FrappeTestCase):
	def test_valid_rfc_persona_moral(self):
		self.assertTrue(is_valid_rfc("AAA010101AAA"))

	def test_valid_rfc_persona_fisica(self):
		self.assertTrue(is_valid_rfc("XAXX010101000"))

	def test_invalid_rfc(self):
		self.assertFalse(is_valid_rfc("INVALID"))
		self.assertFalse(is_valid_rfc(""))

	def test_valid_curp(self):
		self.assertTrue(is_valid_curp("GARC850101HDFRRL09"))

	def test_invalid_curp(self):
		self.assertFalse(is_valid_curp("INVALID"))
		self.assertFalse(is_valid_curp(""))
