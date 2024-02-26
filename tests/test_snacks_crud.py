
import pytest
from snacks_crud.snacks_crud import snacks_crud 


# Demo Tests

@pytest.mark.skip
def test_start():
    actual = snacks_crud()
    expected = "Starter test"
    assert actual == expected

@pytest.mark.skip
def test_fixture_01(fixture_01):
    actual = snacks_crud(fixture_01)
    expected = "Starter fixture"
    assert actual == expected


# Demo Fixture
        
@pytest.fixture 
def fixture_01():
    yield "Starter fixture"

