
from decimal import Decimal
from typing import Union


def cast_to_decimal(value: Union[int, float, str, Decimal], precision: int = 2) -> Decimal:
    """
    Cast elementary data type to Decimal without the floating point precision errors.

    Args:
        value: value to be casted (elementary type: int, float, str. Also, Decimal itself to be idempotent operation)
        precision: decimal digits until which to trim the value

    Returns:
        Value casted to Decimal
    
    """
    if isinstance(value, float):
        value = f'{value:.{precision}f}'
    return value if isinstance(value, Decimal) else Decimal(value)

