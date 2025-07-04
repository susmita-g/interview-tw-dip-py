# Data Transformation Exercises
This repository contains **two exercises** designed to evaluate your ability to:
- Transform and validate JSON data against a schema
- Extract and flatten fields from nested objects
- Write clean, testable JavaScript code

---

## ✅ Prerequisites
Make sure you have **Python 3.7+** installed on your machine.
Then install dependencies:
**pip install fastavro pytest**

---

### Folder Structure
├── input.py                # Provided input object
├── schema.json             # Avro schema for validation (Exercise 1)
├── transform.py            # Write your transformation logic here (Exercise 1)
├── test_transform.test.js  # Unit test cases for transform
├── flatten.py              # Write your flattening logic here (Exercise 2)
├── test_flatten.py         # Unit test cases for flatten
├── index.py                # Entry point to run transformation and validate output

---

# 🧪 Exercise 1: Schema-Based Transformation

### 📋 Objective

Transform input1 from **input.py** to match the schema in **schema.json**. Your output will be validated using fastavro.

## ✅ Tasks
- Read the input1 from `input.py`
- Write transformation logic in `transform.py`
- Output must conform to `schema.json`
- Write test cases in `test_transform.test.py`


---


# Exercise 2: Flatten the Nested JSON

### 📋 Objective

Transform the given input object into the expected output as shown below.

## ✅ Tasks
- Read the input2 from `input.py`
- Write transformation logic in `flatten.py`
- Write test cases in `test_flatten.test.py`

## Expected Output:
{
  engine: "2.0L Turbo",
  fuel: "Gasoline",
  features: "Sunroof|Leather Seats|Keyless Entry",
  retail_price: "23000"
};


---


## Run the code
```bash
python index.py     # Executes transform logic and schema validation
pytest          # Runs test cases (if any)

--
