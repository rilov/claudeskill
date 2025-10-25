# Calculator Formulas Reference

## Understanding This Reference
This file demonstrates how Claude Skills provide reference materials. When Claude uses this skill, it can look up these formulas to ensure accuracy and consistency.

---

## Basic Arithmetic

### Addition
```
result = a + b
```

### Subtraction
```
result = a - b
```

### Multiplication
```
result = a × b
```

### Division
```
result = a ÷ b
// Note: Check for division by zero!
```

---

## Percentage Calculations

### Find X% of Y
```javascript
result = (X / 100) × Y
// Example: 20% of 150 = (20/100) × 150 = 30
```

### What percentage is X of Y?
```javascript
percentage = (X / Y) × 100
// Example: 30 is what % of 150? = (30/150) × 100 = 20%
```

### Percentage Change
```javascript
change = ((new_value - old_value) / old_value) × 100
// Positive result = increase
// Negative result = decrease
```

---

## Financial Calculations

### Simple Interest
```javascript
interest = principal × rate × time
// principal: initial amount
// rate: interest rate (as decimal)
// time: time period
```

### Compound Interest
```javascript
amount = principal × (1 + rate/n)^(n×t)
// n: number of times interest compounds per year
// t: number of years
```

### Monthly Loan Payment
```javascript
payment = principal × (r(1+r)^n) / ((1+r)^n - 1)
// r: monthly interest rate (annual rate / 12)
// n: total number of payments
```

---

## Unit Conversions

### Temperature
```javascript
// Celsius to Fahrenheit
F = (C × 9/5) + 32

// Fahrenheit to Celsius
C = (F - 32) × 5/9

// Celsius to Kelvin
K = C + 273.15
```

### Length
```javascript
// Common conversions
1 inch = 2.54 cm
1 foot = 12 inches = 30.48 cm
1 meter = 100 cm = 3.281 feet
1 mile = 5280 feet = 1.609 km
1 km = 1000 m = 0.621 miles
```

### Weight
```javascript
// Common conversions
1 pound = 0.453592 kg
1 kg = 2.20462 pounds
1 ounce = 28.3495 grams
1 gram = 0.035274 ounces
```

---

## Health Calculations

### BMI (Body Mass Index)
```javascript
// Metric
BMI = weight_kg / (height_m × height_m)

// Imperial
BMI = (weight_lbs / (height_inches × height_inches)) × 703
```

### BMI Categories
- Underweight: < 18.5
- Normal: 18.5 - 24.9
- Overweight: 25 - 29.9
- Obese: ≥ 30

### Daily Calorie Needs (Mifflin-St Jeor)
```javascript
// For men
BMR = (10 × weight_kg) + (6.25 × height_cm) - (5 × age) + 5

// For women
BMR = (10 × weight_kg) + (6.25 × height_cm) - (5 × age) - 161

// Total daily calories = BMR × activity_factor
// Sedentary: 1.2, Light: 1.375, Moderate: 1.55, Active: 1.725
```

---

## Geometry

### Circle
```javascript
circumference = 2 × π × radius
area = π × radius²
```

### Rectangle
```javascript
perimeter = 2 × (length + width)
area = length × width
```

### Triangle
```javascript
area = (base × height) / 2
// Pythagorean theorem
c² = a² + b²
```

---

## Statistics

### Mean (Average)
```javascript
mean = sum_of_all_values / number_of_values
```

### Median
```javascript
// Sort values, then:
// If odd number of values: middle value
// If even number of values: average of two middle values
```

### Standard Deviation
```javascript
1. Calculate mean
2. For each value: (value - mean)²
3. Sum all squared differences
4. Divide by (n-1) for sample, or n for population
5. Take square root
```

---

## Tips for Implementation

### Always Include:
1. **Input validation** - Check for valid numbers
2. **Error handling** - Division by zero, negative values where inappropriate
3. **Precision control** - Round results appropriately
4. **Clear units** - Always show what units the result is in

### Best Practices:
- Use `parseFloat()` for decimal numbers
- Use `toFixed()` to control decimal places
- Check for `isNaN()` before calculations
- Provide clear error messages
- Include reset functionality

---

## How Skills Use This Reference

When Claude creates a calculator using this skill, it:
1. **Looks up the appropriate formula** from this reference
2. **Implements it correctly** with proper validation
3. **Adds educational comments** explaining the math
4. **Ensures accuracy** by following these tested formulas

This reference file demonstrates how Claude Skills provide reliable, reusable knowledge that ensures consistency and quality in outputs.
