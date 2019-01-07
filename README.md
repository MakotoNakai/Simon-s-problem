# Simon's problem

## The problem that this algorithm aims to solve  
 This algorithm can be used to get the period of a randomized function. For example, suppose there is a function <img src="https://latex.codecogs.com/gif.latex?f(x)" title="f(x)" /> and a value <img src="https://latex.codecogs.com/gif.latex?r" title="r" />, which satisfies <img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;f(x&plus;r)(r\neq0)" title="f(x) = f(x+r)(r\neq0)" />.    

## Mathematical explanation  
 Let's say the value I would like to get is <img src="https://latex.codecogs.com/gif.latex?|10\rangle" title="|10\rangle" />.  
 
Here are the process to get the state above.  

1. Put <img src="https://latex.codecogs.com/gif.latex?H" title="H" /> gates to the first 2 qubits.  
<img src="https://latex.codecogs.com/gif.latex?|00\rangle|00\rangle&space;\xrightarrow{H\otimes&space;H\otimes&space;I&space;\otimes&space;I&space;}&space;\frac{|0\rangle&space;&plus;&space;|1\rangle}{\sqrt{2}}&space;\frac{|0\rangle&space;&plus;&space;|1\rangle}{\sqrt{2}}" title="|00\rangle|00\rangle \xrightarrow{H\otimes H\otimes I \otimes I } \frac{|0\rangle + |1\rangle}{\sqrt{2}} \frac{|0\rangle + |1\rangle}{\sqrt{2}}" />  

2. Create a oracle <img src="https://latex.codecogs.com/gif.latex?U_f" title="U_f" />.  
