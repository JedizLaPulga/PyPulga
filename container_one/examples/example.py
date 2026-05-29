import sys
import os
# Add the parent directory to the path so we can import the built module directly for testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

try:
    from pulgapy.container_one import sum_as_string
    result = sum_as_string(5, 10)
    print(f"Result from Rust: {result}")
except ImportError as e:
    print(f"Error: {e}")
    print("Please make sure you have compiled the Rust extension using `python setup.py build_ext --inplace`")
