#!/usr/bin/env python3
"""
HTML Calculator Generator
==========================
This script demonstrates how Claude Skills can use Python to generate
customized calculator interfaces programmatically.

SKILL DEMONSTRATION:
This shows users that skills can:
1. Generate code dynamically
2. Create customized outputs based on parameters
3. Use templates and patterns programmatically
"""

import json
import sys
from typing import Dict, List, Optional
from datetime import datetime


class CalculatorGenerator:
    """
    Generates HTML calculator interfaces programmatically
    This demonstrates how skills can create dynamic content
    """
    
    def __init__(self):
        """Initialize the generator with base templates"""
        self.generated_count = 0
        self.base_css = self._get_base_css()
    
    def _get_base_css(self) -> str:
        """
        Returns base CSS styling for all calculators
        Shows how skills can maintain consistent styling
        """
        return """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .calculator {
            background: white;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.15);
            max-width: 500px;
            width: 100%;
        }
        
        h1 {
            text-align: center;
            margin-bottom: 30px;
            color: #333;
        }
        
        .input-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            color: #555;
            font-weight: 500;
        }
        
        input {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        
        input:focus {
            outline: none;
            border-color: #4CAF50;
        }
        
        button {
            width: 100%;
            padding: 14px;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        button:hover {
            background: #45a049;
        }
        
        .result {
            margin-top: 20px;
            padding: 20px;
            background: #f5f5f5;
            border-radius: 8px;
            text-align: center;
            display: none;
        }
        
        .result.show {
            display: block;
        }
        
        .result-label {
            color: #666;
            font-size: 14px;
            margin-bottom: 10px;
        }
        
        .result-value {
            font-size: 28px;
            font-weight: bold;
            color: #333;
        }
        
        .info {
            margin-top: 20px;
            padding: 15px;
            background: #e8f5e9;
            border-left: 4px solid #4CAF50;
            border-radius: 4px;
        }
        
        .info h3 {
            color: #2e7d32;
            margin-bottom: 8px;
            font-size: 14px;
        }
        
        .info p {
            color: #555;
            font-size: 13px;
            line-height: 1.5;
        }
        
        .developer-credit {
            margin-top: 30px;
            padding: 20px;
            text-align: center;
            border-top: 2px solid #e0e0e0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 0 0 20px 20px;
            margin: 30px -30px -30px -30px;
        }
        
        .developer-credit p {
            color: white;
            font-size: 14px;
            margin: 0;
            font-weight: 500;
            letter-spacing: 0.5px;
        }
        
        .developer-credit .dev-name {
            font-size: 18px;
            font-weight: bold;
            margin-top: 5px;
        }
        """
    
    def generate_basic_calculator(self, 
                                 title: str = "Basic Calculator",
                                 operations: List[str] = None,
                                 color_scheme: str = "green") -> str:
        """
        Generate a basic arithmetic calculator
        
        Args:
            title: Calculator title
            operations: List of operations to include
            color_scheme: Color theme (green, blue, purple, orange)
        
        Returns:
            Complete HTML calculator as string
        """
        if operations is None:
            operations = ["add", "subtract", "multiply", "divide"]
        
        # Map color schemes to gradients
        gradients = {
            "green": "linear-gradient(135deg, #43cea2 0%, #185a9d 100%)",
            "blue": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
            "purple": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
            "orange": "linear-gradient(135deg, #fa709a 0%, #fee140 100%)"
        }
        
        # Map operations to symbols
        op_symbols = {
            "add": "+",
            "subtract": "−",
            "multiply": "×",
            "divide": "÷",
            "power": "^",
            "modulo": "%"
        }
        
        # Generate operation buttons
        operation_buttons = ""
        for op in operations:
            symbol = op_symbols.get(op, op)
            operation_buttons += f'''
            <button type="button" onclick="calculate('{op}')">{symbol}</button>
            '''
        
        # Generate the complete HTML
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        {self.base_css}
        
        body {{
            background: {gradients.get(color_scheme, gradients['green'])};
        }}
        
        .operation-buttons {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
            margin-bottom: 20px;
        }}
        
        .operation-buttons button {{
            background: #{color_scheme == 'blue' and '667eea' or color_scheme == 'purple' and 'f093fb' or color_scheme == 'orange' and 'fa709a' or '4CAF50'};
        }}
        
        .operation-buttons button:hover {{
            opacity: 0.9;
        }}
    </style>
