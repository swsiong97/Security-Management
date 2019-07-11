# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "security_management"
app_title = "Security Management"
app_publisher = "utar"
app_description = "Manage and monitor the security guard and gated community"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "swsiong97@1utar.my"
app_license = "MIT"

scheduler_events = {
 	"all": [
 		"security_management.sync_firebase.syncFirebase"
 	],
}

#doc_events = {
#	'Mobile User':{
#        	"on_update": "main_function.syncFirebase"
#	}
#}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/security_management/css/security_management.css"
# app_include_js = "/assets/security_management/js/security_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/security_management/css/security_management.css"
# web_include_js = "/assets/security_management/js/security_management.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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

# Website user home page (by function)
# get_website_user_home_page = "security_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "security_management.install.before_install"
# after_install = "security_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "security_management.notifications.get_notification_config"

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
#	}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"security_management.tasks.all"
# 	],
# 	"daily": [
# 		"security_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"security_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"security_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"security_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "security_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "security_management.event.get_events"
# }

