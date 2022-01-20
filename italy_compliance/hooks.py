from . import __version__ as app_version

app_name = "italy_compliance"
app_title = "Italy Compliance"
app_publisher = "Frappe Technologies"
app_description = "app to include lo compliance in Italy"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "diksha@frappe.io"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/italy_compliance/css/italy_compliance.css"
# app_include_js = "/assets/italy_compliance/js/italy_compliance.js"

# include js, css files in header of web template
# web_include_css = "/assets/italy_compliance/css/italy_compliance.css"
# web_include_js = "/assets/italy_compliance/js/italy_compliance.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "italy_compliance/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}

doctype_js = {
	"Sales Invoice" : "public/js/sales_invoice.js"
	}

# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "italy_compliance.utils.jinja_methods",
# 	"filters": "italy_compliance.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "italy_compliance.install.before_install"
after_install = "italy_compliance.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "italy_compliance.uninstall.before_uninstall"
# after_uninstall = "italy_compliance.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "italy_compliance.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
	"Sales Invoice": {
		"on_submit": [
			"italy_compliance.utils.sales_invoice_on_submit",
		],
		"on_cancel": [
			"italy_compliance.utils.sales_invoice_on_cancel",
		]
	},
	'Address': {
		'validate': [
			'italy_compliance.utils.set_state_code',
		],
	},
}


regional_overrides = {
	'Italy': {
		'erpnext.controllers.taxes_and_totals.update_itemised_tax_data': 'italy_compliance.utils.update_itemised_tax_data',
		'erpnext.controllers.accounts_controller.validate_regional': 'italy_compliance.utils.sales_invoice_validate',
	}
}
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"italy_compliance.tasks.all"
# 	],
# 	"daily": [
# 		"italy_compliance.tasks.daily"
# 	],
# 	"hourly": [
# 		"italy_compliance.tasks.hourly"
# 	],
# 	"weekly": [
# 		"italy_compliance.tasks.weekly"
# 	],
# 	"monthly": [
# 		"italy_compliance.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "italy_compliance.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "italy_compliance.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "italy_compliance.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"italy_compliance.auth.validate"
# ]

