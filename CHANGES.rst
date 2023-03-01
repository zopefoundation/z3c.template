=========
 CHANGES
=========

4.0 (2023-03-01)
================

- Add support for Python 3.11.

- Drop support for Python 2.7, 3.5, 3.6.


3.2 (2022-03-25)
================

- Add support for Python 3.8, 3.9, and 3.10.

- Drop support for Python 3.4.


3.1.0 (2019-02-05)
==================

- Adapt tests to `zope.configuration >= 4.2`.
- Add support for Python 3.7.


3.0.0 (2017-10-18)
==================

- Add support for PyPy.
- Add support for Python 3.4, 3.5 and 3.6.
- Drop support for Python 2.6 and 3.3.
- Make bound page templates have ``__self__`` and ``__func__``
  attributes to be more like Python 3 bound methods. (``im_func`` and
  ``im_self`` remain available.) See `issue 3
  <https://github.com/zopefoundation/z3c.template/issues/3>`_.
- Depend on Chameleon >= 3.0, z3c.pt >= 2.1 and z3c.ptcompat >= 2.1.0
  due to possible rendering issues. See `PR 2
  <https://github.com/zopefoundation/z3c.template/pull/2>`_.

2.0.0 (2015-11-09)
==================

- Standardize namespace ``__init__``


2.0.0a2 (2013-02-25)
====================

- Make sure the of the templates content type is a native string instead
  forced bytes.


2.0.0a1 (2013-02-22)
====================

- Added support for Python 3.3.

- Replaced deprecated ``zope.interface.implements`` usage with equivalent
  ``zope.interface.implementer`` decorator.

- Dropped support for Python 2.4 and 2.5.


1.4.1 (2012-02-15)
==================

- Remove hooks to use ViewPageTemplateFile from z3c.pt because this breaks when
  z3c.pt is available, but z3c.ptcompat is not included. As recommended by notes
  below.


1.4.0 (2011-10-29)
==================

- Moved z3c.pt include to extras_require chameleon. This makes the package
  independent from chameleon and friends and allows to include this
  dependencies in your own project.

- Upgrade to chameleon 2.0 template engine and use the newest z3c.pt and
  z3c.ptcompat packages adjusted to work with chameleon 2.0.

  See the notes from the z3c.ptcompat package:

  Update z3c.ptcompat implementation to use component-based template engine
  configuration, plugging directly into the Zope Toolkit framework.

  The z3c.ptcompat package no longer provides template classes, or ZCML
  directives; you should import directly from the ZTK codebase.

  Note that the ``PREFER_Z3C_PT`` environment option has been
  rendered obsolete; instead, this is now managed via component
  configuration.

  Also note that the chameleon CHAMELEON_CACHE environment value changed from
  True/False to a path. Skip this property if you don't like to use a cache.
  None or False defined in buildout environment section doesn't work. At least
  with chameleon <= 2.5.4

  Attention: You need to include the configure.zcml file from z3c.ptcompat
  for enable the z3c.pt template engine. The configure.zcml will plugin the
  template engine. Also remove any custom built hooks which will import
  z3c.ptcompat in your tests or other places.


1.3.0 (2011-10-28)
==================

- Update to z3c.ptcompat 1.0 (and as a result, to the z3c.pt 2.x series).

- Using Python's ``doctest`` module instead of depreacted
  ``zope.testing.doctest``.


1.2.1 (2009-08-22)
==================

* Corrected description of ``ITemplateDirective.name``.

* Added `zcml.txt` to ``long_description`` to show up on pypi.

* Removed zpkg helper files and zcml slugs.


1.2.0 (2009-02-26)
==================

* Add support for context-specific templates. Now, templates can be
  registered and looked up using (view, request, context) triple.
  To do that, pass the ``context`` argument to the ZCML directives.
  The ``getPageTemplate`` and friends will now try to lookup context
  specific template first and then fall back to (view, request) lookup.

* Allow use of ``z3c.pt`` using ``z3c.ptcompat`` compatibility layer.

* Forward the template kwargs to the options of the macro

* Changed package's mailing list address to zope-dev at zope.org
  instead of retired one.

1.1.0 (2007-10-08)
==================

* Added an ``IContentTemplate`` interface which is used for
  ``<z3c:template>``.

1.0.0 (2007-??-??)
==================

* Initial release.
