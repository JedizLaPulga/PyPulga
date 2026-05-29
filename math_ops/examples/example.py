import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

try:
    from pulgapy.math_ops import fibonacci
    print("Testing math_ops (Fibonacci of 50):")
    result = fibonacci(50)
    print(f"Result from Rust: {result}")
except ImportError as e:
    print(f"Error: {e}")
    print("Please make sure you have compiled the Rust extension using `python setup.py build_ext --inplace`")
