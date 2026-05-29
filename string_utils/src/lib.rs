use pyo3::prelude::*;

/// Reverses a string efficiently.
#[pyfunction]
fn reverse_string(s: &str) -> PyResult<String> {
    Ok(s.chars().rev().collect())
}

#[pymodule]
fn string_utils(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(reverse_string, m)?)?;
    Ok(())
}
