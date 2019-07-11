from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Announcement"),
        "icon": "octicon octicon-briefcase",
        "items": [
            {
              "type": "doctype",
              "name": "Announcement",
              "label": _("New Announcement"),
              "description": _("Broadcast the messages to the resident"),
            },
          ]
      }
  ]
