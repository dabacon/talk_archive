# Adiabatic Gate Teleportation
- **Event / Venue:** TQC2009 (2010)
- **Format:** `KEY` (`TQCFinal.key.zip`)
- **Slides:** 48

## Extracted Slide Text

1. Adiabatic Gate Teleportation | Dave Bacon | Department of Computer Science & Engineering | University of Washington, Seattle, WA USA
2. Seattle | Zurich
3. Huh?
4. ENIAC, 1946 | 17,468 vacuum tubes | 7,200 crystal diodes | 1,500 relays
5. Alternative History | Imagine: no transistors, no integrated circuits... | Could we build a computer out of unreliable components? | J. von Neumann, “Probabilistic Logics and the Synthesis of Reliable Organism from Unreliable Components” 19
6. Von Neumann’s Model | x y z f | 0 0 0 0 | 0 0 1 0
7. Von Neumann’s Conundrum | Observation: If all gates fail with probability p, then an output bit of any circuit most fail with at least probability p | output | Rest of Circuit
8. Von Neumann’s Solution 1 | 1x | 1y | 1z
9. Von Neumann’s Solution 2 | “Restorative organ”: | random | permutation
10. 1x | 1y | 1z | 2x
11. Controversy | Detour | Is topological quantum computing fault-tolerant? | 1x
12. Cartoon Guide to Classical Physical Fault-Tolerance | spin | Energy | total magnetization
13. Cartoon Guide to Classical Physical Fault-Tolerance | Simple noise model | 1. Pick spin at random | “bare” noise time step
14. Memory | 2D | 1D | rate ~
15. Fault-Tolerance | 2D | 1D | Resilience to “gate” of flipping spins: self-correcting
16. plaquette operator | vertex operator | periodic boundary conditions (torus) | Kitaev Toric Code Hamiltonian:
17. A Problem? | Controversy | Detour | Toric code is like 1D Ising:
18. Not a Problem? | Controversy | Detour | Factor a 1000 bit number:
19. A Problem? | Controversy | Detour | What about during computing?
20. The Quantum Threshold Theorem | error rate | robust | quantum
21. Challenge | TQC should provide it’s own “threshold theorem” | if it is truly fault-tolerant. | Why is this important?
22. Adiabatic Dragging | Controversy | Detour | Energy
23. Adiabatic Teleportation | Controversy | Detour | Initial Code
24. Adiabatic Teleportation | Controversy | Detour | Initial Code
25. Adiabatic Teleportation | Controversy | Detour | Initial Hamiltonian
26. Adiabatic Teleportation | Controversy | Detour | Initial Hamiltonian
27. Adiabatic Gate Teleportation | Controversy | Detour | Example (Hadamard gate):
28. Let’s Build a Computer | One qubit gates | Two qubit gates | Problem: initial Hamiltonian requires 3 qubit interactions
29. Example | To get 2 qubit interactions: perturbation theory gadgets
30. Gadgets | 3a | 6a | 3b
31. Gadgets | 3a | 6a | 3b
32. Variations on a Theme | Exchange interactions: | Adiabatically preparing rotated Hamiltonians: | Not all U’s allow a gap
33. “Impossibility” Theorem | Is it possible to adiabatically SWAP with only one | adiabatic interpolation? | Diagonal in same basis so cannot transfer amplitude
34. Architectures | Sequence of Hamiltonians: | Sequence of single qubit gates applied: | Universal QC by cycling between only 3 Hamiltonians
35. Architectures | n qubit circuit | 4n or 5n qubits
36. Comparison | Holonomic quantum computing, but open loop | Adiabatic universal quantum computing, but with piecewise evolution | compare:
37. Back to TQC!
38. Encoded Qubits | Smooth qubit | Rough qubit
39. Back to TQC! | Smooth qubit
40. Prepare Smooth Puncture | Turn off 2 plaquette operators | adjacent to a qubit where X is turned on.
41. Prepare Smooth Puncture
42. Prepare Smooth Puncture | commutes | with H(t) | eigenspace of
43. Prepare Smooth Puncture | Smooth qubit in +1 eigenvalue of encoded Z
44. Deform Smooth Puncture | Turn on | While turning off | + relevant vertex operators
45. Toolkit | 1. Create small smooth qubit in +1 e.v. of Z | 2. Create small rough qubit in +1 e.v. of X | 3. Enlarge, move both punctures
46. Universal Toolkit | 1. Create small smooth qubit in +1 e.v. of Z | 2. Create small rough qubit in +1 e.v. of X | 3. Enlarge, move both punctures
47. Morals | Adiabatically deforming between different Hamiltonians which have stabilizer codewords as energy eigenstates yields interesting protocols like AGT | Using AGT as a motivator you can understand how | topological quantum computing ca
48. Adiabatic Gate Teleportation | Dave Bacon | University of Washington, Seattle, WA USA | 8th Symposium on Topological Quantum Computing, Zurich 29th-31st August 2009
