# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

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
from qiskit import QuantumCircuit, assemble, Aer, execute
from qiskit.visualization import plot_histogram, plot_bloch_multivector
import qiskit.tools.jupyter
from math import sqrt, pi

get_ipython().run_line_magic('qiskit_version_table', '')

# %% [markdown]
# #### create qubit

# %%
# Create qubit.
qubit = QuantumCircuit(1, 1)
qubit.h(0)    # Put first qubit in superposition
qubit.measure(0, 0)

# Show the steps of the circuit.
qubit.draw(output='mpl')

# %% [markdown]
# #### simulate the qubit

# %%
simulator = Aer.get_backend('qasm_simulator')
job = execute(qubit, simulator, shots=1000)    # Execute simulating qubit 1000 times.
result = job.result()

# Show results of the simulation.
counts = result.get_counts(qubit)
plot_histogram(counts)

# %% [markdown]
# #### visualize the measurements

# %%
sv_sim = Aer.get_backend('statevector_simulator')

# NOTE: The reason why a new simulator is used is bc this simulator
#       returns the statevector (final measurement) of the qubit
#       through get_statevector() while 'qasm_simulator' returns
#       get_counts(), getting measurements for a specific amounts of shots.

# Run simulation.
qobj = assemble(qubit)
state = sv_sim.run(qobj).result().get_statevector()

# Plot the state of the qubit (statevector).
plot_bloch_multivector(state)


