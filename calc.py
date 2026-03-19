from mcp.server.fastmcp import FastMCP
mcp=FastMCP(name="calc_mcp")

@mcp.tool()
def add(a: int, b: int) -> int:
   """Return the sum of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The result of adding `a` and `b`.
    """
   return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
   """Return the product of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The result of multiplying `a` and `b`.
    """
   return a * b
@mcp.tool()
def sub(a:int, b:int) -> int:
   """Return the difference of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The result of subtracting `b` from `a`.
    """
   return a - b
@mcp.tool()
def divide(a:int|float , b:int|float) -> int|float:
   """Return the quotient of two numbers.

    Args:
        a (int | float): The dividend.
        b (int | float): The divisor.

    Returns:
        int | float: The result of dividing `a` by `b`.
    """
   return a / b

@mcp.resource(uri="data://operations")
def operations()->list[str]:
    return ["add", "subtract", "multiply", "divide"]


@mcp.resource(uri="data://operation/{intent}")
def get_operation(intent: str):
    if intent =="add" :
       return "add"
    else:
       return "unknown"

if __name__=="__main__":
    mcp.run(transport="stdio")