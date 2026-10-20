# Adiabatic Gate Teleportation
- **Event / Venue:** Perimeter09 (2009)
- **Format:** `KEY` (`Perimeter09.key.zip`)
- **Slides:** 55

## Extracted Slide Text

1. Adiabatic Gate Teleportation | & Its Applications | Dave Bacon | Department of Computer Science & Engineering
2. Oops, I forgot to strap myself in! | Look over there! | A jackalope! | I’ll bet most states are too entangled to be used as computational resources
3. ENIAC, 1946 | 17,468 vacuum tubes | 7,200 crystal diodes | 1,500 relays
4. Alternative History | Imagine: no transistors, no integrated circuits... | Could we build a computer out of unreliable components? | J. von Neumann, “Probabilistic Logics and the Synthesis of Reliable Organism from Unreliable Components” 19
5. 1x | 1y | 1z | 2x
6. Engineering? We Don’t Need Your Stickin’ Engineering | There are distinct physical reasons why robust classical computation is possible
7. Kitaev’s Idea | Alexei Kitaev | Kitaev, “Fault-tolerant quantum computation by anyons” (1997, published 2003) | “Magnetism arise from spins of individual atoms. Each spin is quite sensitive to thermal fluctuations. But the spins interact wi
8. Topological Quantum Computing | Kitaev, “Fault-tolerant quantum computation by anyons” (1997, published 2003) | Freedman, “Quantum computation and the localization of modular functors” (2001) | non-abelian Anyons used to build a universal q
9. Kitaev’s Toric System | plaquette operator | vertex operator | periodic boundary conditions (torus)
10. Controversy | Detour | Is topological quantum computing fault-tolerant? | 1x
11. Cartoon Guide to Classical Physical Fault-Tolerance | spin | Energy | total magnetization
12. Cartoon Guide to Classical Physical Fault-Tolerance | Simple noise model | 1. Pick spin at random | “bare” noise time step
13. Memory | 2D | 1D | rate ~
14. Fault-Tolerance | 2D | 1D | Resilience to “gate” of flipping spins: self-correcting
15. plaquette operator | vertex operator | periodic boundary conditions (torus) | Kitaev Toric Code Hamiltonian:
16. A Problem? | Controversy | Detour | Toric code is like 1D Ising:
17. Not a Problem? | Controversy | Detour | Factor a 1000 bit number:
18. A Problem? | Controversy | Detour | What about during computing?
19. TQC: Gates | “We now introduce into the system’s Hamiltonian a scalar potential composed of many local “traps,” each sufficient to capture exactly one quasiparticle. These traps may be created by impurities, by small gates, or by the potent
20. TQC Problems? | How does one guarantee that one can trap one and | only one anyon? | Every operation the previous paragraph needs to be demonstrated that it can be done with EXCEPTIONALLY small error if this is to be called physical fault-t
21. Adiabatic Dragging | Controversy | Detour | Energy
22. Adiabatic Teleportation | Controversy | Detour | Initial Code
23. Adiabatic Teleportation | Controversy | Detour | Initial Code
24. Adiabatic Teleportation | Controversy | Detour | Initial Hamiltonian
25. Adiabatic Teleportation | Controversy | Detour | Initial Hamiltonian
26. Adiabatic Gate Teleportation | Controversy | Detour | Example (Hadamard gate):
27. Let’s Build a Computer | One qubit gates | Two qubit gates | Problem: initial Hamiltonian requires 3 qubit interactions
28. Example | To get 2 qubit interactions: perturbation theory gadgets
29. Gadgets | 3a | 6a | 3b
30. Gadgets | 3a | 6a | 3b
31. Variations on a Theme | Exchange interactions: | Adiabatically preparing rotated Hamiltonians: | Not all U’s allow a gap
32. “Impossibility” Theorem | Is it possible to adiabatically SWAP with only one | adiabatic interpolation? | Diagonal in same basis so cannot transfer amplitude
33. Architectures | Sequence of Hamiltonians: | Sequence of single qubit gates applied: | Universal QC by cycling between only 3 Hamiltonians
34. Architectures | n qubit circuit | 4n or 5n qubits
35. Comparison | Holonomic quantum computing, but open loop | Adiabatic universal quantum computing, but with piecewise evolution | compare:
36. Back to TQC!
37. Encoded Qubits | Smooth qubit | Rough qubit
38. Back to TQC! | Smooth qubit
39. Prepare Smooth Puncture | Turn off 2 plaquette operators | adjacent to a qubit where X is turned on.
40. Prepare Smooth Puncture
41. Prepare Smooth Puncture | commutes | with H(t) | eigenspace of
42. Prepare Smooth Puncture | Smooth qubit in +1 eigenvalue of encoded Z
43. Deform Smooth Puncture | Turn on | While turning off | + relevant vertex operators
44. Toolkit | 1. Create small smooth qubit in +1 e.v. of Z | 2. Create small rough qubit in +1 e.v. of X | 3. Enlarge, move both punctures
45. Universal Toolkit | 1. Create small smooth qubit in +1 e.v. of Z | 2. Create small rough qubit in +1 e.v. of X | 3. Enlarge, move both punctures
46. Measurement | Simple, right? | But how to perform why | Hamiltonian still on?
47. Universal Toolkit | 1. Create small smooth qubit in +1 e.v. of Z | 2. Create small rough qubit in +1 e.v. of X | 3. Enlarge, move both punctures
48. Summary | Adiabatically deforming between different Hamiltonians which have stabilizer codewords as energy eigenstates yields interesting protocols like AGT | Using AGT as a motivator you can understand how | topological quantum computing c
49. Adiabatic Gate Teleportation | Dave Bacon | University of Washington, Seattle, WA USA | 8th Symposium on Topological Quantum Computing, Zurich 29th-31st August 2009
50. Open Questions | Like measurement based methods, but without having to | perform correction afterwards: | Can we (1) do cluster state computation in this manner?
51. Self-Correcting | 2D | Calculate: free energy change to flip all spins | 1D
52. Von Neumann’s Model | x y z f | 0 0 0 0 | 0 0 1 0
53. Von Neumann’s Conundrum | Observation: If all gates fail with probability p, then an output bit of any circuit most fail with at least probability p | output | Rest of Circuit
54. Von Neumann’s Solution 1 | 1x | 1y | 1z
55. Von Neumann’s Solution 2 | “Restorative organ”: | random | permutation
