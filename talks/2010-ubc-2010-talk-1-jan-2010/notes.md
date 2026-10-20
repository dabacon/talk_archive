# Adiabatic Cluster State Quantum Computing
- **Event / Venue:** UBC 2010 - Talk 1 (Jan 2010) (2010)
- **Format:** `KEY` (`ubc2.key.zip`)
- **Slides:** 45

## Extracted Slide Text

1. Adiabatic Cluster State Quantum Computing | - or - | Anything you can do, I can do adiabatically | I can do anything sssllllooooowwwweeeerrrrr than you
2. Quantum Computers | 1994 | 1995 | 2002
3. Why Don’t We Have a Quantum Computer Yet?
4. A Plan! | http://qist.lanl.gov/qcomp_map.shtml | 2002 and 2004 roadmap:
5. 1. “scalable” system of qubits | 2. qubit initialization | 3. long decoherence times | 4. universal set of quantum gates
6. The Roadmap | Threshold theorem | ~ Given quantum computer components which fail with probability less than a threshold, one can combine these to make a robust quantum computer | Where experimental QC dedicates most of its resources
7. Why Don’t We Have a Quantum Computer Yet? | “To invent, you need a good imagination, and a pile of junk” | Thomas Edison
8. Give Me A Junkyard ;) | Where are the teams trying to build hundreds, thousands, millions, billions of “bad qubits”? | Device
9. Imagination | “To invent, you need a good imagination, and a pile of junk” - Thomas Edison | Why should we trust that our imagination can make | use of a pile of junk?
10. Models of QC | Quantum Circuit Model | Measurement Based Quantum Computing | One-way model
11. Quantum Circuit Model | Measurement Based Quantum Computing | One-way model | Teleportation model
12. Quantum Circuit Model | Foundation of all other models | Fault-tolerant | Unitary gates require precise timing and control
13. One Way QC | Quantum Circuit Model | Measurement Based Quantum Computing | One-way model
14. One Way QC | No unitary gates | Entanglement as “fuel” for quantum algorithm | Some compression in certain circuits
15. Universal Adiabatic QC | Quantum Circuit Model | Measurement Based Quantum Computing | One-way model
16. Universal Adiabatic QC | Adiabatic gates - no timing issues | Not known to be fault-tolerant | Current constructions use “perturbation theory gadgets” implying small energy gaps even for small circuits
17. Topological QC | Quantum Circuit Model | Measurement Based Quantum Computing | One-way model
18. Topological QC | Adiabatic gates with topological protection | Low decoherence due to energy gap | Fault-tolerant?
19. Today | Two models that combine/reinterpret many of the above models: | Adiabatic Gate Teleportation | Adiabatic Cluster State Quantum Computing
20. Adiabatic Dragging | Controversy | Detour | Energy
21. Teleportation | Controversy | Detour | Initial Code
22. Adiabatic Teleportation | Controversy | Detour | Initial Code
23. Adiabatic Teleportation | Controversy | Detour | Initial Hamiltonian
24. Adiabatic Teleportation | Controversy | Detour | Initial Hamiltonian
25. Adiabatic Gate Teleportation | Controversy | Detour | Example (Hadamard gate):
26. Let’s Build a Computer | One qubit gates | Two qubit gates | Problem: initial Hamiltonian requires 3 qubit interactions
27. Example | To get 2 qubit interactions: perturbation theory gadgets
28. Gadgets | 3a | 6a | 3b
29. Gadgets | 3a | 6a | 3b
30. Variations on a Theme | Exchange interactions fix this: | Adiabatically preparing rotated Hamiltonians: | Not all U’s allow a gap
31. Architectures | Sequence of Hamiltonians: | Sequence of single qubit gates applied: | Universal QC by cycling between only 3 Hamiltonians
32. Architectures | n qubit circuit | 4n or 5n qubits
33. Adiabatic Gate Teleportation | Simple adiabatic gates | Fault-tolerant (port proof from gate model) | Gadget construction slows down 2-qubit gates
34. Anything You Can Do I Can Do Adiabatically? | Adiabatic Gate Teleportation takes a conditional measurement based protocol and performs it adiabatically | Can other such protocols be similarly converted (like the one-way model?)
35. Cluster State Hamiltonian | Cluster state is ground state of | Possible to use gadgets to make only 2-qubit interactions: | [S. D. Bartlett and T. Rudolph, Phys. Rev. A 74, 040302 (2006)]
36. Adiabatic Cluster State QC | By turning on single qubit Hamiltonians while turning off parts of the cluster state Hamiltonian, we can enact a quantum circuit:
37. One Qubit | Modified cluster Hamiltonian: | 1 2 3 4 5 n-1 n | Ground state is 2-fold degenerate, can define logical operators for this qubit:
38. One Qubit | Modified cluster Hamiltonian: | 1 2 3 4 5 n-1 n | Adiabatically turn on field along X direction:
39. One Qubit | Modified cluster Hamiltonian: | 1 2 3 4 5 n-1 n | Adiabatically turn on field along X direction:
40. One Qubit Rotations | Modified cluster Hamiltonian: | 1 2 3 4 5 n-1 n | Adiabatically turn on field along rotated direction:
41. Two Qubit Gate | 1 2 3
42. State Preparation | Cluster Hamiltonian: | 1 2 3 4 5 n-1 n | Turn on two magnetic fields
43. Adiabatic Gate Teleportation | Simple adiabatic gates | Requires only final measurement (like topological quantum computing) | Fault-tolerant to model where cluster state is thermalized
44. Adiabatic Gate Teleportation | Simple adiabatic gates | Requires only final measurement (like topological quantum computing) | Fault-tolerant to model where cluster state is thermalized
45. QW | funded by | Graduate Students | Gregory Crosswhite (Physics)
