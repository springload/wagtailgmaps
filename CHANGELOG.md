# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [2.0.0] - 2025-04-27

### Removed

-   Compatibility with Wagtail 6.3 and before (use wagtailgmap==1.0.1 instead)

### Changed

-   (BREAKING) Rename the `latlng` kwarg to `latlngMode` to better reflect it's meaning
-   (BREAKING) Rename `edit_handlers` to `panels` in line with Wagtail Core
-   Migrated admin JS to Stimulus
-   Replace "WidgetWithScript" with a plain input that has `media`
-   Migrate CI testing to Github Actions
-   Update tox file
-   Format code with black
-   Updated test app for modern Django (mostly `url` to `path`)
-   Documentation updated with guide for setting up API keys (thanks @FlipperPA)

## [1.0.1] - 2018-06-25

Thanks to @scisteffan for their contribution.

## Fixed

-   Map would not display correctly in the admin (#36, #37)

## [1.0] - 2018-03-09

### Removed

-   Compatibility with Wagtail 1.13 and before (use wagtailgmap==0.4 instead)

### Changed

-   Simplified the implementation of the MapFieldPanel
-   Derive the map ID from the field ID (instead of using a randomly generated ID)
-   Simplifies the flow of options between the widget, the template and the JS.

### Fixed

-   Compatibility with Wagtail 2.0
-   Admin map missing API key for display with noscript

## [0.4] - 2018-01-15

Thanks to @balinabbb for their contribution.

### Added

-   Add the possibility to set the (admin) map language with `WAGTAIL_ADDRESS_MAP_LANGUAGE`

## [0.3.1] - 2017-11-20

### Fixed

-   Installation on Python 2.7.6 would fail

## [0.3] - 2017-09-21

Thanks to @danreeves, @craigloftus, @urlsangel and @SalahAdDin for their contributions.

### Added

-   Dedicated `MapFieldPanel` edit handler

### Changed

-   License is now MIT
-   Do not require `django-overextends` anymore

### Fixed

-   Compatibility with Django >= 1.9

## [0.2.5] - 2016-04-04

### Fixed

-   Compatibility with Wagtail 1.4

## [0.2.3] - 2015-09-02

### Added

-   Multiple classes allowed on the panel (e.g. classname="gmap col3")
-   Added logic to allow outputting a `latlng` value rather than the street address. Adding the `gmap--latlng` modifier class to the panel enables the feature.

### Fixed

-   Compatibility with Wagtail 1.0

## [0.2.2] - 2015-07-07

...

## [0.2.1] - 2015-05-25

### Fixed

-   Compatibility with Wagtail 1.0b2

## [0.2] - 2015-05-12

...

## [0.1] - 2015-02-27

Initial Release

[Unreleased]: https://github.com/springload/wagtailgmaps/compare/2.0.0...HEAD
[2.0.0]: https://github.com/springload/wagtailgmaps/compare/1.0.1...2.0.0
[1.0.1]: https://github.com/springload/wagtailgmaps/compare/v1.0...v1.0.1
[1.0]: https://github.com/springload/wagtailgmaps/compare/v0.4...v1.0
[0.4]: https://github.com/springload/wagtailgmaps/compare/v0.3.1...v0.4
[0.3.1]: https://github.com/springload/wagtailgmaps/compare/v0.3...v0.3.1
[0.3]: https://github.com/springload/wagtailgmaps/compare/v0.2.5...v0.3
[0.2.5]: https://github.com/springload/wagtailgmaps/compare/v0.2.3...v0.2.5
[0.2.3]: https://github.com/springload/wagtailgmaps/compare/v0.2.2...v0.2.3
[0.2.2]: https://github.com/springload/wagtailgmaps/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/springload/wagtailgmaps/compare/v0.2...v0.2.1
[0.2]: https://github.com/springload/wagtailgmaps/compare/v0.1...v0.2
[0.1]: https://github.com/springload/wagtailgmaps/compare/9b4372371576da8f96a52cfc225d1c5c1b3c76d1...v0.1
