# The War to Build a Quantum Computer
- **Event / Venue:** UW Physics 2008 (2008)
- **Format:** `KEY` (`UW Physics 5.key.zip`)
- **Slides:** 91

## Extracted Slide Text

1. The War to Build a Quantum Computer | Dave Bacon | University of Washington
2. ENIAC, 1946 | 17,468 vacuum tubes | 7,200 crystal diodes | 1,500 relays
3. Alternative History | Imagine: no transistors, no integrated circuits... | Could we build a computer out of unreliable components? | J. von Neumann, “Probabilistic Logics and the Synthesis of Reliable Organism from Unreliable Components” 19
4. Von Neumann’s Model | x y z f | 0 0 0 0 | 0 0 1 0
5. Von Neumann’s Conundrum | Observation: If all gates fail with probability p, then an output bit of any circuit most fail with at least probability p | output | Rest of Circuit
6. Von Neumann’s Solution 1 | 1x | 1y | 1z
7. Von Neumann’s Solution 2 | “Restorative organ”: | random | permutation
8. 1x | 1y | 1z | 2x
9. Dave? Did someone forget to tell you this is a physics colloquium?
10. We Don’t Need Your Stickin’ Engineering
11. Cartoon Guide to Classical Physical Fault-Tolerance | spin | Energy | total magnetization
12. Cartoon Guide to Classical Physical Fault-Tolerance | Simple noise model | 1. Pick spin at random | “bare” noise time step
13. Memory | 2D | 1D | rate ~
14. Self-Correcting | 2D | Free energy change to flip all spins | 1D
15. Fault-Tolerance | 2D | 1D
16. Dave? Weren’t you going to be talking about quantum computing?
17. Quantum Computing | CS time | state | preparation
18. Quantum Algorithms | 18819881292060796383869723946165043 | 98071635633794173827007633564229888 | 59715234665485319060606504743045317
19. Quantum Algorithms | 01 01 00 11 00 01 10 11 | Na | N1/2
20. Quantum Algorithms | 0101101110011011 | Farhi, Goldstone, and Gutman, “A Quantum Algorithm for the Hamiltonian NAND Tree” 2007 | right going initial wave packet
21. Obstacles | Decoherence: | System | environment
22. Error Correction | 000 | 111 | 001
23. Error Correction | 000 | 111 | 001
24. Quantum Error Correction | Basic idea: encoding information can help protect it | error correcting subspace | errors take codespace to orthogonal subspaces
25. Quantum Error Correction | Commuting set of four operators | Basis: | Codespace:
26. Quantum Error Correction | Every operator which acts | nontrivially on only one qubit | moves to orthogonal subspace
27. Quantum Restorative Organ | If local transition error transition amplitudes are | then output states has error amplitude | entropy
28. Fault-Tolerant Quantum Computing | Consider quantum computing where all quantum circuit components can fail: | state preparation | gates
29. The Quantum Threshold Theorem | error | rate | robust
30. The War | But....
31. Kitaev’s Idea | Alexei Kitaev | Kitaev, “Fault-tolerant quantum computation by anyons” (1997, published 2003) | “Magnetism arise from spins of individual atoms. Each spin is quite sensitive to thermal ﬂuctuations. But the spins interact wit
32. Kitaev’s Toric System | plaquette operator | vertex operator | periodic boundary conditions (torus)
33. Kitaev’s Toric System | Ground state has | Degeneracy?
34. Kitaev’s Toric System | plaquette operator | algebra: products of loops on lattice which wrap around torus directions an even number of times | Not in algebra
35. Kitaev’s Toric System | algebra: products of loops on dual lattice which wrap around torus directions an even number of times | Not in algebra | vertex operator
36. Kitaev’s Toric System | operators which loop around an odd number of times | commute with but not all among each other | ground state is 4-fold degenerate
37. Kitaev’s Toric System | Kitaev Hamiltonian: | ground state is a quantum error correcting code | L2 qubits, encodes 4 qubits, can correct L/2 qubit errors
38. Kitaev’s Toric Protection | Kitaev Hamiltonian: | Single qubit perturbation | Exponential suppression of level splitting due to external
39. Kitaev’s Toric Protection | End of chain of operators | on dual lattice only changes | at the end of the chain
40. Anyons Anyone? | Two types of particles X and Z | braiding X around Z type | particles multiplies wave function by -1
41. Topological Quantum Computing | Kitaev, “Fault-tolerant quantum computation by anyons” (1997, published 2003) | Freedman, “Quantum computation and the localization of modular functors” (2001) | non-abelian Anyons can be used
42. 4D Toric Code | Excitations are now strings | cube operators | link operators
43. Dave, we don’t live in a world with four spatial dimensions! | Challenge: Does there exist a self-correcting quantum system in 3 spatial dimensions? | and in the meantime....the computer engineers...
44. Surface Code | rough | smooth | Z (X) particles can fall off
45. Puncturing Surface Codes | rough | smooth | smooth defect
46. Local Architecture | Build a nearly local quantum error correcting architecture: | The Computer Engineers have hijacked topological | quantum computing!
47. Quantum Compass Model | Dorier, Becca, Mila “The Quantum Compass Model on a Square Lattice” (2005)
48. Quantum Compass Model | Operators which commute with Hamiltonian: | imply ground state is two-fold degenerate | Can it be used to protect quantum information?
49. Quantum Compass Model | Dorier, Becca, Mila “The Quantum Compass Model on a Square Lattice” (2005) | = ratio of | XX and ZZ interactions
50. Subsystem Codes | Take a subspace and put a tensor product on it | encode quantum information into | One doesn’t care what happens to information in
51. Compass Model Subsystem Code | Bacon, “Operator Quantum Error-correcting Subsystems for Self-correcting Quantum Memories” (2006) | group generated by | abelian invariant subgroup:
52. Fault-Tolerance in Subsystem Code | Normally to fault-tolerantly measure syndrome | have to use lots of ancilla qubits | ancilla
53. Fault-Tolerance in Subsystem Code | gauge degrees of freedom allow fault-tolerant syndrome | measurement two qubits at a time: | Best proven threshold for fault-tolerant quantum computing:
54. War | Fault-tolerant quantum computing | justifies the model of quantum computing | But do we really need it, or can physics based methods be used?
55. QW | funded by | Graduate Students | Gregory Crosswhite (Physics)
