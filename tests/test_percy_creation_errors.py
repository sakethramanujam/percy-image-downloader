import pytest
from percy import create_percy

test_resolutions = ["","percy"]
test_pages = ["","100000000000000000"]

@pytest.mark.parametrize("resolution",test_resolutions)
def test_resolution_errors(resolution):
    """
    Tests class object creation
    - when a wrong resolution is entered
    """
    with pytest.raises(ValueError):
        create_percy(resolution=resolution,
                     basepath="/tmp/",
                     page_num=0)

@pytest.mark.parametrize("page_num", test_pages)
def test_pagenum_errors(page_num:int):
    """
    Tests class object creation
    - when a page number out of bounds is entered
    """
    with pytest.raises(ValueError):
        create_percy(resolution="full",
                     basepath="/tmp/",
                     page_num=page_num)
