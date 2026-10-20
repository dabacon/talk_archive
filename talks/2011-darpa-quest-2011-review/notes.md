# Making Error Correction Spatially Local
- **Event / Venue:** DARPA QuEST 2011 Review (2011)
- **Format:** `KEY` (`Bacon_QuEST11.key.zip`)
- **Slides:** 53

## Extracted Slide Text

1. Making Error Correction Spatially Local | Dave Bacon | University of Washington | DARPA QuEST Program Review
2. A QuEST | Do self-correcting quantum systems exist in realistic settings (spatially local few body interactions in 2 or 3 dimensions)? | dream: quantum error correction is performed by simply keeping the many-body system cold | self correct
3. Second QuEST | Is universal adiabatic quantum computing | fault-tolerant? | Energy
4. Today | A result hat has the potential to help | A result that has the potential | to impact both QuESTs
5. Quantum Error Correction | Text | Time | Complicated, time dependent many-qubit recipe for protecting quantum information
6. Stabilizer Codes | [[7,1,3]] Steane code | row = stabilizer | column = qubit
7. Concatenating Our Lives Away | x6 | Concatenation implies measurement of spatially distant, high weight, Pauli operators | I CANZ FIT N
8. Rays of Hope | Surface code QEC | 1. Measure plaquette and | vertex operators
9. t-Local and t-Neighboring | t-Local code: exists a set of stabilizer generators | whose weight ≤ t | weight of Pauli operator = # of operators ≠ I
10. Lament | Why can’t all codes be k-neighboring in two or three spatial dimensions?
11. Main Result | For every [[n,k,d]] stabilizer code, there exists a | [[N,k,r,d]] stabilizer subsystem code, N=O(n2), whose syndrome measurements can be made using t-neighboring measurements (t constant). | Every stabilizer code can be made t
12. Main Result | For every [[n,k,d]] stabilizer code, there exists a | [[N,k,r,d]] stabilizer subsystem code, N=O(n2), whose syndrome measurements can be made using t-neighboring measurements (t constant). | To grok, master these steps:
13. Stabilizer Subsystem Code | [David Poulin, arXiv:quant-ph/0508131] | n physical qubits | k encoded qubits
14. Baloney Sandwich Code | stabilizer | generators | logical
15. Baloney Sandwich Code | stabilizer | generators | X1
16. Space-Time Neighboring | Any quantum circuit can be made to be neighboring in space-time for any spatial dimension D | time | space
17. Space-Time QEC | Fault-tolerant quantum error correction can | be done using t-neighboring locality in | space-time while maintaining a threshold.
18. Measurement Based QC | [Raussendorf and Briegel, Phys. Rev. Lett. 86, 5188 (2001)] | Create Entangled State | X±Θ
19. Twisted Graph State | Rθ | “Vertex operator with angle θ” | Twisted Graph State: is common +1 eigenstate of all vertex operators (one per vertex)
20. QC to Twist Graph State | Quantum circuit made up of preparations, gates, and measurements | Graph describing vertex | operators and places where
21. Encoded MBQC Example | 1. vertex operator for every non-double-circled node | 2. starting state is +1 common eigenspace of these vertex operators | 3. input information encoded @ double-circled nodes
22. CONSTRUCTION | Input: [[n,k,d]] stabilizer code | 1. Construct fault-tolerant syndrome measuring | quantum circuit that is k-neighboring in space-time on lattice in dimension D (D>1)
23. CONSTRUCTION | 2. Convert this circuit to the scheme that would | be used to implement it in MBQC | [Related: Rausendorf, Harrington, Goyal 2006]
24. CONSTRUCTION | 3. Take operators from MBQC construction (vertex | operators and X operators for measurements) and | identify (a) stabilizer subgroup of these operators
25. Profit | For every [[n,k,d]] stabilizer code, there exists a | [[N,k,r,d]] stabilizer subsystem code, N=O(n2), whose syndrome measurements can be made using t-neighboring measurements (t constant). | $$$$
26. FAQ | Q: Why fault-tolerant syndrome measuring circuits? | - These maintain the distance of the code, actually non-fault-tolerant circuits are possible as well.
27. An Obstacle | equiv | swap
28. FAQ | Q: Why fault-tolerant syndrome measuring circuits? | - These maintain the distance of the code, actually non-fault-tolerant circuits are possible as well. | Q: But aren’t fault-tolerant circuits probabilistic?
29. Consequences | EYE FITZ | IN YUR 2D | OR 3D BOX
30. QuESTs | Self correction: | Do these Hamiltonian made of gauge qubits | on these codes self-correct?
31. Review | For every [[n,k,d]] stabilizer code, there exists a | [[N,k,r,d]] stabilizer subsystem code, N=O(n2), whose syndrome measurements can be made using t-neighboring measurements (t constant).
32. Q-Dub Group | Grads | Greg Crosswhite (Physics) | Isaac Crosson (Physics)
33. The Successful Test Dog | No cats were hurt during this talk, but they should have been
