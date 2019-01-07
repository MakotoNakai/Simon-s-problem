# Simon's problem

## The problem that this algorithm aims to solve  
 This algorithm can be used to get the period of a randomized function. For example, suppose there is a function <img src="https://latex.codecogs.com/gif.latex?f(x)" title="f(x)" /> and a value <img src="https://latex.codecogs.com/gif.latex?r" title="r" />, which satisfies <img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;f(x&plus;r)(r\neq|00\rangle)" title="f(x) = f(x+r)(r\neq|00\rangle)" />.    

## Mathematical explanation  
 Let's say the value I would like to get is <img src="https://latex.codecogs.com/gif.latex?|10\rangle" title="|10\rangle" />.  
 
Here are the process to get the state above.  

1. Put <img src="https://latex.codecogs.com/gif.latex?H" title="H" /> gates to the first 2 qubits.  
<img src="https://latex.codecogs.com/gif.latex?|00\rangle|00\rangle&space;\xrightarrow{H\otimes&space;H\otimes&space;I&space;\otimes&space;I&space;}&space;\frac{|0\rangle&space;&plus;&space;|1\rangle}{\sqrt{2}}&space;\frac{|0\rangle&space;&plus;&space;|1\rangle}{\sqrt{2}}" title="|00\rangle|00\rangle \xrightarrow{H\otimes H\otimes I \otimes I } \frac{|0\rangle + |1\rangle}{\sqrt{2}} \frac{|0\rangle + |1\rangle}{\sqrt{2}}" />  

2. Create a oracle <img src="https://latex.codecogs.com/gif.latex?U_f" title="U_f" />.   
The function we would like to implement looks like this.
![screen shot 2019-01-07 at 8 23 18 pm](https://user-images.githubusercontent.com/45162150/50765716-2249f500-12ba-11e9-8bb3-83be46d029d6.png)  
Therefore, the outcome of the oracle would be something like this below.  
<img src="https://latex.codecogs.com/gif.latex?\xrightarrow{U_f}&space;\frac{1}{2}(|00\rangle|1\rangle&space;&plus;&space;|01\rangle|1\rangle&space;&plus;&space;|10\rangle|2\rangle&space;&plus;&space;|10\rangle|2\rangle)" title="\xrightarrow{U_f} \frac{1}{2}(|00\rangle|1\rangle + |01\rangle|1\rangle + |10\rangle|2\rangle + |10\rangle|2\rangle)" />  

This can be achived by putting <img src="https://latex.codecogs.com/gif.latex?CNOT_{02}" title="CNOT_{02}" /> gate. 

3. Put <img src="https://latex.codecogs.com/gif.latex?H" title="H" /> gates on the first 2 qubits again.  
By doing this, you can get <img src="https://latex.codecogs.com/gif.latex?|10\rangle" title="|10\rangle" /> by 50% of probability.  

<img src="https://latex.codecogs.com/gif.latex?\xrightarrow{H\otimes&space;H\otimes&space;I&space;\otimes&space;I}&space;\frac{1}{2}&space;((|00\rangle&plus;|10\rangle)|1\rangle&space;&plus;&space;(|00\rangle-|10\rangle)|2\rangle)" title="\xrightarrow{H\otimes H\otimes I \otimes I} \frac{1}{2} ((|00\rangle+|10\rangle)|1\rangle + (|00\rangle-|10\rangle)|2\rangle)" />  

## Implementation in qiskit  
If you want to perform quantum computing on your laptop, you should install qiskit(https://qiskit.org), python-based programming language for quantum computing. Here are the codes for the calculation above.  

```
# Oracle to get 10
def oracle_01(qci,x0,x1,y0,y1):
    qci.cx(x0,y0) 
    
qn = 4 # The number of total numbers of qubits
cn = 2 # The number of classical bits

upper_qn = qn //2 ## The number of qubits that you put H gates.

q = QuantumRegister(qn)
c = ClassicalRegister(cn)
qc = QuantumCircuit(q, c)

for i in range(upper_qn):
    qc.h(q[i])

oracle_01(qc,q[0],q[1],q[2],q[3])

for j in range(upper_qn):
    qc.h(q[j])

for j in range(cn):
    qc.measure(q[cn-j-1],c[j])
```  

## Result  
This is the result on QASM simulator.  
![screen shot 2019-01-07 at 8 40 25 pm](https://user-images.githubusercontent.com/45162150/50766446-95546b00-12bc-11e9-9c7e-8d3117cc20fd.png)  

This is the result on a real device(ibmq_20_tokyo)  
![screen shot 2019-01-07 at 8 47 01 pm](https://user-images.githubusercontent.com/45162150/50766660-6ee2ff80-12bd-11e9-9c2e-91098b40ffb6.png)  

As you can see, we get <img src="https://latex.codecogs.com/gif.latex?|00\rangle" title="|00\rangle" /> and <img src="https://latex.codecogs.com/gif.latex?|10\rangle" title="|10\rangle" /> 50% of probability each.  However, because <img src="https://latex.codecogs.com/gif.latex?r&space;\neq&space;|00\rangle" title="r \neq |00\rangle" />, the answer is <img src="https://latex.codecogs.com/gif.latex?|10\rangle" title="|10\rangle" />.

