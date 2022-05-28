import unittest

from hypothesis import given
from hypothesis.strategies import integers

from wxwidgets._preview import hex_to_rgb


@given(integers(0, 255), integers(0, 255), integers(0, 255), integers(0, 255))
def test_hex_to_rgb(r, g, b, a):
    hex = f'#{r:0>2x}{g:0>2x}{b:0>2x}'
    assert hex_to_rgb(hex) == (r, g, b)
    hex = f'#{r:0>2x}{g:0>2x}{b:0>2x}'
    assert hex_to_rgb(hex) == (r, g, b)
    hex = f'#{r:0>2x}{g:0>2x}{b:0>2x}{a:0>2x}'
    assert hex_to_rgb(hex) == (r, g, b, a)
