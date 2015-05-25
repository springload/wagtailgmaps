import pkg_resources


def get_wagtail_version():
    return pkg_resources.get_distribution("wagtail").version
