import logging

logger = logging.getLogger(__name__)


def add(a: float, b: float) -> float:
    result = a + b
    logger.info("Addition performed: %s + %s = %s", a, b, result)
    return result


def subtract(a: float, b: float) -> float:
    result = a - b
    logger.info("Subtraction performed: %s - %s = %s", a, b, result)
    return result


def multiply(a: float, b: float) -> float:
    result = a * b
    logger.info("Multiplication performed: %s * %s = %s", a, b, result)
    return result


def divide(a: float, b: float) -> float:
    if b == 0:
        logger.error("Division by zero attempted: %s / %s", a, b)
        raise ValueError("Cannot divide by zero")
    result = a / b
    logger.info("Division performed: %s / %s = %s", a, b, result)
    return result
