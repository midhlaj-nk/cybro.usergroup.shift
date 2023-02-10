# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from cybro.usergroup.shift.testing import CYBRO_USERGROUP_SHIFT_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that cybro.usergroup.shift is properly installed."""

    layer = CYBRO_USERGROUP_SHIFT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if cybro.usergroup.shift is installed."""
        self.assertTrue(self.installer.is_product_installed(
            'cybro.usergroup.shift'))

    def test_browserlayer(self):
        """Test that ICybroUsergroupShiftLayer is registered."""
        from cybro.usergroup.shift.interfaces import (
            ICybroUsergroupShiftLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICybroUsergroupShiftLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = CYBRO_USERGROUP_SHIFT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstall_product('cybro.usergroup.shift')
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if cybro.usergroup.shift is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed(
            'cybro.usergroup.shift'))

    def test_browserlayer_removed(self):
        """Test that ICybroUsergroupShiftLayer is removed."""
        from cybro.usergroup.shift.interfaces import \
            ICybroUsergroupShiftLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICybroUsergroupShiftLayer, utils.registered_layers())
