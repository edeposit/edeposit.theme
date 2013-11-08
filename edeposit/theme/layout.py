from zope.component import getMultiAdapter
from zope.component import queryMultiAdapter
from zope.component import queryUtility

from plone.portlets.interfaces import IPortletManagerRenderer
from plone.portlets.interfaces import IPortletManager

from plone.app.layout.globals.layout import LayoutPolicy

from plone.memoize.view import memoize

class EDepositLayoutPolicy(LayoutPolicy):
    pass
