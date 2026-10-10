from qiskit_ibm_runtime import QiskitRuntimeService

your_api_key = "vCXJFk5ryPH_KRNfeqI9hzufX_Z9g7xGCKxXkfSAIXhP"

QiskitRuntimeService.save_account(
    channel="ibm_cloud",
    token=your_api_key,
    overwrite=True
)

print("Account saved!")