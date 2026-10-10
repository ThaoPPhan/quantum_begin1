from qiskit_ibm_runtime import QiskitRuntimeService

api_token = "vCXJFk5ryPH_KRNfeqI9hzufX_Z9g7xGCKxXkfSAIXhP"

try:
    print("Connecting to IBM Quantum...")

    service = QiskitRuntimeService(
        channel="ibm_cloud",
        token=api_token,
    )

    print("✅ Authentication successful!")
    print("\nAvailable backends:")

    backends = service.backends()

    for backend in backends:
        print("-", backend.name)

except Exception as e:
    print("❌ Connection failed.")
    print("Error:", e)