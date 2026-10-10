from qiskit_ibm_runtime import QiskitRuntimeService

# Loads the account you saved
service = QiskitRuntimeService()

print("Connected!")

print("\nAvailable quantum computers:")
for backend in service.backends():
    print(backend.name)