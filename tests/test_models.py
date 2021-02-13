# import pytest
from models.models import Guest

def test_guest_model():
    guest = Guest('John', 'Henson', 10)
    assert guest.firstName == 'John'
    assert guest.lastName == 'Henson'
    assert guest.roomNumber == 10