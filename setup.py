from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    rust_extensions=[
        RustExtension(
            "pulgapy.math_ops.math_ops", 
            path="pulgapy/math_ops/Cargo.toml", 
            binding=Binding.PyO3
        ),
        RustExtension(
            "pulgapy.string_utils.string_utils", 
            path="pulgapy/string_utils/Cargo.toml", 
            binding=Binding.PyO3
        ),
    ],
    zip_safe=False,
)
