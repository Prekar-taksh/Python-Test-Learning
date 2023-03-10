# In this file, you'll need to define a fixture that initializes the Azure Functions runtime

import pytest
from azure.functions import ExecutionContext, HttpRequest

@pytest.fixture(scope="session")
def function(request):
    from azure_functions_worker import testutils

    func_root = "<path to your Azure Function app code>" #Replace with the path to the root directory of your Azure Function app code
    testutils.clear_scripts_folder()
    testutils.patch_sys_path(func_root)
    testutils.load_function_environment_variables(func_root)

    from <your_function_module> import main #Replace <your_function_module> with the name of the module that contains your function's main function
    return main