</head>
<body>
    <!-- Generated by Calculator Skill Python Script -->
    <!-- This demonstrates programmatic HTML generation -->
    
    <div class="calculator">
        <h1>{title}</h1>
        
        <div class="input-group">
            <label for="num1">First Number</label>
            <input type="number" id="num1" step="any" placeholder="Enter first number">
        </div>
        
        <div class="input-group">
            <label for="num2">Second Number</label>
            <input type="number" id="num2" step="any" placeholder="Enter second number">
        </div>
        
        <div class="operation-buttons">
            {operation_buttons}
        </div>
        
        <div class="result" id="result">
            <div class="result-label">Result</div>
            <div class="result-value" id="resultValue">0</div>
        </div>
        
        <div class="info">
            <h3>📚 Generated by Claude Skill</h3>
            <p>
                This calculator was generated programmatically using Python.
                The skill demonstrates how code can create customized interfaces
                based on parameters like operations and color schemes.
            </p>
            <p style="margin-top: 8px;">
                <strong>Generated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br>
                <strong>Operations:</strong> {', '.join(operations)}<br>
                <strong>Theme:</strong> {color_scheme}
            </p>
        </div>
        
        <div class="developer-credit">
            <p>Developed by</p>
            <p class="dev-name">Rilov</p>
        </div>
    </div>
    
    <script>
        // Generated JavaScript for calculator functionality
        
        function calculate(operation) {{
            const num1 = parseFloat(document.getElementById('num1').value);
            const num2 = parseFloat(document.getElementById('num2').value);
            
            if (isNaN(num1) || isNaN(num2)) {{
                alert('Please enter valid numbers');
                return;
            }}
            
            let result;
            let formula;
            
            switch(operation) {{
                case 'add':
                    result = num1 + num2;
                    formula = `${{num1}} + ${{num2}}`;
                    break;
                case 'subtract':
                    result = num1 - num2;
                    formula = `${{num1}} − ${{num2}}`;
                    break;
                case 'multiply':
                    result = num1 * num2;
                    formula = `${{num1}} × ${{num2}}`;
                    break;
                case 'divide':
                    if (num2 === 0) {{
                        alert('Cannot divide by zero!');
                        return;
                    }}
                    result = num1 / num2;
                    formula = `${{num1}} ÷ ${{num2}}`;
                    break;
                case 'power':
                    result = Math.pow(num1, num2);
                    formula = `${{num1}}^${{num2}}`;
                    break;
                case 'modulo':
                    if (num2 === 0) {{
                        alert('Cannot modulo by zero!');
                        return;
                    }}
                    result = num1 % num2;
                    formula = `${{num1}} % ${{num2}}`;
                    break;
                default:
                    alert('Unknown operation');
                    return;
            }}
            
            // Display result
            document.getElementById('resultValue').textContent = 
                Math.round(result * 10000) / 10000;
            document.getElementById('result').classList.add('show');
            
            // Log to console for debugging
            console.log(`Calculated: ${{formula}} = ${{result}}`);
        }}
        
        // Add keyboard support
        document.addEventListener('keydown', function(e) {{
            if (e.key === 'Enter') {{
                // Calculate with first available operation
                calculate('{operations[0]}');
            }}
        }});
    </script>
