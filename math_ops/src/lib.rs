use pyo3::prelude::*;

/// Computes the nth Fibonacci number.
#[pyfunction]
fn fibonacci(n: u32) -> PyResult<u64> {
    if n <= 1 {
        return Ok(n as u64);
    }
    let mut a = 0;
    let mut b = 1;
    for _ in 2..=n {
        let temp = a + b;
        a = b;
        b = temp;
    }
    Ok(b)
}

#[pymodule]
fn math_ops(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fibonacci, m)?)?;
    Ok(())
}
