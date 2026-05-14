# testEBSA

## Calculator

A simple command-line calculator written in Python that supports basic arithmetic operations.

### Operations

| Operator | Operation      |
|----------|----------------|
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |

### Usage

Run the interactive calculator:

```bash
python calculator.py
```

Example session:

```
Simple Calculator
Operations: +, -, *, /
Type 'quit' to exit.

Enter expression (e.g. 3 + 4): 10 + 5
Result: 15
Enter expression (e.g. 3 + 4): 7 / 2
Result: 3.5
Enter expression (e.g. 3 + 4): quit
Goodbye!
```

### Use as a Library

```python
from calculator import add, subtract, multiply, divide

add(2, 3)       # 5
subtract(10, 4) # 6
multiply(3, 4)  # 12
divide(10, 2)   # 5.0
```

### Tests

```bash
python -m pytest test_calculator.py -v
```