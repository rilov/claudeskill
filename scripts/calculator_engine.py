#!/usr/bin/env python3
"""
Calculator Engine - Python Backend for Advanced Calculations
==============================================================
This demonstrates how Claude Skills can include executable Python scripts
that perform complex calculations and data processing.

SKILL DEMONSTRATION:
This file shows users that Claude Skills can:
1. Include executable code
2. Perform complex calculations
3. Generate visualizations
4. Process data programmatically
"""

import json
import sys
import math
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum

# For visualization (if needed)
try:
    import matplotlib.pyplot as plt
    import numpy as np
    PLOTTING_AVAILABLE = True
except ImportError:
    PLOTTING_AVAILABLE = False


class CalculatorType(Enum):
    """Types of calculators this engine supports"""
    BASIC = "basic"
    SCIENTIFIC = "scientific"
    FINANCIAL = "financial"
    STATISTICAL = "statistical"
    MATRIX = "matrix"
    GRAPHING = "graphing"


@dataclass
class CalculationResult:
    """Structure for returning calculation results"""
    result: Any
    formula_used: str
    steps: List[str]
    visualization_path: Optional[str] = None
    metadata: Dict[str, Any] = None


class CalculatorEngine:
    """
    Main calculator engine that demonstrates how skills can include
    complex Python logic for calculations.
    """
    
    def __init__(self):
        """Initialize the calculator engine"""
        self.history = []
        self.precision = 4
    
    # ============================================
    # BASIC OPERATIONS
    # ============================================
    
    def basic_operation(self, a: float, b: float, operation: str) -> CalculationResult:
        """
        Perform basic arithmetic operations
        This shows how skills can provide robust calculation functions
        """
        steps = []
        
        if operation == "add":
            result = a + b
            formula = f"{a} + {b} = {result}"
            steps = [
                f"Adding {a} and {b}",
                f"Result: {result}"
            ]
        
        elif operation == "subtract":
            result = a - b
            formula = f"{a} - {b} = {result}"
            steps = [
                f"Subtracting {b} from {a}",
                f"Result: {result}"
            ]
        
        elif operation == "multiply":
            result = a * b
            formula = f"{a} × {b} = {result}"
            steps = [
                f"Multiplying {a} by {b}",
                f"Result: {result}"
            ]
        
        elif operation == "divide":
            if b == 0:
                raise ValueError("Division by zero is not allowed")
            result = a / b
            formula = f"{a} ÷ {b} = {result}"
            steps = [
                f"Dividing {a} by {b}",
                f"Result: {result}"
            ]
        
        elif operation == "power":
            result = a ** b
            formula = f"{a}^{b} = {result}"
            steps = [
                f"Raising {a} to the power of {b}",
                f"Result: {result}"
            ]
        
        else:
            raise ValueError(f"Unknown operation: {operation}")
        
        return CalculationResult(
            result=round(result, self.precision),
            formula_used=formula,
            steps=steps,
            metadata={"type": "basic", "operation": operation}
        )
    
    # ============================================
    # SCIENTIFIC CALCULATIONS
    # ============================================
    
    def scientific_calculation(self, value: float, function: str) -> CalculationResult:
        """
        Perform scientific calculations
        Demonstrates how skills can include advanced mathematical functions
        """
        steps = []
        
        functions = {
            "sin": (math.sin, "sine"),
            "cos": (math.cos, "cosine"),
            "tan": (math.tan, "tangent"),
            "log": (math.log10, "log base 10"),
            "ln": (math.log, "natural log"),
            "sqrt": (math.sqrt, "square root"),
            "factorial": (math.factorial, "factorial")
        }
        
        if function not in functions:
            raise ValueError(f"Unknown function: {function}")
        
        func, name = functions[function]
        
        try:
            if function == "factorial":
                if value < 0 or int(value) != value:
                    raise ValueError("Factorial requires non-negative integer")
                result = func(int(value))
            else:
                result = func(value)
            
            formula = f"{function}({value}) = {result}"
            steps = [
                f"Calculating {name} of {value}",
                f"Using mathematical function: {function}",
                f"Result: {result}"
            ]
            
        except Exception as e:
            raise ValueError(f"Error in {function}: {str(e)}")
        
        return CalculationResult(
            result=round(result, self.precision) if isinstance(result, float) else result,
            formula_used=formula,
            steps=steps,
            metadata={"type": "scientific", "function": function}
        )
    
    # ============================================
    # FINANCIAL CALCULATIONS
    # ============================================
    
    def compound_interest(self, principal: float, rate: float, time: float, 
                         compounds_per_year: int = 12) -> CalculationResult:
        """
        Calculate compound interest
        Shows how skills can include domain-specific calculations
        """
        # Convert percentage to decimal if needed
        if rate > 1:
            rate = rate / 100
        
        # Calculate compound interest
        amount = principal * (1 + rate/compounds_per_year) ** (compounds_per_year * time)
        interest = amount - principal
        
        formula = f"A = P(1 + r/n)^(nt)"
        steps = [
            f"Principal (P): ${principal:,.2f}",
            f"Annual Rate (r): {rate:.4%}",
            f"Time (t): {time} years",
            f"Compounds per year (n): {compounds_per_year}",
            f"Calculation: {principal} × (1 + {rate}/{compounds_per_year})^({compounds_per_year}×{time})",
            f"Final Amount: ${amount:,.2f}",
            f"Interest Earned: ${interest:,.2f}"
        ]
        
        return CalculationResult(
            result={"amount": round(amount, 2), "interest": round(interest, 2)},
            formula_used=formula,
            steps=steps,
            metadata={
                "type": "financial",
                "calculation": "compound_interest",
                "effective_rate": ((1 + rate/compounds_per_year) ** compounds_per_year - 1)
            }
        )
    
    def loan_payment(self, principal: float, annual_rate: float, 
                    years: int) -> CalculationResult:
        """
        Calculate monthly loan payment
        Demonstrates complex financial formulas in skills
        """
        # Convert to monthly values
        monthly_rate = annual_rate / 100 / 12
        num_payments = years * 12
        
        if monthly_rate == 0:
            payment = principal / num_payments
        else:
            payment = principal * (monthly_rate * (1 + monthly_rate)**num_payments) / \
                     ((1 + monthly_rate)**num_payments - 1)
        
        total_paid = payment * num_payments
        total_interest = total_paid - principal
        
        formula = "M = P[r(1+r)^n]/[(1+r)^n-1]"
        steps = [
            f"Loan Amount: ${principal:,.2f}",
            f"Annual Rate: {annual_rate}%",
            f"Loan Term: {years} years ({num_payments} months)",
            f"Monthly Payment: ${payment:,.2f}",
            f"Total Amount Paid: ${total_paid:,.2f}",
            f"Total Interest: ${total_interest:,.2f}"
        ]
        
        return CalculationResult(
            result={
                "monthly_payment": round(payment, 2),
                "total_paid": round(total_paid, 2),
                "total_interest": round(total_interest, 2)
            },
            formula_used=formula,
            steps=steps,
            metadata={"type": "financial", "calculation": "loan_payment"}
        )
    
    # ============================================
    # STATISTICAL CALCULATIONS
    # ============================================
    
    def statistics(self, data: List[float]) -> CalculationResult:
        """
        Calculate statistical measures
        Shows how skills can process data sets
        """
        if not data:
            raise ValueError("Data list cannot be empty")
        
        n = len(data)
        mean = sum(data) / n
        
        # Calculate median
        sorted_data = sorted(data)
        if n % 2 == 0:
            median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
        else:
            median = sorted_data[n//2]
        
        # Calculate mode (most frequent value)
        from collections import Counter
        counter = Counter(data)
        mode_data = counter.most_common(1)
        mode = mode_data[0][0] if mode_data else None
        
        # Calculate variance and standard deviation
        variance = sum((x - mean) ** 2 for x in data) / n
        std_dev = math.sqrt(variance)
        
        # Calculate range
        data_range = max(data) - min(data)
        
        steps = [
            f"Data points: {n}",
            f"Mean: {mean:.4f}",
            f"Median: {median:.4f}",
            f"Mode: {mode:.4f}" if mode else "Mode: No unique mode",
            f"Standard Deviation: {std_dev:.4f}",
            f"Variance: {variance:.4f}",
            f"Range: {data_range:.4f}",
            f"Min: {min(data):.4f}",
            f"Max: {max(data):.4f}"
        ]
        
        return CalculationResult(
            result={
                "mean": round(mean, 4),
                "median": round(median, 4),
                "mode": round(mode, 4) if mode else None,
                "std_dev": round(std_dev, 4),
                "variance": round(variance, 4),
                "range": round(data_range, 4),
                "min": round(min(data), 4),
                "max": round(max(data), 4),
                "count": n
            },
            formula_used="Statistical Analysis",
            steps=steps,
            metadata={"type": "statistical", "data_points": n}
        )
    
    # ============================================
    # VISUALIZATION (IF AVAILABLE)
    # ============================================
    
    def create_function_graph(self, function_str: str, x_range: tuple = (-10, 10)) -> CalculationResult:
        """
        Create a graph of a mathematical function
        Demonstrates how skills can generate visualizations
        """
        if not PLOTTING_AVAILABLE:
            return CalculationResult(
                result="Visualization libraries not available",
                formula_used=function_str,
                steps=["Plotting libraries (matplotlib) not installed"],
                metadata={"type": "graphing", "error": "libraries_missing"}
            )
        
        try:
            # Create x values
            x = np.linspace(x_range[0], x_range[1], 1000)
            
            # Evaluate function (safely)
            # In production, you'd want more robust parsing
            allowed_names = {
                'x': x,
                'sin': np.sin,
                'cos': np.cos,
                'tan': np.tan,
                'exp': np.exp,
                'log': np.log,
                'sqrt': np.sqrt,
                'pi': math.pi,
                'e': math.e
            }
            
            y = eval(function_str, {"__builtins__": {}}, allowed_names)
            
            # Create plot
            plt.figure(figsize=(10, 6))
            plt.plot(x, y, 'b-', linewidth=2)
            plt.grid(True, alpha=0.3)
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title(f'Graph of f(x) = {function_str}')
            plt.axhline(y=0, color='k', linewidth=0.5)
            plt.axvline(x=0, color='k', linewidth=0.5)
            
            # Save plot
            output_path = '/tmp/function_graph.png'
            plt.savefig(output_path, dpi=100, bbox_inches='tight')
            plt.close()
            
            steps = [
                f"Function: f(x) = {function_str}",
                f"X range: {x_range[0]} to {x_range[1]}",
                "Generated graph successfully",
                f"Saved to: {output_path}"
            ]
            
            return CalculationResult(
                result="Graph created successfully",
                formula_used=f"f(x) = {function_str}",
                steps=steps,
                visualization_path=output_path,
                metadata={"type": "graphing", "x_range": x_range}
            )
            
        except Exception as e:
            return CalculationResult(
                result=f"Error creating graph: {str(e)}",
                formula_used=function_str,
                steps=[f"Error: {str(e)}"],
                metadata={"type": "graphing", "error": str(e)}
            )


# ============================================
# COMMAND-LINE INTERFACE
# ============================================

def main():
    """
    Command-line interface for the calculator engine
    This shows how skills can be executed directly
    """
    print("=" * 60)
    print("CALCULATOR ENGINE - Claude Skill Demonstration")
    print("=" * 60)
    print("\nThis Python script demonstrates how Claude Skills can:")
    print("1. Include executable code")
    print("2. Perform complex calculations")
    print("3. Process data programmatically")
    print("4. Generate results in various formats")
    print()
    
    # Create calculator instance
    calc = CalculatorEngine()
    
    # If arguments provided, parse them
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "demo":
            # Run demonstration
            print("Running demonstration calculations...\n")
            
            # Basic calculation
            print("1. BASIC ARITHMETIC:")
            result = calc.basic_operation(10, 5, "multiply")
            print(f"   {result.formula_used}")
            print()
            
            # Scientific calculation
            print("2. SCIENTIFIC:")
            result = calc.scientific_calculation(45, "sin")
            print(f"   {result.formula_used}")
            print()
            
            # Financial calculation
            print("3. FINANCIAL (Compound Interest):")
            result = calc.compound_interest(1000, 5, 10)
            print(f"   Principal: $1000, Rate: 5%, Time: 10 years")
            print(f"   Final Amount: ${result.result['amount']:,.2f}")
            print()
            
            # Statistical calculation
            print("4. STATISTICS:")
            data = [23, 45, 67, 89, 12, 34, 56, 78, 90, 45]
            result = calc.statistics(data)
            print(f"   Data: {data}")
            print(f"   Mean: {result.result['mean']}")
            print(f"   Std Dev: {result.result['std_dev']}")
            print()
            
        elif command == "json" and len(sys.argv) > 2:
            # Parse JSON input for programmatic use
            import json
            data = json.loads(sys.argv[2])
            
            if data["type"] == "basic":
                result = calc.basic_operation(
                    data["a"], 
                    data["b"], 
                    data["operation"]
                )
            elif data["type"] == "scientific":
                result = calc.scientific_calculation(
                    data["value"],
                    data["function"]
                )
            elif data["type"] == "financial":
                if data["calculation"] == "compound_interest":
                    result = calc.compound_interest(
                        data["principal"],
                        data["rate"],
                        data["time"],
                        data.get("compounds_per_year", 12)
                    )
                elif data["calculation"] == "loan_payment":
                    result = calc.loan_payment(
                        data["principal"],
                        data["rate"],
                        data["years"]
                    )
            elif data["type"] == "statistical":
                result = calc.statistics(data["data"])
            
            # Output as JSON
            output = {
                "result": result.result,
                "formula": result.formula_used,
                "steps": result.steps,
                "metadata": result.metadata
            }
            print(json.dumps(output, indent=2))
        
        else:
            print("Usage:")
            print("  python calculator_engine.py demo")
            print("  python calculator_engine.py json '<json_input>'")
    
    else:
        # Interactive mode
        print("INTERACTIVE MODE")
        print("Available calculators:")
        print("  1. Basic (add, subtract, multiply, divide, power)")
        print("  2. Scientific (sin, cos, tan, log, ln, sqrt, factorial)")
        print("  3. Financial (compound interest, loan payment)")
        print("  4. Statistical (mean, median, mode, std dev)")
        print("\nType 'exit' to quit\n")
        
        while True:
            try:
                choice = input("Select calculator (1-4) or 'exit': ").strip()
                
                if choice == 'exit':
                    break
                
                elif choice == '1':
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                    op = input("Operation (add/subtract/multiply/divide/power): ")
                    result = calc.basic_operation(a, b, op)
                    print(f"\nResult: {result.result}")
                    print(f"Formula: {result.formula_used}\n")
                
                elif choice == '2':
                    value = float(input("Enter value: "))
                    func = input("Function (sin/cos/tan/log/ln/sqrt/factorial): ")
                    result = calc.scientific_calculation(value, func)
                    print(f"\nResult: {result.result}")
                    print(f"Formula: {result.formula_used}\n")
                
                elif choice == '3':
                    calc_type = input("Type (compound/loan): ")
                    if calc_type == "compound":
                        p = float(input("Principal amount: $"))
                        r = float(input("Annual interest rate (%): "))
                        t = float(input("Time (years): "))
                        result = calc.compound_interest(p, r, t)
                        print(f"\nFinal Amount: ${result.result['amount']:,.2f}")
                        print(f"Interest Earned: ${result.result['interest']:,.2f}\n")
                    elif calc_type == "loan":
                        p = float(input("Loan amount: $"))
                        r = float(input("Annual interest rate (%): "))
                        y = int(input("Loan term (years): "))
                        result = calc.loan_payment(p, r, y)
                        print(f"\nMonthly Payment: ${result.result['monthly_payment']:,.2f}")
                        print(f"Total Interest: ${result.result['total_interest']:,.2f}\n")
                
                elif choice == '4':
                    data_input = input("Enter numbers separated by spaces: ")
                    data = [float(x) for x in data_input.split()]
                    result = calc.statistics(data)
                    print(f"\nStatistical Analysis:")
                    for step in result.steps:
                        print(f"  {step}")
                    print()
                
            except Exception as e:
                print(f"Error: {e}\n")
    
    print("\n" + "=" * 60)
    print("This demonstration shows how Claude Skills can include")
    print("Python scripts for complex calculations and processing.")
    print("=" * 60)


if __name__ == "__main__":
    main()
