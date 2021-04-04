## Qubit Operations
______________________
### Simple introduction to qubits with Qiskit

Steps taken:
* imports
* create qubit
    * through `QuantumCircuit()`
    * put in superposition
    * measured
* simulations
    * `qasm_simulator` to view measures through `shots` amount of iters
    * `statevector_simulator` to view single measurement of qubit
        * plot measurement to represent state on bloch sphere

`Qiskit version:`

```python
{
    'qiskit-terra': '0.16.4', 
    'qiskit-aer': '0.7.6', 
    'qiskit-ignis': '0.5.2', 
    'qiskit-ibmq-provider': '0.12.1', 
    'qiskit-aqua': '0.8.2', 
    'qiskit': '0.24.0'
}
```