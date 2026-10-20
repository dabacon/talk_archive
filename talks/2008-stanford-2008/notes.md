# Punching Holes and Quantum Fault-Tolerance
- **Event / Venue:** Stanford 2008 (2008)
- **Format:** `KEY` (`Stanford08.key.zip`)
- **Slides:** 50

## Extracted Slide Text

1. Punching Holes and Quantum Fault-Tolerance | Dave Bacon | Department of Computer Science & Engineering | Department of Physics
2. ENIAC, 1946 | 17,468 vacuum tubes | 7,200 crystal diodes | 1,500 relays
3. Alternative History | Imagine: no transistors, no integrated circuits... | Could we build a computer out of unreliable components? | J. von Neumann, “Probabilistic Logics and the Synthesis of Reliable Organism from Unreliable Components” 19
4. Von Neumann’s Model | x y z f | 0 0 0 0 | 0 0 1 0
5. 1x | 1y | 1z | 2x
6. We Don’t Need Your Stickin’ Engineering | There are distinct physical reasons why robust classical computation is possible
7. Cartoon Guide to Classical Physical Fault-Tolerance | spin | Energy | total magnetization
8. Cartoon Guide to Classical Physical Fault-Tolerance | Simple noise model | 1. Pick spin at random | “bare” noise time step
9. Memory | 2D | 1D | rate ~
10. Self-Correcting | 2D | Free energy change to flip all spins | 1D
11. Fault-Tolerance | 2D | 1D
12. Dave? Weren’t you going to be talking about quantum computing?
13. Quantum Computing | CS time | state | preparation
14. Quantum Algorithms | 18819881292060796383869723946165043 | 98071635633794173827007633564229888 | 59715234665485319060606504743045317
15. Obstacles | Decoherence: | System | environment
16. Error Correction | 000 | 111 | 001
17. Error Correction | 000 | 111 | 001
18. Quantum Error Correction | Basic idea: encoding information can help protect it | error correcting subspace | errors take codespace to orthogonal subspaces
19. Quantum Error Correction | Commuting set of four operators | Basis: | Codespace:
20. Quantum Error Correction | Every operator which acts | nontrivially on only one qubit | moves to orthogonal subspace
21. Quantum Restorative Organ | If local transition error transition amplitudes are | then output states has error amplitude | entropy
22. Fault-Tolerant Quantum Computing | Consider quantum computing where all quantum circuit components can fail: | state preparation | gates
23. The Quantum Threshold Theorem | error | rate | robust
24. The War | But....
25. Kitaev’s Idea | Alexei Kitaev | Kitaev, “Fault-tolerant quantum computation by anyons” (1997, published 2003) | “Magnetism arise from spins of individual atoms. Each spin is quite sensitive to thermal ﬂuctuations. But the spins interact wit
26. Kitaev’s Toric System | plaquette operator | vertex operator | periodic boundary conditions (torus)
27. Kitaev’s Toric System | Ground state has | Degeneracy?
28. Kitaev’s Toric Qubits | strings of Xs and Zs which loop around an odd number of times commute with but cannot be generated as products of these operators
29. Kitaev’s Toric Qubits | strings of Xs and Zs which loop around an odd number of times commute with but cannot be generated as products of these operators
30. Kitaev’s Toric System | Kitaev Hamiltonian: | ground state is a quantum error correcting code | 2L2 qubits, encodes 2 qubits, can correct L/2 qubit errors
31. Kitaev’s Toric Protection | Kitaev Hamiltonian: | Single qubit perturbation | Exponential suppression of level splitting due to external
32. Kitaev’s Toric Protection | End of chain of operators | on dual lattice only changes | at the end of the chain
33. Topological Quantum Computing | Kitaev, “Fault-tolerant quantum computation by anyons” (1997, published 2003) | Freedman, “Quantum computation and the localization of modular functors” (2001) | non-abelian Anyons can be used
34. 4D Toric Code | Excitations are now strings | cube operators | link operators
35. Dave, we don’t live in a world with four spatial dimensions! | Challenge: Does there exist a self-correcting quantum system in 3 spatial dimensions? | and in the meantime....the computer engineers...
36. Surface Code | rough | smooth | Z (X) particles can fall off
37. Puncturing Surface Codes | rough | smooth | smooth defect
38. Puncturing Surface Codes | rough | smooth | smooth defect
39. Local Architecture | Build a nearly local quantum error correcting architecture: | The Computer Engineers have hijacked topological | quantum computing!
40. Subsystem Codes | Take a subspace and put a tensor product on it | encode quantum information into | One doesn’t care what happens to information in
41. Stabilizer Codes | Stabilizer group: Abelian subgroup of Pauli group | not containing | Pauli group on n qubits:
42. Stabilizer Subsystem Codes | Normalizer of stabilizer in Pauli group: | Divide into gauge and logical qubits: | gauge
43. Doubling the Toric Code | L x L (L even) square lattice | z type | x type
44. Doubled Toric Code | Abelian invariant subgroup: | generators | Stabilizer group
45. Doubled Toric Code | Normalizer of stabilizer group: and two logical qubits | [[L2,2,L2-2,L/2]] subsystem code
46. Puncturing the DTC | z type | remove one | region of allowed removal
47. Puncturing the DTC | z type | remove > 1? | weight of smallest Z error (mod gauge) = length of defect
48. Local Architecture | Build a nearly local quantum error correcting architecture: | Benefit over toric surface code: | error correction at boundary
49. Puncturing | Fault-tolerant quantum computing: | physics or computer engineer? | Physical many-body systems with
50. QW | funded by | Graduate Students | Gregory Crosswhite (Physics)
