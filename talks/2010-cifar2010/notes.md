# Help! There’s a Computer in My Physical System!
- **Event / Venue:** CIFAR2010 (2010)
- **Format:** `KEY` (`HelpMe.key.zip`)
- **Slides:** 54

## Extracted Slide Text

1. Help! There’s a Computer in My Physical System! | Dave Bacon | Department of Computer Science & Engineering | University of Washington
2. Oh Canada! | !!!!!!
3. Quantum Computers | 1994 | 1995 | 2002
4. Why Don’t We Have a Quantum Computer Yet?
5. A Plan!* | http://qist.lanl.gov/qcomp_map.shtml | 2002 and 2004 roadmap: | *but no man, canal, or Panama
6. 1. “scalable” system of qubits | 2. qubit initialization | 3. long decoherence times | 4. universal set of quantum gates
7. The Roadmap | Threshold theorem | ~ Given quantum computer components which fail with probability less than a threshold, one can combine these to make a robust quantum computer | Where experimental QC dedicates most of its resources
8. Why Don’t We Have a Quantum Computer Yet? | “To invent, you need a good imagination, and a pile of junk” | Thomas Edison
9. Give Me A Junkyard ;) | Where are the teams trying to build hundreds, thousands, millions, billions of “bad qubits”? | Device
10. Imagination | “To invent, you need a good imagination, and a pile of junk” - Thomas Edison | Why should we trust that our imagination can make | use of a pile of junk?
11. Models of QC | Quantum Circuit Model | Measurement Based Quantum Computing | One-way model
12. Quantum Circuit Model | Measurement Based Quantum Computing | One-way model | Teleportation model
13. Quantum Circuit Model | Foundation of all other models | Fault-tolerant | Unitary gates require precise timing and control
14. One Way QC | Quantum Circuit Model | Measurement Based Quantum Computing | One-way model
15. One Way QC | “No” unitary gates | Entanglement as “fuel” for quantum algorithm | Some compression in certain circuits
16. Universal Adiabatic QC | Quantum Circuit Model | Measurement Based Quantum Computing | One-way model
17. Universal Adiabatic QC | Adiabatic gates - fewer “timing” issues | Not known to be fault-tolerant | Current constructions use “perturbation theory gadgets” implying small energy gaps even for small circuits
18. Topological QC | Quantum Circuit Model | Measurement Based Quantum Computing | One-way model
19. Topological QC | Adiabatic gates with topological protection | Low decoherence due to energy gap | Fault-tolerant?
20. Today | Three models that combine/reinterpret many of the above models: | Adiabatic Gate Teleportation | Adiabatic Cluster State Quantum Computing
21. Adiabatic Dragging | Controversy | Detour | Energy
22. Teleportation | Controversy | Detour | Initial Code
23. Adiabatic Teleportation | Controversy | Detour | Initial Code
24. Adiabatic Teleportation | Controversy | Detour | Initial Hamiltonian
25. Adiabatic Teleportation | Controversy | Detour | Initial Hamiltonian
26. Adiabatic Gate Teleportation | Controversy | Detour | Example (Hadamard gate):
27. Let’s Build a Computer | One qubit gates | Two qubit gates | Problem: initial Hamiltonian requires 3 qubit interactions
28. Example | To get 2 qubit interactions: perturbation theory gadgets
29. Gadgets | 3a | 6a | 3b
30. Gadgets | 3a | 6a | 3b
31. Variations on a Theme | Exchange interactions:
32. Architectures | Sequence of Hamiltonians: | Sequence of single qubit gates applied: | Universal QC by cycling between only 3 Hamiltonians
33. Adiabatic Gate Teleportation | Simple adiabatic gates | Fault-tolerant (port from gate model) | Gadget construction slows down 2-qubit gates (only second order, though)
34. Anything You Can Do I Can Do Adiabatically? | Adiabatic Gate Teleportation takes a conditional measurement based protocol and performs it adiabatically | Can other such protocols be similarly converted (like the one-way model?) | “Anything 
35. Cluster State Hamiltonian | Cluster state is ground state of | Possible to use gadgets to make only 2-qubit interactions: | [S. D. Bartlett and T. Rudolph, Phys. Rev. A 74, 040302 (2006)]
36. Adiabatic Cluster State QC | By turning on single qubit Hamiltonians while turning off parts of the cluster state Hamiltonian, we can enact a quantum circuit: | [Bacon and Flammia, Phys. Rev. A 82, 030303R (2010)]
37. One Qubit | Modified cluster Hamiltonian: | 1 2 3 4 5 n-1 n | Ground state is 2-fold degenerate, can define logical operators for this qubit:
38. One Qubit | 1 2 3 4 5 n-1 n
39. One Qubit Information | 1 2 3 4 5 n-1 n | Information propagates one qubit | down the line and H is applied.
40. State Preparation | 1 2 3 4 5 n-1 n | non-degenerate | 2-fold degenerate
41. Adiabatic Gate Teleportation | Simple adiabatic gates | Preparation like topological QC, symmetry enforced initialization | Requires only final measurement
42. Can We Make a Classical Transistor? | An “identity gate” | Problem: quantum information cannot be cloned
43. Quantum Transistor | 1. Many-body system in its ground state | 2. Qubits localized on one side of the device | 3. Apply a strong 1-qubit external field to device
44. Quantum Transistor Dictionary
45. Example
46. Adiabatic? | How slowly must we turn on the external field in order for the device to successfully quantum compute?
47. Adiabatic Quantum Transistor | Gap for 1D circuit with random angle rotations...
48. Adiabatic Quantum Transistor | Gap for 2D circuit with random angle rotations...
49. Adiabatic | How slowly must we turn on the external field in order for the device to successfully quantum compute? | 1D no twists, proven polynomial in size of circuit (map to 2 transverse Ising models with boundary terms.) | 1D twists, ext
50. Fault-Tolerance? | For 1D untwisted Hamiltonian, | decouples into 2 1D Ising chains | with transverse field.
51. Adiabatic Gate Teleportation | Adiabatic gates, state prep is only in initializing ground state | Only need to apply field across portion of device (clocked architecture) | Requires only final measurement
52. Help! There’s a Computer in My Physical System! | Dave Bacon | University of Washington | Steve Flammia
53. Minimal Architectures | n qubit circuit | 4n or 5n qubits
54. QW | funded by | Grads | Gregory Crosswhite (Physics)
