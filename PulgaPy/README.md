# PulgaPy

PulgaPy is a modular, high-performance Python library powered by Rust. 

It is designed using a "container" architecture: each module (or container) is built as a completely independent Rust crate that compiles into its own native Python extension (`.pyd` / `.so`). This structure provides the incredible speed and safety of Rust while remaining extremely easy to use from Python.

## Architecture

PulgaPy is designed with separation of concerns in mind:
- **Modular Containers**: Each container (e.g., `container_one`, `container_two`) lives in its own directory with its own Rust source code, Python `__init__.py`, documentation, and examples.
- **In-place Compilation**: Rust code is compiled in-place, dropping the compiled Python extension directly into the container's package folder.
- **Unified Distribution**: The entire collection of containers is bundled together into a single, cohesive Python package that can be installed via `pip`.

## Installation

### From Source

To build PulgaPy from source, you will need to have [Rust](https://rustup.rs/) and Python installed.

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/PulgaPy.git
   cd PulgaPy
   ```

2. Create a virtual environment and install build dependencies:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Linux/macOS:
   # source venv/bin/activate
   
   pip install setuptools setuptools-rust wheel build
   ```

3. Build the Rust extensions in-place:
   ```bash
   python setup.py build_ext --inplace
   ```

### Using pip (Once Published)

When PulgaPy is published to PyPI, you can install it simply with:
```bash
pip install pulgapy
```

## Usage Example

Once the extensions are built, you can import the containers directly in Python:

```python
from pulgapy.container_one import sum_as_string
from pulgapy.container_two import multiply

# Calling Rust functions from container_one!
print(sum_as_string(5, 10))  # Outputs: "15"

# Calling Rust functions from container_two!
print(multiply(6, 7))        # Outputs: 42
```

## Developing New Containers

To add a new module to the library:
1. Create a new folder under `pulgapy/` (e.g., `pulgapy/container_three/`).
2. Add a `Cargo.toml`, `src/lib.rs`, and `__init__.py` following the existing pattern.
3. Add the crate path to the root `Cargo.toml` `workspace.members`.
4. Register the `RustExtension` inside `setup.py`.
5. Add the python package path to `packages` in `pyproject.toml`.
6. Compile and test!
