import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

try:
    from pulgapy.string_utils import reverse_string
    print("Testing string_utils (Reversing 'Hello from Rust!'):")
    result = reverse_string("Hello from Rust!")
    print(f"Result from Rust: {result}")
except ImportError as e:
    print(f"Error: {e}")
    print("Please make sure you have compiled the Rust extension using `python setup.py build_ext --inplace`")
