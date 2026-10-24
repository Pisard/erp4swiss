app_name = "erp4swiss"
app_title = "ERP4Swiss"
app_publisher = "Vking Trade"
app_description = "ERPNext customisations for Switzerland: Swiss QR invoice print format and QR bill fixes"
app_email = "info@videocam.ch"
app_license = "mit"

# Apps
# ------------------

required_apps = ["swiss_accounting_software"]

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "erp4swiss",
# 		"logo": "/assets/erp4swiss/logo.png",
# 		"title": "ERP4Swiss",
# 		"route": "/erp4swiss",
# 		"has_permission": "erp4swiss.api.permission.has_app_permission",
# 	}
# ]

# The dock, the rail down the left of the desk, is a document rather than a hook. Author it in
# Manage Dock on a developer-mode site and press Export to App, and it is written to
# `erp4swiss/dock/erp4swiss/erp4swiss.json` for git to carry. An app that ships none has no
# rail: its sidebar gets a switcher in the header instead.
#
# A companion app, one that extends a host app rather than standing on its own, says so with
# `mount_on` on that same record, and its entries are appended to the host's rail. Mounting keeps
# the companion off the apps screen, so it takes precedence over any add_to_apps_screen above.

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erp4swiss/css/erp4swiss.css"
# app_include_js = "/assets/erp4swiss/js/erp4swiss.js"

# include js, css files in header of web template
# web_include_css = "/assets/erp4swiss/css/erp4swiss.css"
# web_include_js = "/assets/erp4swiss/js/erp4swiss.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "erp4swiss/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {"Sales Invoice": "public/js/sales_invoice.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_kanban_js = {"doctype" : "public/js/doctype_kanban.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "erp4swiss/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "erp4swiss.utils.jinja_methods",
# 	"filters": "erp4swiss.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "erp4swiss.install.before_install"
# after_install = "erp4swiss.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "erp4swiss.uninstall.before_uninstall"
# after_uninstall = "erp4swiss.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "erp4swiss.utils.before_app_install"
# after_app_install = "erp4swiss.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "erp4swiss.utils.before_app_uninstall"
# after_app_uninstall = "erp4swiss.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "erp4swiss.build.after_build"

# To hook into the build process of other apps
# The list of apps being built is passed as an argument

# after_app_build = "erp4swiss.build.after_app_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erp4swiss.notifications.get_notification_config"

# Awesome Bar
# -----------
# Extra search results: list of dicts with label, description, route, index.
# route: ["List", "ToDo"], "/desk/docs/some/page", or "https://example.com"
# awesomebar_search = ["erp4swiss.search.awesomebar_results"]

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erp4swiss.tasks.all"
# 	],
# 	"daily": [
# 		"erp4swiss.tasks.daily"
# 	],
# 	"hourly": [
# 		"erp4swiss.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erp4swiss.tasks.weekly"
# 	],
# 	"monthly": [
# 		"erp4swiss.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "erp4swiss.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "erp4swiss.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erp4swiss.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "erp4swiss.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["erp4swiss.utils.before_request"]
# after_request = ["erp4swiss.utils.after_request"]

# Job Events
# ----------
# before_job = ["erp4swiss.utils.before_job"]
# after_job = ["erp4swiss.utils.after_job"]

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
# 	"erp4swiss.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []



# ERP4Swiss
# ------------------

# The Swiss QR slip page (drawn by swiss_accounting_software) is made A4 before it is merged.
override_whitelisted_methods = {
	"swiss_accounting_software.attach_pdf.attach_pdf": "erp4swiss.overrides.qr_bill.attach_pdf",
}

# Sales Invoice prints with QR_Sales_Invoice by default.
fixtures = [
	{
		"dt": "Custom Field",
		"filters": [
			[
				"name",
				"in",
				[
					"Sales Invoice-reference_information",
					"Sales Invoice-reference",
					"Sales Invoice-column_break_svdcf",
					"Sales Invoice-subject",
				],
			],
		],
	},
	{
		"dt": "Email Template",
		"filters": [["name", "in", ["Facture (ERP4Swiss)"]]],
	},
	{
		"dt": "Property Setter",
		"filters": [
			["doc_type", "=", "Sales Invoice"],
			["property", "=", "default_print_format"],
		],
	},
]

# Invoice emails are sent right away instead of waiting up to 4 minutes for the email queue.
doc_events = {
	"Email Queue": {
		"after_insert": "erp4swiss.email_queue.send_immediately",
	},
}
