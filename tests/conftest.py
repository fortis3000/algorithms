import pytest
from random import seed, randint, sample, shuffle, uniform


seed(2021)


@pytest.fixture(name="large_int")
def get_large_int():
    yield randint(-2e31, 2e31 - 1)


@pytest.fixture(name="small_float")
def get_small_float():
    return uniform(-1.0, 1.0)


@pytest.fixture(name="large_float")
def get_large_float():
    return uniform(-2e31, 2e31)


@pytest.fixture(name="seq_li", params=list(range(10)))
def generate_sequence_li(request):
    return [randint(-2e31, 2e31 - 1) for _ in range(request.param)]


@pytest.fixture(name="seq_sf", params=list(range(10)))
def generate_sequence_sf(request):
    return [uniform(-1.0, 1.0) for _ in range(request.param)]


@pytest.fixture(name="seq_lf", params=list(range(10)))
def generate_sequence_lf(request):
    return [uniform(-2e31, 2e31) for _ in range(request.param)]


@pytest.fixture(name="unique_seq", params=list(range(10)))
def generate_unique_sequence(request):
    return sample(range(1000 * request.param), request.param)
