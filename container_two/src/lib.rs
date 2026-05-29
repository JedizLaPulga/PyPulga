use pyo3::prelude::*;

/// Multiplies two numbers.
#[pyfunction]
fn multiply(a: i32, b: i32) -> PyResult<i32> {
    Ok(a * b)
}

/// A Python module implemented in Rust.
#[pymodule]
fn container_two(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(multiply, m)?)?;
    Ok(())
}
