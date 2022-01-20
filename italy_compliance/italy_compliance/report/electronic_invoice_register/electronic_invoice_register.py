# Copyright (c) 2022, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe

from erpnext.accounts.report.sales_register.sales_register import _execute


def execute(filters=None):
	return _execute(filters)
