from qiskit_ibm_runtime import QiskitRuntimeService

your_api_key = "YOUR_API_KEY"  # Replace with your actual API key

QiskitRuntimeService.save_account(
    channel="ibm_cloud",
    token=your_api_key,
    overwrite=True
)

print("Account saved!")