import pytest
from .conftest import *

from ..sortings import Sorter  # sort_selection, sort_quick, sort_merge


class TestSelectionSorting:
    def test_sort_selection_li(self, seq_li):
        assert Sorter.sort_selection(seq_li) == sorted(seq_li)

    def test_sort_selection_sf(self, seq_sf):
        assert Sorter.sort_selection(seq_sf) == sorted(seq_sf)

    def test_sort_selection_lf(self, seq_lf):
        assert Sorter.sort_selection(seq_lf) == sorted(seq_lf)

    def test_sort_selection_unique(self, unique_seq):
        us = unique_seq
        assert Sorter.sort_selection(us) == sorted(us)

    def test_sort_quick_unique(self, unique_seq):
        us = unique_seq
        # length bug with sorted on the spot
        sus = sorted(us)
        assert Sorter.sort_quick(us) == sus


class TestQuickSorting:
    def test_sort_quick_li(self, seq_li):

        # length bug with sorted on the spot
        s = seq_li
        ss = sorted(seq_li)
        assert Sorter.sort_quick(s) == sorted(ss)

    def test_sort_quick_sf(self, seq_sf):

        # length bug with sorted on the spot
        s = seq_sf
        ss = sorted(seq_sf)
        assert Sorter.sort_quick(s) == sorted(ss)

    def test_sort_quick_lf(self, seq_lf):

        # length bug with sorted on the spot
        s = seq_lf
        ss = sorted(seq_lf)
        assert Sorter.sort_quick(s) == sorted(ss)


class TestMergeSorting:
    def test_sort_merge_li(self, seq_li):
        assert Sorter.sort_merge(seq_li) == sorted(seq_li)

    def test_sort_merge_sf(self, seq_sf):
        assert Sorter.sort_merge(seq_sf) == sorted(seq_sf)

    def test_sort_merge_lf(self, seq_lf):
        assert Sorter.sort_merge(seq_lf) == sorted(seq_lf)

    def test_sort_merge_unique(self, unique_seq):
        us = unique_seq
        assert Sorter.sort_merge(us) == sorted(us)