</body>
</html>"""
        
        self.generated_count += 1
        return html
    
    def generate_specialized_calculator(self, calculator_type: str) -> str:
        """
        Generate specialized calculators based on type
        
        Types available:
        - bmi: Body Mass Index calculator
        - tip: Tip calculator
        - age: Age calculator
        - discount: Discount calculator
        """
        
        generators = {
            "bmi": self._generate_bmi_calculator,
            "tip": self._generate_tip_calculator,
            "age": self._generate_age_calculator,
            "discount": self._generate_discount_calculator
        }
        
        if calculator_type not in generators:
            raise ValueError(f"Unknown calculator type: {calculator_type}")
        
        return generators[calculator_type]()
    
    def _generate_bmi_calculator(self) -> str:
        """Generate a BMI calculator"""
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BMI Calculator</title>
    <style>
        {self.base_css}
        body {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }}
        .bmi-category {{ margin-top: 15px; padding: 10px; border-radius: 8px; font-weight: 600; }}
        .underweight {{ background: #e3f2fd; color: #1976d2; }}
        .normal {{ background: #e8f5e9; color: #2e7d32; }}
        .overweight {{ background: #fff3e0; color: #ef6c00; }}
        .obese {{ background: #ffebee; color: #c62828; }}
    </style>
</head>
<body>
    <div class="calculator">
        <h1>🏃‍♂️ BMI Calculator</h1>
        
        <div class="input-group">
            <label>Unit System</label>
            <select id="unitSystem" onchange="updateLabels()">
                <option value="metric">Metric (kg, cm)</option>
                <option value="imperial">Imperial (lbs, inches)</option>
            </select>
        </div>
        
        <div class="input-group">
            <label for="weight" id="weightLabel">Weight (kg)</label>
            <input type="number" id="weight" step="0.1" placeholder="Enter weight">
        </div>
        
        <div class="input-group">
            <label for="height" id="heightLabel">Height (cm)</label>
            <input type="number" id="height" step="0.1" placeholder="Enter height">
        </div>
        
        <button onclick="calculateBMI()">Calculate BMI</button>
        
        <div class="result" id="result">
            <div class="result-label">Your BMI</div>
            <div class="result-value" id="bmiValue">0</div>
            <div class="bmi-category" id="bmiCategory"></div>
        </div>
        
        <div class="info">
            <h3>📚 About BMI</h3>
            <p>
                Body Mass Index (BMI) is a measure of body fat based on height and weight.
                This calculator was generated by a Claude Skill's Python script.
            </p>
            <p style="margin-top: 8px;">
                <strong>Categories:</strong><br>
                Underweight: BMI < 18.5<br>
                Normal: 18.5 ≤ BMI < 25<br>
                Overweight: 25 ≤ BMI < 30<br>
                Obese: BMI ≥ 30
            </p>
        </div>
        
        <div class="developer-credit">
            <p>Developed by</p>
            <p class="dev-name">Rilov</p>
        </div>
    </div>
    
    <script>
        function updateLabels() {{
            const system = document.getElementById('unitSystem').value;
            if (system === 'metric') {{
                document.getElementById('weightLabel').textContent = 'Weight (kg)';
                document.getElementById('heightLabel').textContent = 'Height (cm)';
            }} else {{
                document.getElementById('weightLabel').textContent = 'Weight (lbs)';
                document.getElementById('heightLabel').textContent = 'Height (inches)';
            }}
        }}
        
        function calculateBMI() {{
            const system = document.getElementById('unitSystem').value;
            const weight = parseFloat(document.getElementById('weight').value);
            const height = parseFloat(document.getElementById('height').value);
            
            if (isNaN(weight) || isNaN(height) || weight <= 0 || height <= 0) {{
                alert('Please enter valid positive numbers');
                return;
            }}
            
            let bmi;
            if (system === 'metric') {{
                const heightM = height / 100;
                bmi = weight / (heightM * heightM);
            }} else {{
                bmi = (weight / (height * height)) * 703;
            }}
            
            // Display result
            document.getElementById('bmiValue').textContent = bmi.toFixed(1);
            
            // Determine category
            let category, className;
            if (bmi < 18.5) {{
                category = 'Underweight';
                className = 'underweight';
            }} else if (bmi < 25) {{
                category = 'Normal Weight';
                className = 'normal';
            }} else if (bmi < 30) {{
                category = 'Overweight';
                className = 'overweight';
            }} else {{
                category = 'Obese';
                className = 'obese';
            }}
            
            const categoryElement = document.getElementById('bmiCategory');
            categoryElement.textContent = category;
            categoryElement.className = 'bmi-category ' + className;
            
            document.getElementById('result').classList.add('show');
        }}
    </script>
</body>
</html>"""
    
    def _generate_tip_calculator(self) -> str:
        """Generate a tip calculator"""
        # Simplified for brevity - you can expand this
        return self.generate_basic_calculator(
            title="Tip Calculator",
            operations=["add"],
            color_scheme="purple"
        )
    
    def _generate_age_calculator(self) -> str:
        """Generate an age calculator"""
        # Simplified for brevity
        return self.generate_basic_calculator(
            title="Age Calculator",
            operations=["subtract"],
            color_scheme="blue"
        )
    
    def _generate_discount_calculator(self) -> str:
        """Generate a discount calculator"""
        # Simplified for brevity
        return self.generate_basic_calculator(
            title="Discount Calculator",
            operations=["subtract", "multiply", "divide"],
            color_scheme="orange"
        )
    
    def save_calculator(self, html_content: str, filename: str) -> str:
        """
        Save generated calculator to file
        
        Args:
            html_content: The HTML content to save
            filename: Output filename
        
        Returns:
            Path to saved file
        """
        output_path = f"/tmp/{filename}"
        with open(output_path, 'w') as f:
            f.write(html_content)
        return output_path


