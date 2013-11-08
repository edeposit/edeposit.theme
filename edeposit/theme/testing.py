from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from zope.configuration import xmlconfig

class EDepositTheme(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import optilux.theme
        xmlconfig.file('configure.zcml', optilux.theme, context=configurationContext)
    
    def setUpPloneSite(self, portal):
        applyProfile(portal, 'edeposit.theme:default')

EDEPOSIT_THEME_FIXTURE = EDepositTheme()
EDEPOSIT_THEME_INTEGRATION_TESTING = IntegrationTesting(bases=(EDEPOSIT_THEME_FIXTURE,), name="EDepositTheme:Integration")
EDEPOSIT_THEME_FUNCTIONAL_TESTING = FunctionalTesting(bases=(EDEPOSIT_THEME_FIXTURE,), name="EDepositTheme:Functional")
