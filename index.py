import json
from transform import transform
with open("input.json", "r") as f:
    data = json.load(f)
input1 = data["input1"]
from fastavro.validation import validate
import fastavro

# Load schema
with open("schema.json") as f:
    schema = json.load(f)

# ===== TRANSFORM LOGIC STARTS HERE =====
transformed = transform(input1)




# ===== TRANSFORM LOGIC ENDS HERE =====


# Validate output
if validate(transformed, schema):
    print("\n✅ Schema validation passed")
else:
    print("\n❌ Schema validation failed")
