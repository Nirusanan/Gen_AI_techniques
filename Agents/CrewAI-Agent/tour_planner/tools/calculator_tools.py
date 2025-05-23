from langchain.tools import tool

class CalculatorTools:
    @staticmethod
    @tool("Make a calculation")
    def calculate(operation: str) -> str:
        """
        Useful to perform any mathematical calculations,
        like sum, minus, multiplication, division, etc.
        The input to this tool should be a mathematical
        expression, a couple examples are `200*7` or `5000/2*10`
        """
        try:
            return str(eval(operation))  
        except (SyntaxError, NameError):
            return "Error: Invalid syntax in mathematical expression"
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed"
