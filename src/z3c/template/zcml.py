##############################################################################
#
# Copyright (c) 2005 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""ZCML Directives
"""
import os

import zope.component.zcml
import zope.configuration.fields
import zope.interface
import zope.schema
from zope.configuration.exceptions import ConfigurationError
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

import z3c.template.interfaces
from z3c.template.template import TemplateFactory


class ITemplateDirective(zope.interface.Interface):
    """Parameters for the template directive."""

    template = zope.configuration.fields.Path(
        title='Layout template.',
        description="Refers to a file containing a page template (should "
        "end in extension ``.pt`` or ``.html``).",
        required=True,
    )

    name = zope.schema.TextLine(
        title="The name of the template.",
        description="The name is used to look up the template.",
        default='',
        required=False)

    macro = zope.schema.TextLine(
        title='Macro',
        description="""
            The macro to be used.
            This allows us to define different macros in one template.
            The template designer can now create a whole site, the
            ViewTemplate can then extract the macros for single viewlets
            or views.
            If no macro is given the whole template is used for rendering.
            """,
        default='',
        required=False,
    )

    for_ = zope.configuration.fields.GlobalObject(
        title='View',
        description='The view for which the template should be available',
        default=zope.interface.Interface,
        required=False,
    )

    layer = zope.configuration.fields.GlobalObject(
        title='Layer',
        description='The layer for which the template should be available',
        required=False,
        default=IDefaultBrowserLayer,
    )

    context = zope.configuration.fields.GlobalObject(
        title='Context',
        description='The context for which the template should be available',
        required=False,
    )

    provides = zope.configuration.fields.GlobalInterface(
        title="Interface the template provides",
        description="This attribute specifies the interface the template"
        " instance will provide.",
        default=z3c.template.interfaces.IContentTemplate,
        required=False,
    )

    contentType = zope.schema.ASCIILine(
        title='Content Type',
        description='The content type identifies the type of data.',
        default='text/html',
        required=False,
    )


class ILayoutTemplateDirective(ITemplateDirective):
    """Parameters for the layout template directive."""

    provides = zope.configuration.fields.GlobalInterface(
        title="Interface the template provides",
        description="This attribute specifies the interface the template"
        " instance will provide.",
        default=z3c.template.interfaces.ILayoutTemplate,
        required=False,
    )


def templateDirective(
        _context, template, name='',
        for_=zope.interface.Interface, layer=IDefaultBrowserLayer,
        provides=z3c.template.interfaces.IContentTemplate,
        contentType='text/html', macro=None, context=None):

    # Make sure that the template exists
    template = os.path.abspath(str(_context.path(template)))
    if not os.path.isfile(template):
        raise ConfigurationError("No such file", template)

    factory = TemplateFactory(template, contentType, macro)
    zope.interface.directlyProvides(factory, provides)

    if context is not None:
        for_ = (for_, layer, context)
    else:
        for_ = (for_, layer)

    # register the template
    if name:
        zope.component.zcml.adapter(_context, (factory,), provides,
                                    for_, name=name)
    else:
        zope.component.zcml.adapter(_context, (factory,), provides,
                                    for_)


def layoutTemplateDirective(
        _context, template, name='',
        for_=zope.interface.Interface, layer=IDefaultBrowserLayer,
        provides=z3c.template.interfaces.ILayoutTemplate,
        contentType='text/html', macro=None, context=None):

    templateDirective(_context, template, name, for_, layer, provides,
                      contentType, macro, context)
