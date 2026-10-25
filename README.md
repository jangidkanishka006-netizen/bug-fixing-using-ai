# Bug Fixing Using AI

## About the Project
This project demonstrates debugging a Python program by identifying and fixing logical errors and a division-by-zero error.

## Files
- `buggy_code.py` — Original program containing intentional bugs.
- `fixed_code.py` — Corrected and improved version.

## Bugs Identified and Fixed

### Bug 1: Division by Zero
**Problem:** The original code divided the total marks by zero, causing a `ZeroDivisionError`.

**Solution:** Divide the total marks by the number of marks. An empty list is handled separately.

### Bug 2: Incorrect Pass/Fail Logic
**Problem:** The program displayed "Fail" when the average was 40 or more.

**Solution:** Corrected the condition so an average of 40 or more results in "Pass".

## Technologies Used
- Python 3
- AI-assisted debugging concepts

## Sample Output
```text
Average Marks: 73.33333333333333
Result: Pass
```

## What I Learned
- Identifying runtime errors.
- Finding logical errors.
- Testing corrected code.
- Improving code readability.
- Understanding AI-assisted debugging.

## How to Run
```bash
python buggy_code.py
python fixed_code.py
```

Note: The buggy version intentionally raises an error. Run the fixed version to see the correct output.

## Author
Kanishka Jangid
