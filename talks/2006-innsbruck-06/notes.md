# This Space Left Intentionally Blank
- **Event / Venue:** Innsbruck 06 (2006)
- **Format:** `PPT` (`Innsbruck06.ppt`)
- **Slides:** 56

## Extracted Slide Text

1. This Space Left Intentionally Blank
2. Quantum Error Correcting Subsystem Codes — and Fault-Tolerant Quantum Computing — Dave Bacon — Department of Computer Science & Engineering
3. Paradise?
4. Environment — Problem Child — decoherence: — coherent superposition
5. My Mortal Enemy
6. Problem Solution — QC — “decoherence” — “imprecision”
7. Sketch: How It Works — To make robust elements, information is encoded into a quantum — error correcting codes of significant size and fault-tolerant methods — are used for gates, preparation, measurement, and correction
8. In Practice? — 13000 ions, 1000 laser beams, 160000 electrodes in ion trap — The device complexity simply to engineer robust qubits is severe — “A quantum computer will spend most of its time doing error correction.”
9. Quantum Error Correction — encoded — quantum — information
10. The Quantum Hard Drive? — Kitaev — Do there exist (or can we engineer) quantum systems whose — physics guarantees fault-tolerant quantum computation?
11. Kitaev’s Model — qubits on links — plaque operators: — vertex operators:
12. Kitaev’s Model, Continued — plaque operators: — vertex operators: — Hamiltonian
13. Topology of Operators — products of vertex operators — are closed loops of Z’s which — are homologically trivial
14. Degeneracy — Hamiltonian — plaque operators: — vertex operators:
15. Kitaev’s Model — plaque operators: — vertex operators: — anti-commutes with
16. Excitations — excitations particles come in pairs (particle/antiparticle) — at end of “error” chains — two types of particles, X-type (live on vertices of dual lattice)
17. A Qubit — Moving an X or Z type particle on a homologically nontrivial — path and annihilating with it’s partner preserves the ground — states
18. Anyons Anyone? — Phase:
19. Topological Protection — Encode two qubits — into the ground state — gap
20. Topological Quantum Computing — Encode two qubits — into the ground state — gap
21. Topological Error Correction — Different mode of using Kitaev’s Model, as a component in — a fault-tolerant quantum computer, encode into ground state — 1. Errors occur
22. Fault-Tolerant? — Encode two qubits — into the ground state — gap
23. Fault-Tolerant? — time
24. Three Storage Testbeds — Ferromagnetic Ising models: — Toom’s rule: — one dimensional
25. Ising model — Ferromagnetic Ising Models — spins on edges of a lattice: — energy of a configuration:
26. Dynamic Ising model (Metropolis update) — Dynamic Ising Models — Interaction with environment causes spin flips — Update rule:
27. Reminder — two-level system perturbatively coupled to a thermal boson bath — “heating” — “cooling”
28. Dynamic Ising model (Metropolis update) — Dynamic Ising Models — Interaction with environment causes spin flips — Update rule (alternate with noise):
29. Toom’s Rule — two dimensional noisy cellular automata — Update rule: — b=majority(n,e,b)
30. Compare and Contrast — Encode information into the system and watch what happens — Redundancy code. — Order parameter is magnetization:
31. Storage — 1D Ising — 2D Ising — Long time behavior (not infinite time, but effectively)
32. 2nd attempt: — 1D Ising — Relaxation to thermal — Imperfect preparation
33. Manipulation — Flipping spins is imperfect — 1D Ising — 2D Ising
34. “Self Fixing” — Excitations point-like — Energy to err is constant — Disordering entropy >> Energy
35. Energy: — sum over neighbors — Energy is proportional to perimeter — Self-Correction
36. Toom’s Rule Versus 2D Ising — 2D Ising — Applied magnetic field (corresponds to a bias in noise) — Toom’s Rule
37. Whence Kitaev’s Model? — Robust storage of quantum information. — But it does not provide a mechanism for — robust manipulation of quantum information.
38. Into the 4th Dimension
39. Quantum Compass Model — XX — XX — ZZ
40. Subsystem Error Correction — Only need to protect subsystem, — not full subspaces. — encoding
41. Shor Stabilizer — Quantum version of parity check matrix — Stabilizer generators: — Define subspace:
42. Shor Redux — Stabilizer generators: — Encodes 9-4=5 qubits of information — Logical operators:
43. Shor Redux
44. Shor Redux Errors
45. Subsystem Code — Stabilizer generators: — plus encoded Z operators — generate all even number of Z’s per row
46. Generalized Shor Subsystem Codes — Two classical codes: C1=[n1,k1,d1] and C2=[n2,k2,d2] — Quantum Shor subspace code [[n1n2,k1k2,min(d1,d2)]] — Number of stabilizers = (n1-k1)n2+(n2-k2)
47. Panos Aliferis/Andrew Cross 2006
48. Quantum Compass Model — XX — XX — ZZ
49. Problems: — no gap in the thermodynamic limit — [Dourier, Becca, Mila 05]
50. ZZ — ZZ — XX — XX
