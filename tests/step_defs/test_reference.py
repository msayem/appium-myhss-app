from tests.step_defs.data_steps import *
from tests.step_defs.interaction_steps import *
from tests.step_defs.page_steps import *
from tests.step_defs.validate_steps import *
from pytest_bdd import scenarios


# Scenarios
scenarios('../features')