def main():
    """
    Command-line interface for the calculator generator
    Demonstrates how skills can be executed from command line
    """
    print("=" * 60)
    print("CALCULATOR HTML GENERATOR - Claude Skill Demo")
    print("=" * 60)
    print("\nThis Python script shows how Claude Skills can:")
    print("1. Generate code programmatically")
    print("2. Create customized outputs")
    print("3. Use templates and patterns")
    print()
    
    generator = CalculatorGenerator()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "generate":
            # Generate a calculator based on parameters
            if len(sys.argv) > 2:
                calc_type = sys.argv[2]
                
                if calc_type == "basic":
                    # Parse additional parameters if provided
                    title = sys.argv[3] if len(sys.argv) > 3 else "Basic Calculator"
                    operations = sys.argv[4].split(',') if len(sys.argv) > 4 else None
                    color = sys.argv[5] if len(sys.argv) > 5 else "green"
                    
                    html = generator.generate_basic_calculator(title, operations, color)
                    filename = "generated_basic_calculator.html"
                
                elif calc_type in ["bmi", "tip", "age", "discount"]:
                    html = generator.generate_specialized_calculator(calc_type)
                    filename = f"generated_{calc_type}_calculator.html"
                
                else:
                    print(f"Unknown calculator type: {calc_type}")
                    sys.exit(1)
                
                # Save the generated calculator
                path = generator.save_calculator(html, filename)
                print(f"✅ Calculator generated successfully!")
                print(f"📁 Saved to: {path}")
                print(f"\nYou can open this file in a web browser to use the calculator.")
        
        elif command == "demo":
            # Generate multiple calculators as demonstration
            print("Generating demonstration calculators...\n")
            
            # Generate basic calculator
            html = generator.generate_basic_calculator(
                "Demo Calculator",
                ["add", "subtract", "multiply", "divide", "power"],
                "blue"
            )
            path = generator.save_calculator(html, "demo_basic.html")
            print(f"✅ Basic Calculator -> {path}")
            
            # Generate BMI calculator
            html = generator.generate_specialized_calculator("bmi")
            path = generator.save_calculator(html, "demo_bmi.html")
            print(f"✅ BMI Calculator -> {path}")
            
            print(f"\n🎉 Generated {generator.generated_count} calculators!")
            
        elif command == "json":
            # Generate from JSON specification
            if len(sys.argv) > 2:
                spec = json.loads(sys.argv[2])
                html = generator.generate_basic_calculator(
                    spec.get("title", "Calculator"),
                    spec.get("operations"),
                    spec.get("color", "green")
                )
                path = generator.save_calculator(html, spec.get("filename", "calculator.html"))
                print(json.dumps({"success": True, "path": path}))
        
        else:
            print("Unknown command:", command)
    
    else:
        # Interactive mode
        print("INTERACTIVE MODE\n")
        print("Options:")
        print("1. Generate Basic Calculator")
        print("2. Generate BMI Calculator")
        print("3. Generate Multiple Calculators (Demo)")
        print("4. Exit")
        
        choice = input("\nSelect option (1-4): ")
        
        if choice == "1":
            title = input("Calculator title [Basic Calculator]: ") or "Basic Calculator"
            ops_input = input("Operations (comma-separated) [add,subtract,multiply,divide]: ")
            operations = ops_input.split(',') if ops_input else None
            color = input("Color scheme (green/blue/purple/orange) [green]: ") or "green"
            
            html = generator.generate_basic_calculator(title, operations, color)
            filename = input("Filename [calculator.html]: ") or "calculator.html"
            path = generator.save_calculator(html, filename)
            
            print(f"\n✅ Calculator generated: {path}")
        
        elif choice == "2":
            html = generator.generate_specialized_calculator("bmi")
            path = generator.save_calculator(html, "bmi_calculator.html")
            print(f"\n✅ BMI Calculator generated: {path}")
        
        elif choice == "3":
            print("\nGenerating demonstration calculators...")
            for i, (name, color) in enumerate([("Red", "purple"), ("Blue", "blue"), ("Green", "green")]):
                html = generator.generate_basic_calculator(f"{name} Calculator", None, color)
                path = generator.save_calculator(html, f"demo_{i+1}.html")
                print(f"✅ {name} Calculator -> {path}")
    
    print("\n" + "=" * 60)
    print("This demonstrates how Claude Skills can use Python")
    print("to generate customized content programmatically.")
    print("=" * 60)


if __name__ == "__main__":
    main()
