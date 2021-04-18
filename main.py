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

# Show the steps of the circuit.
qubit.draw(output='mpl')

# %% [markdown]
# #### check measurement probabilities through sim

# %%
# NOTE: We need to create a new qubit without measurement (to visualize probabilities).
qubit_2 = QuantumCircuit(1)
qubit_2.h(0)
qobj_2 = assemble(qubit_2)

sv_sim = Aer.get_backend('statevector_simulator')
state = sv_sim.run(qobj_2).result().get_statevector()

# Show result of sim.
array_to_latex(state, pretext="\\text{Probabilitiy Vector = }")

# NOTE: We find that there is a 50/50 chance of measuring |0> and |1>.

# %% [markdown]
# #### simulate the qubit measurements

# %%
simulator = Aer.get_backend('qasm_simulator')
job = execute(qubit, simulator, shots=1000)    # Simulate qubit measurement 1000 times.
result = job.result()

# Show results of the simulation.
counts = result.get_counts(qubit)
plot_histogram(counts)

# %% [markdown]
# #### simulate the qubit measurements (on a bloch sphere)

# %%
# Run simulation.
state = sv_sim.run(qobj).result().get_statevector()

# NOTE: The reason why a new simulator is used is bc this simulator
#       returns the statevector (final measurement) of the qubit
#       through get_statevector() while 'qasm_simulator' returns
#       get_counts(), getting measurements for a specific amounts of shots.
# Plot the state of the qubit (statevector).

plot_bloch_multivector(state)

# %% [markdown]
# #### run simulation on an actual IBM quantum computer.

# %%
# NOTE: If you don't have an IBMQ account follow this video to get started: https://bit.ly/3s6tayr

IBMQ.load_account()

provider = IBMQ.get_provider('ibm-q')

# Get least busy computer.
quantum_computer = least_busy(provider.backends(simulator=False))
print('Running on ', quantum_computer)

qcomp = provider.get_backend('ibmq_16_melbourne')
job = execute(qubit, backend=quantum_computer)
job_monitor(job)

result = job.result()
plot_histogram(result.get_counts())

# NOTE: The simulated version has more accurate results
#       bc the real quantum computer has quantum noise and can result in breaking of superposition.


