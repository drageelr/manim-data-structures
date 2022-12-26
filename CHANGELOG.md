# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.6] - 2022-12-26

### PRS

- [#5](https://github.com/drageelr/manim-data-structures/pull/5)
  - `MArrayElement` & `MArray` & `MVariable`play animations by themselves.
  - `MArrayPointer` added.

## [0.1.5] - 2022-12-10

### PRs

- [#1](https://github.com/drageelr/manim-data-structures/pull/1):
    - `MVariable` added.
    - `MArray.remove_elem()` added.
    - `MArray.append_elem()` changed.
    - `MArray` label and fetch method added.
    - Generic `MArrayElement` sub-mobjects fetch method added.
    - `MArrayElementComp` enum added.
    - Changed `array.py` to `m_array.py`.
    - Documentation updated.

## [0.1.4] - 2022-11-27

### Added

- [`MArray`](https://github.com/drageelr/manim-data-structures/blob/251d6ff130243e4408ef6a9453cc7ad27f62d372/src/manim_data_structures/array.py#L292) class can now grow in any of the four directions; Up, Down, Right & Left.
- [`MArray`](https://github.com/drageelr/manim-data-structures/blob/251d6ff130243e4408ef6a9453cc7ad27f62d372/src/manim_data_structures/array.py#L292) class has hidden indices now.

## [0.1.3] - 2022-11-25

### Changed

- [`MArrayElement`](https://github.com/drageelr/manim-data-structures/blob/1854335f2311c3157f19e6d328165013fc64cbf6/src/manim_data_structures/array.py#L6) method `fetch_mob_text` changed to [`fetch_mob_value`](https://github.com/drageelr/manim-data-structures/blob/1854335f2311c3157f19e6d328165013fc64cbf6/src/manim_data_structures/array.py#L147).
- [`MArrayElement`](https://github.com/drageelr/manim-data-structures/blob/1854335f2311c3157f19e6d328165013fc64cbf6/src/manim_data_structures/array.py#L6) method `animate_mob_text` changed to [`animate_mob_value`](https://github.com/drageelr/manim-data-structures/blob/1854335f2311c3157f19e6d328165013fc64cbf6/src/manim_data_structures/array.py#L220).

## [0.1.2] - 2022-11-25

### Added

- Added doc strings to [`MArrayElement`](https://github.com/drageelr/manim-data-structures/blob/1854335f2311c3157f19e6d328165013fc64cbf6/src/manim_data_structures/array.py#L6) class.
- Added doc strings to [`MArray`](https://github.com/drageelr/manim-data-structures/blob/1854335f2311c3157f19e6d328165013fc64cbf6/src/manim_data_structures/array.py#L243) class.

## [0.1.1] - 2022-11-24

### Changed

- Minimum python version requirement changed from `3.11` to `3.7`.

## [0.1.0] - 2022-11-24

### Added

- [`MArrayElement`](https://github.com/drageelr/manim-data-structures/blob/1854335f2311c3157f19e6d328165013fc64cbf6/src/manim_data_structures/array.py#L6) class to represent an array element.
- [`MArray`](https://github.com/drageelr/manim-data-structures/blob/1854335f2311c3157f19e6d328165013fc64cbf6/src/manim_data_structures/array.py#L243) class to represent an array.
