import pytest
from percy import create_percy
from percy.settings import RESOLUTIONS

resolutions = list(RESOLUTIONS.keys())
test_pagenums = [i for i in range(5)]


@pytest.mark.parametrize("resolution", resolutions)
def test_resolution_full(resolution: str):
    """
    Tests class object creation when,
    resolution = 'full'
    """
    assert str(type(create_percy(resolution=resolution,
                                 basepath="/tmp/",
                                 page_num=1))) == "<class 'percy.percy.Percy'>"

