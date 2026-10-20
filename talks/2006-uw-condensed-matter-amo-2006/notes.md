# Building Robust Qubits Using Many-Body Strongly Interacting Quantum Systems
- **Event / Venue:** UW Condensed Matter AMO 2006 (2006)
- **Format:** `PPT` (`valentines.ppt`)
- **Slides:** 61

## Extracted Slide Text

1. Building Robust Qubits Using Many-Body Strongly Interacting Quantum Systems — Dave Bacon, Principal Research Scientist — Department of Computer Science & Engineering — University of Washington
2. Happy Valentine’s Day
3. Quantum World, Quantum Computers — “Nature isn't classical, dammit, and if you want to make a simulation of Nature, you'd better make it quantum mechanical, and by golly it's a wonderful problem, because it doesn't look so easy.” — – Richar
4. Shor’s Algorithm (1994) — 18819881292060796383869723946165043 — 98071635633794173827007633564229888 — 59715234665485319060606504743045317
5. Perspective — GREATEST COMMON DIVISOR — gcd(1020,153)=gcd(153,102) — 1020 = 6×153+102
6. Two Quests — What can quantum — information processing — devices do?
7. Building Battle Royale — Physics — Computer Science & Engineering — Who will dominate construction of a large scale quantum computer?
8. A Different Path — I will argue that the path to constructing a robust large scale — quantum computer will look nothing like what is currently — envisioned, but instead will be achieved via a careful application
9. Environment — Problem Child — decoherence: — coherent superposition
10. Problem Solution — QC — “decoherence” — “imprecision”
11. Sketch: How It Works — To make robust elements, information is encoded into a quantum — error correcting codes of significant size and fault-tolerant methods — are used for gates, preparation, measurement, and correction
12. In Practice? — 13000 ions, 1000 laser beams, 160000 electrodes in ion trap — The device complexity simply to engineer robust qubits is severe — “A quantum computer will spend most of its time doing error correction.”
13. Quantum Error Correction — encoded — quantum — information
14. The Quantum Hard Drive? — Kitaev — Do there exist (or can we engineer) quantum systems whose — physics guarantees fault-tolerant quantum computation?
15. Kitaev’s Model — qubits on links — plaque operators: — vertex operators:
16. Kitaev’s Model, Continued — plaque operators: — vertex operators: — Hamiltonian
17. Topology of Operators — products of vertex operators — are closed loops of Z’s which — are homologically trivial
18. Degeneracy — Hamiltonian — plaque operators: — vertex operators:
19. Kitaev’s Model — plaque operators: — vertex operators: — anti-commutes with
20. Excitations — excitations particles come in pairs (particle/antiparticle) — at end of “error” chains — two types of particles, X-type (live on vertices of dual lattice)
21. A Qubit — Moving an X or Z type particle on a homologically nontrivial — path and annihilating with it’s partner preserves the ground — states
22. Two Qubits — Moving an X or Z type particle on a homologically nontrivial — path and annihilating with it’s partner preserves the ground — states
23. Anyons Anyone? — Phase:
24. Topological Protection — Encode two qubits — into the ground state — gap
25. Topological Quantum Computing — Encode two qubits — into the ground state — gap
26. Topological Error Correction — Different mode of using Kitaev’s Model, as a component in — a fault-tolerant quantum computer, encode into ground state — 1. Errors occur
27. Fault-Tolerant? — Encode two qubits — into the ground state — gap
28. What is a Computer? — What is the phase of matter corresponding to the computer? — Practical question (as opposed to philosophical) — There are distinct physical reasons why robust classical
29. No Quantum Transistor? — Quantum Cloning Machine — “A single quantum cannot be cloned,” Wootters and Zurek, Nature, 1982
30. To Build a Quantum Computer — Classical — Problem (1938): How to build a reliable system from — unreliable components?
31. Three Storage Testbeds — Ferromagnetic Ising models: — Toom’s rule: — one dimensional
32. Ising model — Ferromagnetic Ising Models — spins on edges of a lattice: — energy of a configuration:
33. Dynamic Ising model (Metropolis update) — Dynamic Ising Models — Interaction with environment causes spin flips — Update rule:
34. Reminder — two-level system perturbatively coupled to a thermal boson bath — “heating” — “cooling”
35. Dynamic Ising model (Metropolis update) — Dynamic Ising Models — Interaction with environment causes spin flips — Update rule (alternate with noise):
36. Toom’s Rule — two dimensional noisy cellular automata — Update rule: — b=majority(n,e,b)
37. Compare and Contrast — Encode information into the system and watch what happens — Redundancy code. — Order parameter is magnetization:
38. Storage — 1D Ising — 2D Ising — Long time behavior (not infinite time, but effectively)
39. 2nd attempt: — 1D Ising — Relaxation to thermal — Imperfect preparation
40. Manipulation — Flipping spins is imperfect — 1D Ising — 2D Ising
41. “Self Fixing” — Excitations point-like — Energy to err is constant — Disordering entropy >> Energy
42. Toom’s Rule Versus 2D Ising — 2D Ising — Applied magnetic field (corresponds to a bias in noise) — Toom’s Rule
43. Whence Kitaev’s Model? — Robust storage of quantum information. — But it does not provide a mechanism for — robust manipulation of quantum information.
44. Goal — 1. Many-body quantum system with degeneracy due to — existence of quantum error correcting code — 2. “Self-correcting”
45. Quantum Compass Model — XX — XX — ZZ
46. Subsystem Error Correction — Only need to protect subsystem, — not full subspaces. — encoding
47. Quantum Compass Model — XX — XX — ZZ
48. Subsystem Error Correction — Measure: — Diagnose error and apply fix. Fix may apply operator of form — But this commutes with
49. Problems: — no gap in the thermodynamic limit — [Dourier, Becca, Mila 05]
50. ZZ — ZZ — XX — XX
