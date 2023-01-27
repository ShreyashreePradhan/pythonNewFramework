import pytest


# Utilities have knowledge of initial setups
# Parent class

@pytest.mark.usefixtures("Setup")
class BaseClass:
    pass
