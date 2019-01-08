from qiskit import IBMQ, QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.qasm import pi
from qiskit.tools.visualization import plot_histogram, circuit_drawer
import numpy as np

APItoken = "Replace me"
url = "Replace me"
IBMQ.enable_account(APItoken, url)

IBMQ.backends()

def s_oracle(qci,x0,x1,y0,y1):
	qci.x(y1)
	qci.cx(x0,y0)
	qci.cx(x1,y0)
	


qn = 4
cn = 2
upper_qn = qn //2
q = QuantumRegister(qn)
c = ClassicalRegister(cn)
qc = QuantumCircuit(q, c)

for i in range(upper_qn):
	qc.h(q[i])
	
s_oracle(qc,q[0],q[1],q[2],q[3])

for j in range(upper_qn):
	qc.h(q[j])

for j in range(cn):
	qc.measure(q[cn-j-1],c[j])
# Put a real device first and a simulator after that.
# I put ibmq_20_tokyo because I'm allowed to use it.
backends = ['ibmq_20_tokyo', 'qasm_simulator']
#Use this for the actual machine
backend_sim = IBMQ.get_backend(backends[0])
#Use this for the simulation
#backend_sim = Aer.get_backend(backends[1])#{'00': 2137, '11': 1959}
result = execute(qc, backend_sim, shots=4096).result()
#circuit_drawer(qc).show()
plot_histogram(result.get_counts(qc))
print(result.get_counts(qc))
