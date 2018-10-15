# coding:utf-8

"""Python2/3系の互換性を維持するためのファイル。"""

try:
    import pathlib  # noqa
except ImportError:
    import pathlib2 as pathlib  # noqa
