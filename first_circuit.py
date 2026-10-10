import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_qsphere
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime import SamplerV2 as Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit.transpiler import generate_preset_pass_manager
from qiskit.visualization import array_to_latex
from qiskit.visualization import plot_distribution

import numpy as np
from numpy import sqrt

# 1. Visualize |0>
sv = Statevector([1, 0])
fig = plot_state_qsphere(sv)
fig.savefig("state_0.png")
plt.close(fig)


# 2. Same |0> but created using a circuit
qc1 = QuantumCircuit(1)
sv = Statevector(qc1)
fig = plot_state_qsphere(sv)
fig.savefig("state_0_circuit.png")
plt.close(fig)



