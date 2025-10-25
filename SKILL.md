---
name: calculator-builder-by-rilov
description: Creates interactive calculators with clear explanations. This skill demonstrates how Claude Skills work by showing structured guidance, templates, and best practices for a specific task.
---

# Rilov's Calculator Builder Skill

## 🎯 What This Skill Does

This skill helps Claude create simple, interactive calculators with HTML/JavaScript. It's designed to be educational - showing users how Claude Skills provide:
1. **Structured guidance** - Step-by-step instructions
2. **Templates** - Reusable code patterns
3. **Best practices** - Quality standards and tips
4. **Examples** - Reference implementations

---

## 📚 How Claude Skills Work

When you upload this skill, Claude gains specialized knowledge for this specific task. Think of it as giving Claude a "recipe book" that it follows when you ask for a calculator.

**The skill contains:**
- Instructions (this SKILL.md file)
- Templates (in /templates folder)
- Examples (in /examples folder)
- References (additional guidance)

---

## 🛠️ Calculator Creation Workflow

When a user asks for a calculator, follow these steps:

### Step 1: Identify Calculator Type
Determine what kind of calculator is needed:
- **Basic Math** (addition, subtraction, multiplication, division)
- **Financial** (loan, interest, investment)
- **Unit Converter** (length, weight, temperature)
- **Health** (BMI, calorie, water intake)
- **Custom** (user-specific requirements)

### Step 2: Use the Appropriate Template
Navigate to `/templates` and select the matching template:
- `basic-calculator.html` - For simple arithmetic
- `financial-calculator.html` - For money calculations
- `converter-calculator.html` - For unit conversions
- `health-calculator.html` - For health metrics

### Step 3: Customize the Template
Modify the template based on user requirements:
1. Update the title and description
2. Adjust input fields and labels
3. Modify calculation logic
4. Customize styling and colors
5. Add validation and error handling

### Step 4: Add Educational Comments
**IMPORTANT**: Since this skill is about demystifying how things work, always add clear comments explaining:
- What each section does
- How the calculations work
- Why certain approaches are used
- How users can modify it

### Step 5: Add Branding
**IMPORTANT**: Every calculator must include:
- Footer with "Developed by Rilov"
- Professional styling for the signature
- Link or credit line visible but not intrusive

### Step 6: Test and Deliver
Create the calculator as an HTML artifact and include:
- Clear instructions for use
- Explanation of the calculation logic
- Tips for customization
- Developer credit: "Developed by Rilov"

---

## 💡 Best Practices

### Always Include:
1. **Input validation** - Check for valid numbers
2. **Clear labels** - Explain what each field is for
3. **Result formatting** - Make outputs readable (decimals, commas, units)
4. **Reset button** - Allow users to start over
5. **Responsive design** - Work on mobile and desktop
6. **Developer credit** - "Developed by Rilov" in footer

### Code Style:
```javascript
// GOOD: Clear variable names and comments
function calculateBMI(weightKg, heightM) {
    // BMI = weight in kg / (height in meters)²
    const bmi = weightKg / (heightM * heightM);
    return bmi.toFixed(1); // Round to 1 decimal place
}

// BAD: Unclear code
function calc(w, h) {
    return w/(h*h);
}
```

---

## 📝 Example Response Pattern

When someone asks: "Create a tip calculator"

1. **Acknowledge**: "I'll create a tip calculator for you using my calculator-building skill!"

2. **Explain the approach**: "This will calculate tips based on bill amount and service quality, with options for splitting the bill."

3. **Create the calculator**: Use the template and customize it

4. **Add educational value**: Include comments explaining:
   - How tip percentages work
   - The calculation formula
   - How to modify tip percentages
   - How to add more features

5. **Provide the deliverable**: Create an HTML artifact with the working calculator

---

## 🎓 Educational Components

Always explain these concepts when creating calculators:

1. **HTML Structure**:
   - How forms collect user input
   - Why we use specific input types (number, range, etc.)
   - The importance of labels for accessibility

2. **JavaScript Logic**:
   - How event listeners work
   - Why we validate inputs
   - How calculations are performed
   - Error handling strategies

3. **CSS Styling**:
   - How to make calculators visually appealing
   - Responsive design principles
   - User experience considerations

---

## 🐍 Python Script Execution

### Advanced Calculations with Python
This skill includes Python scripts that demonstrate how Claude can:
- Execute custom code for complex calculations
- Generate calculators programmatically
- Process data and create visualizations
- Provide command-line interfaces

### Available Python Scripts:

#### 1. Calculator Engine (`/scripts/calculator_engine.py`)
A comprehensive calculation engine that handles:
- Basic arithmetic operations
- Scientific functions (sin, cos, log, etc.)
- Financial calculations (compound interest, loan payments)
- Statistical analysis (mean, median, standard deviation)
- Function graphing (if matplotlib available)

**Usage Examples:**
```bash
# Run demonstration
python calculator_engine.py demo

# Use with JSON input
python calculator_engine.py json '{"type":"basic","a":10,"b":5,"operation":"multiply"}'

# Interactive mode
python calculator_engine.py
```

#### 2. HTML Generator (`/scripts/generate_calculator.py`)
Generates customized calculator HTML files programmatically:
- Creates calculators with specified operations
- Customizable color schemes
- Specialized calculators (BMI, tip, etc.)

**Usage Examples:**
```bash
# Generate basic calculator
python generate_calculator.py generate basic "My Calculator" "add,subtract,multiply" blue

# Generate BMI calculator
python generate_calculator.py generate bmi

# Run demonstration
python generate_calculator.py demo
```

### How Python Scripts Enhance This Skill:

1. **Complex Calculations**: Handle advanced math that's difficult in JavaScript
2. **Dynamic Generation**: Create customized calculators based on parameters
3. **Data Processing**: Analyze datasets and generate statistics
4. **Automation**: Batch generate multiple calculators
5. **Integration**: Can be called from other systems via command line

## 🚀 Quick Start Examples

### Example 1: Percentage Calculator
```javascript
// This function calculates what X% of a number is
function calculatePercentage(number, percentage) {
    // Convert percentage to decimal (50% = 0.5)
    const decimal = percentage / 100;
    // Multiply the number by the decimal
    return number * decimal;
}
```

### Example 2: Compound Interest
```javascript
// Calculate compound interest
function compoundInterest(principal, rate, time, n) {
    // A = P(1 + r/n)^(nt)
    // Where: P = principal, r = rate, t = time, n = compounds per year
    const amount = principal * Math.pow((1 + rate/n), n*time);
    return amount.toFixed(2);
}
```

---

## 🎯 Success Metrics

A well-built calculator should:
- ✅ Work correctly with valid inputs
- ✅ Handle invalid inputs gracefully
- ✅ Be easy to understand and use
- ✅ Include clear explanations
- ✅ Be modifiable by users
- ✅ Look professional and clean

---

## 📚 Additional Resources

Direct users to these locations within the skill:
- `/templates/` - Pre-built calculator templates
- `/examples/` - Complete calculator examples
- `/references/formulas.md` - Common calculation formulas
- `/references/styling.css` - Reusable CSS styles

---

## 🤝 User Guidance

If a user wants to understand how this skill works, explain:

1. **Skills are instruction sets** - They tell Claude how to approach specific tasks
2. **Templates provide structure** - Reusable patterns for common needs
3. **Best practices ensure quality** - Guidelines for creating good outputs
4. **Examples show possibilities** - Demonstrate what can be built

This skill is intentionally simple and transparent to help users understand how Claude Skills enhance Claude's capabilities for specific tasks!
