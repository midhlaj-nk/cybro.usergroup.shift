# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE
    PloneSandboxLayer,
)
from plone.testing import z2

import cybro.usergroup.shift


class CybroUsergroupShiftLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=cybro.usergroup.shift)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cybro.usergroup.shift:default')


CYBRO_USERGROUP_SHIFT_FIXTURE = CybroUsergroupShiftLayer()


CYBRO_USERGROUP_SHIFT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CYBRO_USERGROUP_SHIFT_FIXTURE,),
    name='CybroUsergroupShiftLayer:IntegrationTesting',
)


CYBRO_USERGROUP_SHIFT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CYBRO_USERGROUP_SHIFT_FIXTURE,),
    name='CybroUsergroupShiftLayer:FunctionalTesting',
)


CYBRO_USERGROUP_SHIFT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        CYBRO_USERGROUP_SHIFT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CybroUsergroupShiftLayer:AcceptanceTesting',
)
