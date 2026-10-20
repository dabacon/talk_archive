# Making Error Correction Spatially Local
- **Event / Venue:** SQUINT2011 (2011)
- **Format:** `KEY` (`localizeme.key.zip`)
- **Slides:** 28

## Extracted Slide Text

1. Making Error Correction Spatially Local | Dave Bacon and Jonathan Shi | University of Washington
2. Error Correction | flash memory | magnetic hard drive | transistor
3. Quantum Error Correction | Text | Time | Complicated, time dependent recipe for protecting quantum information
4. Stabilizer Codes | [[7,1,3]] Steane code | row = stabilizer | column = qubit
5. Concatenating Our Lives Away | x6 | Concatenation implies measurement of spatially distant, high weight, Pauli operators | I CANZ FIT N
6. Rays of Hope | Surface code QEC | 1. Measure plaquette and | vertex operators
7. k-Local and k-Neighboring | k-Local code: exists a set of stabilizer generators | whose weight ≤ k | weight of Pauli operator = # of operators ≠ I
8. Lament | Why can’t all codes be k-neighboring in two or three spatial dimensions?
9. Main Result | For every [[n,k,d]] stabilizer code, there exists a | [[N,k,r,d]] stabilizer subsystem code, N=O(n2), whose syndrome measurements can be made using k-neighboring measurements (k constant). | Every stabilizer code can be made t
10. Main Result | For every [[n,k,d]] stabilizer code, there exists a | [[N,k,r,d]] stabilizer subsystem code, N=O(n2), whose syndrome measurements can be made using k-neighboring measurements (k constant). | 1. stabilizer subsystem codes
11. Stabilizer Subsystem Code | [David Poulin, arXiv:quant-ph/0508131] | n physical qubits | k encoded qubits
12. Baloney Sandwich Code | stabilizer | generators | logical
13. Baloney Sandwich Code | stabilizer | generators | X1
14. Space-Time Neighboring | Any quantum circuit can be made to be neighboring in space-time for any spatial dimension D | time | space
15. Space-Time QEC | Fault-tolerant quantum error correction can | be done using k-neighboring locality in | space-time while maintaining a threshold.
16. Measurement Based QC | [Raussendorf and Briegel, Phys. Rev. Lett. 86, 5188 (2001)] | Create Entangled State | X±Θ
17. Twisted Graph State | Rθ | “Vertex operator with angle θ” | Twisted Graph State: is common +1 eigenstate of all vertex operators (one per vertex)
18. QC to Twist Graph State | Quantum circuit made up of preparations, gates, and measurements | Graph describing vertex | operators and places where
19. Encoded MBQC Example | 1. vertex operator for every non-double-circled node | 2. starting state is +1 common eigenspace of these vertex operators | 3. input information encoded @ double-circled nodes
20. CONSTRUCTION | Input: [[n,k,d]] stabilizer code | 1. Construct fault-tolerant syndrome measuring | quantum circuit that is k-neighboring in space-time on lattice in dimension D (D>1)
21. CONSTRUCTION | 2. Convert this circuit to the scheme that would | be used to implement it in MBQC | [Related: Rausendorf, Harrington, Goyal 2006]
22. CONSTRUCTION | 3. Take operators from MBQC construction (vertex | operators and X operators for measurements) and | identify (a) stabilizer subgroup of these operators
23. Profit | For every [[n,k,d]] stabilizer code, there exists a | [[N,k,r,d]] stabilizer subsystem code, N=O(n2), whose syndrome measurements can be made using k-neighboring measurements (k constant). | $$$$
24. FAQ | Q: Why fault-tolerant syndrome measuring circuits? | - These maintain the distance of the code | Q: But aren’t fault-tolerant circuits probabilistic?
25. Consequences | EYE FITZ | IN YUR 2D | OR 3D BOX
26. Q-Dub Group | funded by | Grads | Greg Crosswhite (Physics)
27. The Test Dog | No cats were hurt during this talk, but they should have been | The Successful Test Dog
