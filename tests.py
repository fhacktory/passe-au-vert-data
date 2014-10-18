from nose.tools import assert_equal
from passe_au_vert import light_state

def test_light_state():
	assert_equal(light_state(10, 0, 5, 10).split(',')[0], 'red')
	assert_equal(light_state(10, 0, 15, 5).split(',')[0], 'green')
	assert_equal(light_state(100, 0, 5, 10).split(',')[0], 'red')