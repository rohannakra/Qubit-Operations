# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## Objective: Put qubit in superposition and measure it.
# %% [markdown]
# ##### important note:
# 
# |0⟩ =
# [
# 1
# 0
# ]
# 
# |1⟩ =
# [
# 0
# 1
# ]
# %% [markdown]
# #### imports

# %%
from qiskit import QuantumCircuit, assemble, Aer, execute, IBMQ, __qiskit_version__
from qiskit.providers.ibmq import least_busy
from qiskit.tools import job_monitor
from qiskit_textbook.tools import array_to_latex
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from math import sqrt, pi

print(__qiskit_version__)

# %% [markdown]
# #### create qubit

# %%
# Create qubit.
qubit = QuantumCircuit(1, 1)
qubit.h(0)    # Put first qubit in superposition
qubit.measure(0, 0)

# Create object.
qobj = assemble(qubit)

# %% [markdown]
# #### wave function  of qubit:
# <img src='wave_function.gif'>
# %% [markdown]
# #### create helper function to run simulations

# %%
class Simulate:
    def __init__(self, circuit, simulator):
        self.circuit = circuit
        self.simulator = simulator

    def execute_circuit_sv(self):
        sv_sim = Aer.get_backend('statevector_simulator')

        result = execute(self.circuit, sv_sim).result()

        state = result.get_statevector(self.circuit)
        circuit_diagram = self.circuit.draw('mpl')
        bloch_sphere = plot_bloch_multivector(state)

        return circuit_diagram, state, bloch_sphere
    
    def execute_circuit_qasm(self):
        qasm_sim = Aer.get_backend('qasm_simulator')

        result = execute(qubit, qasm_sim, shots=100).result()
        counts = result.get_counts(self.circuit)
        circuit_diagram = self.circuit.draw('mpl')
        histogram = plot_histogram(counts)

        return circuit_diagram, counts, histogram
    
    def execute_circuit_qcomp(self):
        IBMQ.load_account()

        provider = IBMQ.get_provider('ibm-q')

        # Get least busy computer.
        qcomp = least_busy(provider.backends(simulator=False))
        print('Running on', qcomp)

        job = execute(qubit, backend=qcomp)
        job_monitor(job)

        result = job.result()
        return plot_histogram(result.get_counts())
    
    def __call__(self):
        if self.simulator == 'statevector':
            return self.execute_circuit_sv()
        elif self.simulator == 'qasm':
            return self.execute_circuit_qasm()
        elif self.simulator == 'qcomp' or self.simulator == 'quantum computer':
            return self.execute_circuit_qcomp()
        else:
            raise NameError(f"Simulator '{simulator}' is not an option.")
        

circuit_diagram, state, bloch_sphere = Simulate(qubit, 'statevector')()
circuit_diagram, counts, histogram = Simulate(qubit, 'qasm')()


# %%
circuit_diagram


# %%
histogram


# %%
bloch_sphere


# %%
qcomp_histogram = Simulate(qubit, 'qcomp')()
qcomp_histogram


