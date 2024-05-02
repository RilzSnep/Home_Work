from datetime import datetime
from typing import Callable, Any, Union, Optional


def log(filename: Optional[str] = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Union[str, Any]:
            start = datetime.now()
            try:
                result = func(*args, *kwargs)
                status = "ok"
            except Exception as e:
                result = f"error: {e.__class__.__name__}"
                status = "error"
            end = datetime.now()
            log_message = f"{start} {func.__name__} {status} ({end - start}). Inputs: {args}, {kwargs}"
            print(log_message) if not filename else open(filename, "a").write(log_message + "\n")
            if status == "error":
                raise
            return result
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(15, 3)
