# Architectures for Quantum Computers
- **Event / Venue:** UW Architecture Lecture (2008)
- **Format:** `PPT` (`qarch.ppt`)
- **Slides:** 57

## Extracted Slide Text

1. Architectures for Quantum Computers — CSE 471 Lecture — June 2, 2006 — Dave Bacon
2. Quantum Slander — I think I can safely say that nobody — understands quantum mechanics. — Niels Bohr
3. Do not be intemidated by quantum physicists!
4. Today: Into the Quantum Void — What is a quantum computer? — What, really, is a quantum computer? — DiVincenzo’s criteria
5. New Sizes, New Rules — 10,000nm — 1,000nm — 100nm
6. Quantum Computers — 18819881292060796383869723946165043 — 98071635633794173827007633564229888 — 59715234665485319060606504743045317
7. Quantum Simulations — Simulating quantum systems on classical computers is hard — Simulating quantum systems on quantum computers is easy — Quantum algorithms for simulating quantum processes
8. Bit, Pbit, and Qubit — Configurations: — Description: — Observation:
9. What is a Quantum Computer? — qubits — Quantum algorithm — 1. Initialize
10. Quantum Circuits — Quantum algorithms are usually expressed as families of quantum circuits — WARNING: quantum computers will (probably) not be made of etched circuit boards — corresponding to the above circuits. Quantum circuits = Quantum 
11. But What Will It Look Like? — Solid State — Atomic — Molecular
12. DiVincenzo’s Criteria — David — DiVincenzo — 1. Well defined qubits in a “scalable” architecture
13. Ion Trap — 2 9Be+ Ions in an Ion Trap — (picture from NIST Boulder) — Oscillating electric
14. Where’s the Qubit? — Energy — orbitals — Each ion = 1 qubit
15. Scalable? — . Well defined qubits in a scalable architecture? — More to say about this later!!!
16. DiVincenzo’s Criteria — David — DiVincenzo — 1. Well defined qubits in a “scalable” architecture
17. Measurement — Energy — laser — decay
18. DiVincenzo’s Criteria — David — DiVincenzo — 1. Well defined qubits in a “scalable” architecture
19. Single Qubit Operations — Energy — Laser 1 — Laser 2
20. Initialization — laser — decay — Laser 1
21. DiVincenzo’s Criteria — David — DiVincenzo — 1. Well defined qubits in a “scalable” architecture
22. Universal Computers — Turing machine reads state of tape at current position. — Based on this reading and state of machine, Turing machine writes new symbol at current position and possibly moves left or right. — A Universal Turing Machine 
23. Universal Quantum Computer — U(2) — Universal Quantum Computer — a quantum computer which can be programmed to perform any algorithmic manipulation on quantum information.
24. stationary — Coupling Two Qubits — sloshing mode — These modes can be used as a bus between the qubits.
25. DiVincenzo’s Criteria — David — DiVincenzo — 1. Well defined qubits in a “scalable” architecture
26. What is the Problem? — Real quantum systems are open quantum systems! — system — environment
27. My Mortal Enemy
28. More Obstructions — FAULTY CONTROL — System — Controller
29. Classical Solutions — Use redundancy to protect information against noise — Claude Shannon 1948 — “A mathematical theory of communication”
30. More Classical Solutions — Classical gates fail with probability p — Solution: error correcting codes + fault tolerant construction — John von Neumann, 1956
31. Quantum Error Correcting Codes — “bare” error rate = p — error rate on encoded = O(p2) — By encoding quantum information we can protect it from the
32. Perfection Through Concatenation — failure — probability — cp2
33. Fault-Tolerant Quantum Computation — Must design quantum circuits which succeed even when — every element of the circuit (preparation, unitary gates, — measurements) can fail.
34. Threshold Theorem, ~1996 — QC — “decoherence” — “imprecision”
35. Threshold(s) Theorem(s) — Threshold theorems come in many different forms…. — provable bounds, Monte Carlo estimates, … — different shapes…
36. Ion Trap Parameters — from Thaker et. al. ISCA-33 — ~200 (1-5) • m — Trap Size
37. DiVincenzo’s Criteria — David — DiVincenzo — 1. Well defined qubits in a “scalable” architecture
38. Quantum Computing Architectures — “Large Scale” — Quantum — Architecture
39. A Major Issue — Qubits cannot be copied: — No cloning theorem — Qubits must be moved from place to place, interact with other qubits, etc.
40. Moving Qubits — SWAP channel? — Problem: bandwidth decays exponentially with distance — (SWAP error multiply)
41. Quantum Teleportation — 1 qubit — 2 bits — Alice wants to send to Bob
42. Moving Qubits — Teleportation channel — entangled qubits — Entanglement distillation
43. Teleportation Units — Entanglement — Generator — classical control
44. Quantum Logic Array — Build quantum computer from array of uniform blocks. These blocks can be configured as teleportation units, quantum gates, preparation, and measurement. But each element will have a serious quantum error correcting mic
45. Correcting, Correcting, Correcting — “Quantum Error Correcting” — Microarchitecture — Quantum
46. Quantum CCD Architecture — electrodes — ions — interaction regions
47. Simple Block Architecture — channel — storage
48. Fault-tolerant Procedures
49. Tools! — High level — description of — fault-tolerant
50. High Level Languages — operator dft(qureg q) { // main operator — const n=#q; // set n to length of input — int i; int j; // declare loop counters
