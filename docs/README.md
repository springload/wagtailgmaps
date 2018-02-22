# Documentation

## Browser support

We align our browser support targets with that of Wagtail. Have a look at the [official documentation](http://docs.wagtail.io/en/latest/contributing/developing.html).

## Python/Django/Wagtail support

Python versions as defined in `setup.py` classifiers.

Django versions as [supported](https://www.djangoproject.com/download/#supported-versions) by the Django Project.

Wagtail versions as [supported](http://docs.wagtail.io/en/latest/releases/upgrading.html) by Wagtail (LTS, current and current-1).

Django/Wagtail combinations as [supported](http://docs.wagtail.io/en/latest/releases/upgrading.html#compatible-django-python-versions) by Wagtail.

### Which version combinations to include in Travis test matrix?

In order to keep for CI build time from growing out of control, not all Python/Django/Wagtail combinations will be tested.

Test as follow:
- All supported Django/Wagtail combinations with Python `2.7` (since it's the only version in the `2.x` series we support).
- All supported Django/Wagtail combinations with the latest supported Python version of the `3.x` series.
- The latest supported Django/Wagtail combination for the remaining Python versions.
