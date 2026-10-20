# Crazy Quantum Concatenated Code Hamiltonians*
- **Event / Venue:** IBM 2008 (2008)
- **Format:** `KEY` (`ibm.key.zip`)
- **Slides:** 62

## Extracted Slide Text

1. Crazy Quantum Concatenated Code Hamiltonians* | Dave Bacon | University of Washington | * This proposal, like all proposals for quantum computation, relies on speculative technology, does not in its current form take into account all possib
2. The Quantum Computing Enemy | Decoherence | Imprecise control | The Solution?
3. Fight Physics with Physics
4. The Computing Phase
5. Fundamental Question | What makes a physical system a good storer and manipulator of (quantum/classical) information?
6. Heating and Cooling | system | bath | For perturbative interactions with bath in equilibrium
7. Model Hard Drive | spin flip:
8. Self-Correction
9. Storage Comparisons | Ferromagnetic Ising models: | one dimensional | two (and >) dimensional
10. Dynamic Ising Models | Interaction with environment causes spin flips | Update rule: | If flipping spin would decrease energy, flip spin
11. Toom’s Rule | two dimensional noisy cellular automata | Update rule: | b=majority(n,e,b)
12. Storage | 1D Ising | 2D Ising | Long time behavior (not infinite time, but effectively)
13. 2 nd attempt: | 1D Ising | Relaxation to thermal | Imperfect preparation
14. Manipulation | Flipping spins is imperfect | 1D Ising | 2D Ising
15. Toom’s Rule Versus 2D Ising | 2D Ising | Applied magnetic field (corresponds to a bias in noise) | Toom’s Rule
16. Quantum Hard Drives? | quantum error correcting | code states
17. Kitaev’s Toric Code Model | qubits on links | plaquette operators: | vertex operators:
18. Excitations | excitations particles come in pairs (particle/antiparticle) | at end of “error” chains | two types of particles, X-type (live on vertices of dual lattice)
19. Into the Fourth Dimesnion | qubits on plaquettes | link stabilizers | also cube stabilizers
20. Excitations are Strings | Energy cost proportional to perimeter | errors | self correcting
21. Perfection Through Concatenation | failure | probability | cp 2
22. Can We Concatenate For a Self-Correcting Quantum Memory?
23. Stabilizer Codes in an Unstable Amount of Time | Stabilizer: group of commuting Pauli operators | (not containing -I) | Ex: five qubit code
24. Stabilizer Hamiltonians | [[n,k,d]] code | ground state is k fold degenerate | smallest weight Pauli error which acts non-trivially on ground state subspace is weight k
25. Concatenated Code Hamiltonians | r levels of concatenation: | nr qubits | Hamiltonian is sum of nr-1 terms
26. Self-Correcting Barrier | Correction distance: number of errors corrected via the concatenated code correction scheme | Energy change bounded by correction distance.
27. Perturb It? | Want to show that local perturbations do not destroy information encoded into ground state. | But can we rigorously apply degenerate perturbation | theory here?
28. Leverage Concatenation
29. Deg. Pert. Theory | energy | If then | perturbed
30. Deg. Pert. Theory | If we truncate we can bound the error:
31. Ground State Heff | Single qubit perturbations on [[n,1,3]] code: | First order: | Second order:
32. Ground State Heff | Third order: | nontrivial term on g.s. | where
33. But...
34. Higher States | First order: | does not act on ground subspace | Second order:
35. Together | focus on | which act nontrivially on ground state
36. Threshold | When is this lower strength than perturbation? | Combinatorial calculation for [[5,1,3]] code:
37. Review | r levels of concatenation:
38. Why? | This seems to imply that concatenation produces a splitting at 2r. Why isn’t this dr? | Probably technical: work with respect to unperturbed interaction | What about the new effective stabilizers?
39. The Not So Hidden Problems | n local interactions
40. Solutions? | Fault-tolerant simulation of stabilizer Hamiltonians | Can we gadget our way out of this mess?
41. Simulate Hamiltonians | Lloyd, Rahn, Ahn, arXiv:quant-ph/9912040 | Stroboscopic evolution to generate effective evolution | Problem:
42. Fault-Tolerant Stabilizer Hamiltonian Simulation | Similar conditions for fault-tolerant quantum error correction | Q: error model for this setup???
43. Gadgets | three qubit | interaction | Can we amplify?
44. Concatenated Gadgets? | amplification simply replaces n qubit interactions with | an exponential number of ancillas | Is it possible to get around this via concatenation?
45. A Final Observation | 9 qubit subsystem code is well suited geometrically | for concatenation | stabilizers
46. Crazy Quantum Concatenated Code Hamiltonians* | Dave Bacon | University of Washington | * This proposal, like all proposals for quantum computation, relies on speculative technology, does not in its current form take into account all possib
