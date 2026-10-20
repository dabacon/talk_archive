# Building Robust Qubits
- **Event / Venue:** APS NW Tacoma (2008)
- **Format:** `PPT` (`apsnw.ppt`)
- **Slides:** 34

## Extracted Slide Text

1. Building Robust Qubits — Dave Bacon — Department of Computer Science & Engineering — University of Washington
2. My Mortal Enemy
3. Success Stories — Life — Computers — How is it that nearly error free behavior can arise from
4. What is a Quantum Computer? — qubits — Quantum algorithm — 1. Initialize
5. Why Build a Quantum Computer? — Original answer: [Peter Shor 1994] — 18819881292060796383869723 — 94616504398071635633794173
6. Why Build a Quantum Computer? — Today’s answer: — Factoring, discrete log [Shor 94] — Unstructured search [Grover 96]
7. Environment — DECOHERENCE — coherent superposition — System
8. More Obstructions — FAULTY CONTROL — System — Controller
9. Classical Solutions — Use redundancy to protect information against noise — Claude Shannon 1948 — “A mathematical theory of communication”
10. More Classical Solutions — Classical gates fail with probability p — Solution: error correcting codes + fault tolerant construction — John von Neumann, 1956
11. Quantum Problems? — No cloning of quantum information — How to perform error correction without measuring? — Quantum errors seem “analog”
12. Quantum Observations — How to perform error correction without measuring? — Observation: not all measurements destroy quantum information — Information encoded into a subspace undisturbed
13. Quantum Observations — By encoding into subspaces we can correct single bit flips
14. Quantum Problems? — Environment — qubit — digitized effects of decoherence
15. Quantum Error Correcting Codes — Encode qubit into 2 dimensional — subspace with all +1 eigenvalues — Single qubit errors (i.e. )
16. Fault-Tolerant Quantum Computation — Must design quantum circuits which succeed even when — every element of the circuit (preparation, unitary gates, — measurements) can fail.
17. Perfection Through Concatenation — failure — probability — cp2
18. Threshold Theorem, ~1996 — QC — “decoherence” — “imprecision”
19. Threshold(s) Theorem(s) — Threshold theorems come in many different forms…. — provable bounds, Monte Carlo estimates, … — different shapes…
20. Back To Reality — theory — practice — Practical devices of information processing enact the ideas of
21. Toy Model — Ising model in two+ dimensions — Redundancy code:
22. Relaxation to thermal — Imperfect preparation — Robust — The two encoded states have lifetimes which grow with the size
23. Do there exist (or can we engineer) quantum systems whose — physics guarantees fault-tolerant quantum computation? — Today in QC: we have theory (like von Neumann, Shannon) but not devices which implement these idea (without severe device c
24. Quantum Error Correction — encoded — quantum — information
25. A Start — 5 qubit quantum error correcting code — Hamiltonian such that ground state is this error correcting code — (ground state is twofold degenerate):
26. Two Body? — Problem: four qubit interactions? Bleh. — XX — XX
27. ground state is +1 eigenvalue of four qubit interactions
28. Problem? — free energy — Relative number — of errors
29. Degenerate Codes to the Rescue — Some errors, have no effect on the codespace, for example si — This leads to the concept of degenerate quantum codes — [Bacon, Phys. Rev. A, 73, 012340 (2006)]
30. Mountains, Molehills — -1 — -2 — energy
31. Mountains into Molehills — Long range quantum compass model — energy — Low energy spectrum for L=4,
32. Into The Third Dimension
33. Towards Robust Qubits — Wire many faulty — qubits together into a fault-tolerant scheme — Engineer physical systems whose physics enacts error correction
34. Toy Model — Ising model in two+ dimensions — Redundancy code:
