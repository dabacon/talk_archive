# Quantifying Entanglement
- **Event / Venue:** Reed 2006 (2006)
- **Format:** `PPT` (`reed06.ppt`)
- **Slides:** 63

## Extracted Slide Text

1. Physics and Computer Science Through the Lens of Quantum Computing — Dave Bacon — Department of Computer Science & Engineering — University of Washington, Seattle, WA
2. All Apologies
3. Err…can you — fix my computer? — Physics and Computer Science
4. What Gets Me Out of Bed — Intellectual Merit — Practical Consequences — Quantum Information Science
5. Behind the Bit — bits — noisy bits — quantum bit
6. Quantum Computer? — A Famous Bongo Player — “How can we simulate quantum mechanics?...Can we do it with a new kind of computer…a quantum computer? It’s not a Turing machine but a machine of a different kind” — - Richard Feynman (1981)
7. Bit, Noisy bit, and Qubit — Configurations: — Description: — Observation:
8. The Ideal Quantum Computer — qubits — Quantum algorithm — 1. Initialize
9. 18819881292060796383869723 — 94616504398071635633794173 — 82700763356422988859715234 — 66548531906060650474304531
10. Over the Top — “Only time will tell if and when the problems of building a quantum computer can be overcome….As information becomes the world’s most valuable commodity, the economic, political and military fate of nations will depend on the
11. Quantum Algorithms — Quantum algorithms > Classical algorithms — Factoring, discrete log [Shor 94] — Unstructured search [Grover 96]
12. Quantum Computing? — What merit? (beyond new algorithms which scare the NSA) — What gives quantum computers their power — over classical computers
13. Quantum Computer = Parallel Computer? — n qubits = superposition over 2n states — “massively parallel computer”? — NO!
14. Interference? — measure — 50% — 50%
15. Not Interference — Interference is not only quantum mechanical
16. GHZ/Mermin Game — Alice — Input A — Output a
17. GHZ/Mermin Game — Alice — Input A — Output a
18. Bell’s Theorem — space — time — Measurements on space-like separated entangled quantum systems cannot be explained by local classical communication.
19. Minimizing the — Yakking — ALICE — BOB
20. Communication Complexity — [Yao, STOC 79] — [Kushilevitz and Nisan 96] — [Yao, FOCS 93]
21. Quantum Communication — Complexity — [Raz, STOC 99] — There exist functions F(a,b) which require
22. Teleportation (Demystified) — Alice wants to send to Bob — 1 bit — 1 bit
23. Quantum Teleportation — 1 qubit — 2 bits — Alice wants to send to Bob
24. Rehash — [Raz, STOC 99] — There exist functions F(a,b) which require — • (m1/4/log(m)) bits of communication to solve
25. Pure state bipartite entanglement — Entropy of one-half of mixed state is measure of entanglement — Schmidt decomposition: r is the Schmidt rank — Schmidt rank is upper bound on entropy:
26. “Small” Entanglement — n qubits — Theorem [Vidal 03]: If • is O(poly(n)) then there is an efficient — description of the state. If • remains small throughout a quantum computation then there is a O(poly(n)) classical simulation of the quant
27. Matrix Product States — “Small” Entanglement = Efficiently classical simulation — Better classical algorithms for simulating — real world quantum systems?
28. Perimeter “Law” — In many quantum systems, the low energy sector has an entropy of a region which grows like the perimeter of the region — “Small” entanglement
29. DMRGish Algorithm in 2D — [Verstraete, Cirac 04] — Design states which — respect this scaling!
30. Quantum Computing? — What gives quantum computers their power — over classical computers — New classical algorithms for use by physicists!
31. Quantum Computing? — How building a quantum computer will result — in a new phase of matter
32. Two Views of Information — No Information without Physical Representation! — Rolf Landauer — Al Gore
33. The Ideal Quantum Computer — qubits — Quantum algorithm — 1. Initialize
34. Environment — DECOHERENCE — coherent superposition — System
35. More Obstructions — FAULTY CONTROL — System — Controller
36. This is the End, My Only Friend, the End — Everything, (quantum) noisy, all the time. — Is a Quantum Computer Even a Computer? — 1. quantum data is analog
37. Quantum Data is Analog — n qubit quantum state: — Superposition of an exponential number of states. — Each amplitude is a complex number…i.e. analog data
38. Quantum data likes to become classical data — Decoherence is a complex process which is fundamentally — responsible for there being classical information — coherent superposition
39. Quantum Evolution is Analog — Quantum evolution: — A unitary “gate” also has a bunch of complex numbers — Each amplitude is a complex number…i.e. analog data
40. Quantum Theory is Wrong — Quantum theory has only ever been observed for small — (micro to meso) systems. — It will break down for large systems
41. This is the End, My Only Friend, the End — Everything, (quantum) noisy, all the time. — Is a Quantum Computer Even a Computer? — 1. quantum data is analog
42. Classical Solutions — Use redundancy to protect information against noise — Claude Shannon 1948 — “A mathematical theory of communication”
43. More Classical Solutions — Classical gates fail with probability p — Solution: error correcting codes + fault tolerant construction — John von Neumann, 1956
44. Quantum Problems? — No cloning of quantum information — How to perform error correction without measuring? — Quantum errors seem “analog”
45. Quantum Observations — How to perform error correction without measuring? — Observation: not all measurements destroy quantum information — Information encoded into a subspace undisturbed
46. Quantum Observations — By encoding into subspaces we can correct single bit flips
47. Quantum Problems? — Environment — qubit — digitized effects of decoherence
48. Quantum Error Correcting Codes — Encode qubit into 2 dimensional — subspace with all +1 eigenvalues — Single qubit errors (i.e. )
49. Perfection Through Concatenation — failure — probability — cp2
50. Fault-Tolerant Quantum Computation — Must design quantum circuits which succeed even when — every element of the circuit (preparation, unitary gates, — measurements) can fail.
