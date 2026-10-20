# Obligatory Feynman Anecdote
- **Event / Venue:** UW Condensed Matter AMO 2007 (2007)
- **Format:** `PPT` (`Dave Bacon ftaqc.ppt`)
- **Slides:** 55

## Extracted Slide Text

1. When Physics and Computer Science Collide — A Cross Cultural Extravaganza — Dave Bacon — Department of Computer Science & Engineering
2. Err…can you — fix my computer? — Smaller transistors, please!
3. Biologist — Physicist — Wow that biophysicist sure knows a lot of physics! — Wow that biophysicist sure knows a lot of biology!
4. My Goal — Quantum — Algorithms — Fault-Tolerant
5. Quantum Computer? — Richard Feynman — “How can we simulate quantum mechanics? ...Can we do it with a new kind of computer… a quantum computer? It’s not a Turing machine but a machine of a different kind” - Richard Feynman (1981) — simulatin
6. Quantum Computers! — Public Key Cryptosystems — RSA — Diffie-Hellman
7. Quantum Computer — qubits — Quantum algorithm — 1. Initialize
8. Factor N: — Find — Either: or must share common — common divisor with
9. Why hard? — Measure second register — First register is (nearly) — symmetric under translation
10. symmetry under — translation — change to momentum basis! — Perform a Fourier Transform!
11. Efficient quantum circuit for quantum Fourier transform: — [Efficient = O([# qubits]2) — Factoring — Period Finding
12. Symmetries — Quantum algorithms — The Second Basis Change We Learn In Quantum Mechanics?
13. Singlet: — Triplet: — Clebsch-Gordan Transform — What Use?
14. Collective Unitaries — Symmetry Under n Collective Unitary Rotations
15. Singlet: — Triplet: — The Symmetric Group — Transform Under
16. Quantum Schur Transform — n d-dimensional — systems — (n qudits)
17. What Use, This Symmetry? — Young diagram — Spectrum — “Optimal” estimate of spectrum
18. The Plethora of Uses of Schur — Optimal spectrum estimation — [M. Keyl and R. F. Werner. Phys. Rev. A, 2001] — Universal distortion-free entanglement concentration
19. But Efficient? — QFT — Schur — Who would need to efficiently calculate Clebsch-Gordan
20. Efficient Schur — [D. Bacon, I.L. Chuang, A. Harrow, Phys. Rev. Lett. 2006] — [D. Bacon, I.L. Chuang, A. Harrow, SODA 2007] — Schur transform to accuracy time
21. The Plethora of Uses of Schur — Optimal spectrum estimation — [M. Keyl and R. F. Werner. Phys. Rev. A, 2001] — Universal distortion-free entanglement concentration
22. But Algorithms?
23. The Hidden Subgroup Problem — Setup: Fix a group (known) and a subgroup (unknown). Given query access to a function f : → S that is constant and distinct on left (right) cosets of in . We say that f hides . — Problem: Find a generating set 
24. Why the Fuss? — efficient algorithm for HSP — over (or ) — efficient algorithm for the
25. Standard Query Model — Uf — Oracle: — Query in equal superposition over group elements
26. You Down With Symmetry? — hidden subgroup state — Symmetry under left regular representation: — Fourier transform over finite group
27. Multicopy — Can we make a measurement on — copies and — learn the subgroup?
28. Clebsch-Gordan Transform — To The Rescue? — does not have a Clebsch-Gordan related symmetry — Problem:
29. Bring the Symmetry to the Problem — Clebsch-Gordan Transform — To The Rescue! — Hidden Subgroup Problem
30. Entangled Measurement
31. Pure state bipartite entanglement — Entropy of one-half of mixed state is measure of entanglement
32. “Small” Entanglement — n qubits — Theorem [Vidal 03]: If • is O(poly(n)) then there is an efficient — description of the state. If • remains small throughout a quantum computation then there is a O(poly(n)) classical simulation of the quant
33. Matrix Product States — “Small” Entanglement = Efficiently classical simulation — Better classical algorithms for simulating — real world quantum systems?
34. Perimeter “Law” — In “many” quantum systems, the low energy sector has an entropy of a region which grows like the perimeter of the region — “Small” entanglement
35. DMRGish Algorithm in 2D — [Verstraete, Cirac 04] — Design states which — respect this scaling!
36. DMRGish Algorithm — Gregory Crosswhite — UW Physics Grad Student — But what to simulate with these new algorithms?
37. The Ideal Quantum Computer — qubits — Quantum algorithm — 1. Initialize
38. Environment — DECOHERENCE — coherent superposition — System
39. More Obstructions — FAULTY CONTROL — System — Controller
40. This is the End, My Only Friend, the End — Everything, (quantum) noisy, all the time. — Is a Quantum Computer Even a Computer? — 1. quantum data is analog
41. Classical Solutions — Use redundancy to protect information against noise — Claude Shannon 1948 — “A mathematical theory of communication”
42. More Classical Solutions — Classical gates fail with probability p — Solution: error correcting codes + fault tolerant construction — John von Neumann, 1956
43. Quantum Threshold Theorem — QC — “decoherence” — “imprecision”
44. Fault-Tolerant Quantum Computation — Must design quantum circuits which succeed even when — every element of the circuit (preparation, unitary gates, — measurements, doing nothing) can fail.
45. Sudden Approximation — Quantum circuit model — Computing in the — sudden approximation
46. Adiabatic Approximation — Time dependent — Hamiltonian: — energy
47. Adiabatic Quantum Algorithms — [E. Farhi, J. Goldstone, S. Gutmann, and M. Sipser, 2000] — 1. Prepare ground state of — 2. “Slowly” evolve
48. Universal Adiabatic — Quantum Computation — Adiabatic quantum computation • The quantum circuit model — [D. Aharonov, W. van Dam, J. Kempe, Z. Landau, S. Lloyd, O. Regev, 2004]
49. But Realistic? — [D. Aharonov, W. van Dam, J. Kempe, Z. Landau, S. Lloyd, O. Regev, 2004] — 3-qubit Hamiltonians — 2-qubit Hamiltonians
50. But Fault-Tolerant? — energy — time: — Stay in ground state:
