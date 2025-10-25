#!/usr/bin/env python3
"""
SKILL DEMONSTRATION SCRIPT
==========================
This script demonstrates how Claude Skills use Python for:
1. Complex calculations
2. Dynamic HTML generation
3. Data processing
4. Integration capabilities

Run this script to see the skill in action!
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from calculator_engine import CalculatorEngine
from generate_calculator import CalculatorGenerator
import json


def banner(text):
    """Create a formatted banner"""
    print("\n" + "=" * 60)
    print(f" {text}")
    print("=" * 60)


def demo_calculations():
    """Demonstrate calculation capabilities"""
    banner("DEMONSTRATION: Python Calculation Engine")
    print("\nThis shows how Claude Skills can perform complex calculations\n")
    
    calc = CalculatorEngine()
    
    # Basic calculation
    print("1. BASIC ARITHMETIC")
    result = calc.basic_operation(42, 8, "multiply")
    print(f"   Question: What is 42 × 8?")
    print(f"   Answer: {result.result}")
    print(f"   Formula: {result.formula_used}\n")
    
    # Scientific calculation
    print("2. SCIENTIFIC FUNCTION")
    result = calc.scientific_calculation(30, "sin")
    print(f"   Question: What is sin(30)?")
    print(f"   Answer: {result.result}")
    print(f"   Formula: {result.formula_used}\n")
    
    # Financial calculation
    print("3. LOAN CALCULATION")
    result = calc.loan_payment(200000, 4.5, 30)
    print(f"   Question: Monthly payment for $200,000 loan at 4.5% for 30 years?")
    print(f"   Answer: ${result.result['monthly_payment']:,.2f}/month")
    print(f"   Total Interest: ${result.result['total_interest']:,.2f}\n")
    
    # Statistical analysis
    print("4. STATISTICAL ANALYSIS")
    data = [23, 45, 67, 89, 12, 34, 56, 78, 90, 45, 33, 67]
    result = calc.statistics(data)
    print(f"   Data: {data}")
    print(f"   Mean: {result.result['mean']}")
    print(f"   Median: {result.result['median']}")
    print(f"   Std Dev: {result.result['std_dev']}\n")


def demo_generation():
    """Demonstrate HTML generation capabilities"""
    banner("DEMONSTRATION: HTML Calculator Generation")
    print("\nThis shows how Claude Skills can generate code dynamically\n")
    
    generator = CalculatorGenerator()
    
    # Generate different calculator types
    calculators = [
        {
            "name": "Scientific Calculator",
            "operations": ["add", "subtract", "multiply", "divide", "power"],
            "color": "blue"
        },
        {
            "name": "Finance Calculator",
            "operations": ["multiply", "divide", "power"],
            "color": "green"
        },
        {
            "name": "Simple Calculator",
            "operations": ["add", "subtract"],
            "color": "purple"
        }
    ]
    
    for calc_spec in calculators:
        html = generator.generate_basic_calculator(
            calc_spec["name"],
            calc_spec["operations"],
            calc_spec["color"]
        )
        
        filename = f"demo_{calc_spec['name'].replace(' ', '_').lower()}.html"
        path = generator.save_calculator(html, filename)
        
        print(f"✅ Generated: {calc_spec['name']}")
        print(f"   Operations: {', '.join(calc_spec['operations'])}")
        print(f"   Theme: {calc_spec['color']}")
        print(f"   File: {path}\n")
    
    # Generate specialized calculator
    print("✅ Generated: BMI Calculator (Specialized)")
    html = generator.generate_specialized_calculator("bmi")
    path = generator.save_calculator(html, "demo_bmi_calculator.html")
    print(f"   Type: Health/Fitness")
    print(f"   Features: Metric/Imperial units")
    print(f"   File: {path}\n")


def show_skill_structure():
    """Show how the skill is organized"""
    banner("SKILL STRUCTURE EXPLANATION")
    
    print("""
This Claude Skill is organized as follows:

📁 simple-calculator-skill/
│
├── 📄 SKILL.md              # Main instructions for Claude
│   └─ Tells Claude:
│      • When to use this skill
│      • How to create calculators
│      • Best practices to follow
│
├── 📁 templates/            # Reusable HTML templates
│   ├── basic-calculator.html
│   └── percentage-calculator.html
│
├── 📁 scripts/              # Python execution scripts
│   ├── 🐍 calculator_engine.py
│   │   └─ Performs complex calculations
│   ├── 🐍 generate_calculator.py
│   │   └─ Creates HTML programmatically
│   └── 🐍 demo.py (this file)
│       └─ Demonstrates the skill
│
├── 📁 examples/             # Complete examples
│   ├── tip-calculator.html
│   └── python-powered-demo.html
│
└── 📁 references/           # Documentation
    └── formulas.md          # Mathematical formulas
    """)


def explain_how_it_works():
    """Explain how Claude uses this skill"""
    banner("HOW CLAUDE USES THIS SKILL")
    
    print("""
When you upload this skill to Claude and ask for a calculator:

1️⃣  CLAUDE READS THE SKILL
    • Loads SKILL.md for instructions
    • Identifies available templates and scripts
    • Understands the workflow to follow

2️⃣  CLAUDE ANALYZES YOUR REQUEST
    • "Create a tip calculator" → Uses templates
    • "Calculate compound interest" → Uses Python engine
    • "Generate 5 calculators" → Uses generator script

3️⃣  CLAUDE EXECUTES THE APPROPRIATE METHOD
    
    For HTML Templates:
    • Selects appropriate template
    • Customizes based on requirements
    • Adds educational comments
    
    For Python Calculations:
    • Runs calculator_engine.py
    • Performs complex math
    • Returns formatted results
    
    For Dynamic Generation:
    • Executes generate_calculator.py
    • Creates customized HTML
    • Saves output files

4️⃣  CLAUDE DELIVERS THE RESULT
    • Provides working calculator
    • Explains how it works
    • Includes documentation
    """)


def show_benefits():
    """Show the benefits of using skills"""
    banner("BENEFITS OF CLAUDE SKILLS")
    
    print("""
🎯 CONSISTENCY
   • Same quality every time
   • Follows best practices
   • Reduces errors

⚡ EFFICIENCY
   • Reusable templates
   • No need to recreate from scratch
   • Faster development

📚 KNOWLEDGE ORGANIZATION
   • Structured approach
   • Clear documentation
   • Easy to understand

🔧 CUSTOMIZATION
   • Modify templates
   • Add new functions
   • Extend capabilities

🐍 ADVANCED FEATURES
   • Execute Python code
   • Complex calculations
   • Data processing
   • File generation

📖 EDUCATIONAL VALUE
   • Shows how things work
   • Includes explanations
   • Demystifies the process
    """)


def interactive_menu():
    """Interactive menu for demonstrations"""
    while True:
        banner("CLAUDE SKILL DEMONSTRATION")
        print("\n📚 Choose a demonstration:\n")
        print("1. Show Skill Structure")
        print("2. Demonstrate Calculations")
        print("3. Generate Calculators")
        print("4. Explain How It Works")
        print("5. Show Benefits")
        print("6. Run Everything")
        print("0. Exit")
        
        choice = input("\nSelect option (0-6): ").strip()
        
        if choice == "0":
            print("\n👋 Thanks for exploring Claude Skills!")
            break
        elif choice == "1":
            show_skill_structure()
        elif choice == "2":
            demo_calculations()
        elif choice == "3":
            demo_generation()
        elif choice == "4":
            explain_how_it_works()
        elif choice == "5":
            show_benefits()
        elif choice == "6":
            show_skill_structure()
            demo_calculations()
            demo_generation()
            explain_how_it_works()
            show_benefits()
        else:
            print("\n❌ Invalid option. Please try again.")
        
        if choice != "0":
            input("\nPress Enter to continue...")


def main():
    """Main entry point"""
    # Check for command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "calc":
            demo_calculations()
        elif sys.argv[1] == "generate":
            demo_generation()
        elif sys.argv[1] == "structure":
            show_skill_structure()
        elif sys.argv[1] == "explain":
            explain_how_it_works()
        elif sys.argv[1] == "benefits":
            show_benefits()
        elif sys.argv[1] == "all":
            show_skill_structure()
            demo_calculations()
            demo_generation()
            explain_how_it_works()
            show_benefits()
        else:
            print("Usage: python demo.py [calc|generate|structure|explain|benefits|all]")
    else:
        # Run interactive menu
        interactive_menu()
    
    banner("END OF DEMONSTRATION")
    print("""
This demonstration showed how Claude Skills work:
• They're not magic - just organized instructions and code
• They can execute Python for complex operations
• They provide templates for common patterns
• They're completely transparent and understandable

You can modify this skill to:
• Add new calculator types
• Include more complex calculations
• Customize the styling
• Extend the Python capabilities

Upload this skill to Claude to see it in action!
    """)


if __name__ == "__main__":
    main()
