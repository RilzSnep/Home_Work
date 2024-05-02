from src.decorators import log
import pytest


@log()
def test_function_success() -> str:
    return "success"


@log(filename="test_log.txt")
def test_function_success_file() -> str:
    return "success"


