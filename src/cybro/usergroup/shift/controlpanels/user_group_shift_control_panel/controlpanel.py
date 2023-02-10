# -*- coding: utf-8 -*-
from cybro.usergroup.shift import _
from cybro.usergroup.shift.interfaces import ICybroUsergroupShiftLayer
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.restapi.controlpanels import RegistryConfigletPanel
from plone.z3cform import layout
from zope.component import adapter
from zope.interface import Interface
from zope import schema

class IUserGroupShiftControlPanel(Interface):
    myfield_name = schema.TextLine(
        title=_(
            "This is an example field for this control panel",
        ),
        description=_(
            "",
        ),
        default="",
        required=False,
        readonly=False,
    )


class UserGroupShiftControlPanel(RegistryEditForm):
    schema = IUserGroupShiftControlPanel
    schema_prefix = "cybro.usergroup.shift.user_group_shift_control_panel"
    label = _("User Group Shift Control Panel")


UserGroupShiftControlPanelView = layout.wrap_form(
    UserGroupShiftControlPanel, ControlPanelFormWrapper
)



@adapter(Interface, ICybroUsergroupShiftLayer)
class UserGroupShiftControlPanelConfigletPanel(RegistryConfigletPanel):
    """Control Panel endpoint"""

    schema = IUserGroupShiftControlPanel
    configlet_id = "user_group_shift_control_panel-controlpanel"
    configlet_category_id = "Products"
    title = _("User Group Shift Control Panel")
    group = ""
    schema_prefix = "cybro.usergroup.shift.user_group_shift_control_panel"
