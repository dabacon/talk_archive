# Quantum Computing Architectures
- **Event / Venue:** UW Architecture 2007 (2007)
- **Format:** `PPT` (`qarch.ppt`)
- **Slides:** 31

## Extracted Slide Text

1. Quantum Computing Architectures — CSE 471 Lecture — May 31, 2007 — Dave Bacon
2. Behind the Bit — bits — noisy bits — quantum bit
3. Bit, Pbit, and Qubit — Configurations: — Description: — Observation:
4. Quantum Computers — 18819881292060796383869723946165043 — 98071635633794173827007633564229888 — 59715234665485319060606504743045317
5. Quantum Simulations — Simulating quantum systems on classical computers is hard — Simulating quantum systems on quantum computers is easy — Quantum algorithms for simulating quantum processes
6. Architectures For Quantum Computers — Small scale (6-8 qubit) quantum computers have been built. — Systems-level challenges to achieving scalable, fault-tolerant — quantum computation
7. The Ideal Quantum Computer — qubits — Quantum algorithm — 1. Initialize
8. “Unique” Quantum Challenges — Quantum info — cannot be copied: — Quantum info
9. Classical Solutions — Use redundancy to protect information against noise — Claude Shannon 1948 — “A mathematical theory of communication”
10. Quantum Error Correcting Codes — “bare” error rate = p — error rate on encoded = O(p2) — By encoding quantum information we can protect it from the
11. More Classical Problems — Classical gates fail with probability p — Solution: error correcting codes + fault tolerant construction — John von Neumann, 1956
12. Fault-Tolerant Quantum Computation — Must design quantum circuits which succeed even when — every element of the circuit (preparation, unitary gates, — measurements) can fail.
13. Perfection Through Concatenation — failure — probability — cp2
14. Architectures For Quantum Computers — Systems-level challenges to achieving scalable, fault-tolerant — quantum computation — Error Correction
15. Building Blocks — qubits — stationary — walking
16. http://iontrap.physics.lsa.umich.edu/ — research/trap — Sketch Ion Trap QC — “electrodes”
17. Time Scales — walking — Example: — ion trap qubits
18. Quantum Memory Hierarchy — Memory error rates << Errors during computation — Error correction more frequent during computation — More ancillas (used for error correction) in compute region
19. Quantum Memory Hierarchy — Slow memory / Fast compute leads to standard cache ideas… — except…
20. Communication — Pf=(p0)k — Distance k — Exponential
21. Quantum Teleportation — 1 qubit — 2 bits — Alice wants to send to Bob
22. Moving Qubits — Teleportation channel — entangled qubits — Entanglement distillation
23. Teleportation Units — Entanglement — Generator — classical control
24. Quantum Architectures — New generation of tools in order to aid in the design of quantum computing architectures….
25. Tools! — High level — description of — fault-tolerant
26. High Level Languages — operator dft(qureg q) { // main operator — const n=#q; // set n to length of input — int i; int j; // declare loop counters
27. Quantum Assembly Language — qubit q0 — qubit q1 — qubit q2
28. Scheduler — Example from Chuang group at http://www.media.mit.edu/quanta
29. Further Resources — Quantum Computing For Computer Scientists (David Mermin): — http://people.ccmr.cornell.edu/~mermin/qcomp/CS483.html — “Standard” Textbook:
30. Quantum Architectures — Today: a taste — On the verge of becoming extremely important — 5-8 qubit ion trap machines
