# Turning Time Into Space for Codes and Profit*
- **Event / Venue:** Coogee2011 (2011)
- **Format:** `KEY` (`TimeIntoSpace.key.zip`)
- **Slides:** 70

## Extracted Slide Text

1. Turning Time Into Space for Codes and Profit* | Dave Bacon | University of Washington | *no warrantee, void where prohibited, not valid in WA, Australia, or anywhere else in this universe
2. Spacetime Joke
3. TQC
4. What Are We Doing? | Topological QC | Adiabatic QC | Measurement-based QC
5. Quantum Computational Matter? | A focus on systems, states, models, phases where space-time locality is an important limiting constraint | Systems, states, models, phases where quantum information or quantum computational are front and cent
6. Self-Correcting System | Physics of the device enacts quantum error correction and allows fault-tolerant quantum computing?
7. One Code, Two Models | 2D | 1D | Ising model:
8. Memory | 2D | 1D | rate ~
9. Fault-Tolerance | 2D | 1D | Resilience to “gate” of flipping spins: self-correcting
10. Self-Correcting Quantum Systems? | excitations = strings | cube operators | link operators
11. Bravyi-Terhal Bounds | For k-local D dimensional stabilizer codes (subspace | and subsystem) on an {1,..,L}D lattice, the distance of the code is bound by | cL2
12. Without Spatial Locality | Classical | distance = n | Quantum
13. Looking For? | Competition between most likely errors and cost of these errors (energy versus entropy) | Codes with local check operators.....
14. Turn Time to Space? | We know how to perform quantum error correction, locally in space-time. Can we leverage this to design | codes that are local in space? | Time
15. Stabilizer Subsystem Codes | [n,k,d] subspace code | [n,r,k,d] subsystem code | n physical qubits
16. Baloney Sandwich Example | Measure large stabilizer using only 2-qubit measurements | Gauge | Stabilizer
17. One Way QC | Quantum Circuit Model | Measurement Based Quantum Computing | One-way model
18. There’s a Code in My Wire | Vertex operators at v: | Consider stabilizer code with stabilizer generators all | vertices in a line except first one:
19. There’s a Code in My Wire | X info | localized here | logical qubit:
20. There’s a Code in My Wire | Add a gauge qubit: | does not commute with new gauge qubits | commutes with new gauge qubits
21. There’s a Code in My Wire | X info localized here | Z info localized here | modulo the gauge qubits:
22. There’s a Code in My Wire | Modulo gauge, information can be localized here | MBQC from a coding perspective | [n,1,r,1] subsystem code
23. Dave WTH Are You Doing? | Take: set of n-qubit Pauli operators | These: generate a group | This: group = r qubit Pauli group + abelian group
24. Main Idea (WAKE UP) | Circuit for measuring syndrome of a [n,k,d] stabilizer code | MBQC scheme for circuit, convert to subsystem code on N qubits | Claim: RHS code is [N,k,d] code*
25. Dictionary: | circuit to labeled graph | labeled graph describes group | include: vertex operators for
26. Circuit, Circuit, Graph | Simplest stabilizer code:
27. 12 Gauge Qubits | 2 Stabilizers | 1 Logical Qubit
28. Modulo gauge and stabilizer group logical Z can be made weight 1, but logical X can only be made weight 2 | Stabilizers can be measured by low weight measurements
29. General Method | Generalized Heisenberg pict: | Track X,Y,Z for input qubits | Track single Pauli for state preps
30. Whew | Using this method (track gauge, stabilizer, logical) | one can figure out what these operators are for | any given circuit.
31. Syndrome Circuit
32. Syndrome Circuit | Modulo gauge operators stabilizers are (a) stabilizer of code with ancillas used to measure then (b) ancillas measurement operators | Modulo gauge/stabilizer operators, logical operators are logical operators for code on 
33. An Obstacle | equiv | swap
34. An Obstacle | weight d logical | weight <d logical | Need to design circuits that do not lower weight of
35. One solution | Expander graph | Wire vertices to block | Subdivide
36. Main Result (AGAIN) | With careful use of syndrome measuring circuits, | one can turn any [n,k,d] stabilizer code into a spatially local code with [N,r,k,d] code, | where N = O(size of syndrome measuring circuit)
37. Bravyi-Terhal Bounds | Concatenated code: nr qubits, distance dr=nr log_n d | L2 | distance d = L2 log_n d
38. Adiabatic Cluster State QC | By turning on single qubit Hamiltonians while turning off parts of the cluster state Hamiltonian, we can enact a quantum circuit: | [Bacon and Flammia, Phys. Rev. A 82, 030303R (2010)]
39. Quantum Transistor | 1. Many-body system in its ground state | 2. Qubits localized on one side of the device | 3. Apply a strong 1-qubit external field to device
40. Questions | Threshold? | Hamiltonian which is sum of generators, is it self-correcting? (Related to questions about “adiabatic quantum transistor.”) | Other methods for not lowering weight of error operators? Do traditional FT methods work?
41. QW | funded by | Grads | Gregory Crosswhite (Physics)
