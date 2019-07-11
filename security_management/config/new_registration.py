from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("New Registration"),
        "icon": "octicon octicon-briefcase",
        "items": [
	    {
              "type": "doctype",
              "name": "Resident",
              "label": _("New Resident Registration"),
              "description": _("New resident registration"),
            },
	    {
              "type": "doctype",
              "name": "Security Guard",
              "label": _("New Security Guard Registration"),
              "description": _("New Security Guard registration"),
            },
	    {
              "type": "doctype",
              "name": "Mobile User",
              "label": _("New Mobile User"),
              "description": _("Register new user for mobile application"),
            }
          ]
      }
  ]
