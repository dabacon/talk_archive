# Quantum Error Correcting Codes For Locavores
- **Event / Venue:** QEC11 (2011)
- **Format:** `KEY` (`locavore.key.zip`)
- **Slides:** 41

## Extracted Slide Text

1. Quantum Error Correcting Codes For Locavores | Dave Bacon* and Jonathan Shi | University of Washington | *= decohered to Google
2. Thanks Daniel!
3. But Why?
4. Quantum Error Correction | Text | Time | Complicated, time dependent recipe for protecting quantum information
5. Stabilizer Codes | [[7,1,3]] Steane code | row = stabilizer | column = qubit
6. Concatenating Our Lives Away | x6 | Concatenation implies measurement of spatially distant, high weight, Pauli operators | I CANZ FIT N
7. Rays of Hope | Surface code QEC | 1. Measure plaquette and | vertex operators
8. s-Local and s-Neighboring | s-Local code: exists a set of stabilizer generators | whose weight ≤s | weight of Pauli operator = # of operators ≠ I
9. Lament | Why can’t all codes be s-neighboring in two or three spatial dimensions?
10. Main Result | For every [[n,k,d]] stabilizer code, there exists a | [[N,k,r,d]] stabilizer subsystem code, N=O(n2), whose syndrome measurements can be made using s-neighboring measurements (s constant) in >1 spatial dimensions. (r = # gauge
11. Main Result | For every [[n,k,d]] stabilizer code, there exists a | [[N,k,r,d]] stabilizer subsystem code, N=O(n2), whose syndrome measurements can be made using s-neighboring measurements (s constant). | 1. stabilizer subsystem codes
12. 1. Stabilizer Subsystem Code | [David Poulin, arXiv:quant-ph/0508131] | n physical qubits | k encoded qubits
13. A Subsystem Code | stabilizer | generators | logical
14. A Subsystem Code | stabilizer | generators | X1
15. Stabilizer Moves | S1 | S2 | Sn-k-r
16. 2. Measurement Based QC | [Raussendorf and Briegel, Phys. Rev. Lett. 86, 5188 (2001)] | Create Entangled State | X±Θ
17. MBQC Wire to Code | Graph state 1D line: common +1 eigenstate of graph state vertex operators | vertex | operator
18. A MBQC Wire | Remove end stabilizer from stabilizer group and | promote it to a logical operator | S1=XZII....
19. Qubit Where? | S1=XZII.... | S2=ZXZI.... | S3=IZXZ....
20. A MBQC Wire | Make S2 a gauge qubit | X1=XZII..., Z1=ZIII... | Stabilizer generators
21. A MBQC Wire | Make S2 a gauge qubit | X1=XZII..., Z1=IXZI... | Stabilizer generators
22. A MBQC Wire | X1=XIXI...XIX, Z1=IXIX...IXZ | Stabilizer generators | Logical operators
23. A MBQC Wire | S1=XIXI...XIX | Stabilizer generators | Logical operators
24. Twisted Graph State | Rθ | “Vertex operator with angle θ” | Twisted Graph State: is common +1 eigenstate of all vertex operators (one per vertex)
25. QC to Twist Graph State | Quantum circuit made up of preparations, gates, and measurements | Graph describing vertex | operators and places where
26. Encoded MBQC Example | 1. vertex operator for every non-double-circled node | 2. starting state is +1 common eigenspace of these vertex operators | 3. input information encoded @ double-circled nodes
27. Encoded MBQC Example | 1. vertex operator for every non-double-circled node | 4. X measurements occur on all vertices labeled X | Instead of performing MBQC we can instead
28. In Action | S1 measured by measuring blue vertex operators. | S2 represents that preparation and measurement | coincide.
29. In Action | Modulo gauge and stabilizer group logical Z can be made weight 1, but logical X can only be made weight 2
30. 3. Sidebar: Space-Time Neighboring | Any quantum circuit can be made to be neighboring in space-time for any spatial dimension D | time | space
31. Space-Time QEC | Fault-tolerant quantum error correction can | be done using s-neighboring locality in | space-time while maintaining a threshold.
32. THE CONSTRUCTION | Input: [[n,k,d]] stabilizer code | 1. Construct fault-tolerant syndrome measuring | quantum circuit that is s-neighboring in space-time on lattice in dimension D (D>1)
33. CONSTRUCTION | 2. Convert this circuit to the scheme that would | be used to implement it in MBQC | [Related: Rausendorf, Harrington, Goyal 2006]
34. CONSTRUCTION | 3. Take operators from MBQC construction (vertex | operators and X operators for measurements) and | identify (a) stabilizer subgroup of these operators
35. Profit | For every [[n,k,d]] stabilizer code, there exists a | [[N,k,r,d]] stabilizer subsystem code, N=O(n2), whose syndrome measurements can be made using s-neighboring measurements (s constant). | $$$$
36. FAQ | Q: Why fault-tolerant syndrome measuring circuits? | - These maintain the distance of the code | Q: But aren’t fault-tolerant circuits probabilistic?
37. Consequences | EYE FITZ | IN YUR 2D | OR 3D BOX
38. Q-Dub Group Still Lives! | funded by | Grads | Isaac Crosson (Physics)
39. The Test Dog | No cats were hurt during this talk, but they should have been | The Successful Test Dog
