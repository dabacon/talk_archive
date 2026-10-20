# CSEP 590tv: Quantum Computing
- **Event / Venue:** UW Summer 2005 Course - Lecture 4 (2005)
- **Format:** `PPT` (`Lecture4.ppt`)
- **Slides:** 67

## Extracted Slide Text

1. CSEP 590tv: Quantum Computing — Dave Bacon — July 13, 2005 — Today’s Menu
2. Administrivia — Hand in HW #2 — Pick up HW #3 (due July 20) — HW #1 solution available on website
3. Recap — Unitary rotations and measurements in different basis — Two qubits. — Separable versus Entangled.
4. Partial Measurements — Say we measure one of the two qubits of a two qubit system: — What are the probabilities of the different measurement — outcomes?
5. Matrices, Bras, and Kets — So far we have used bras and kets to describe row and column — vectors. We can also use them to describe matrices: — Outer product of two vectors:
6. Matrices, Bras, and Kets — We can expand a matrix about all of the computational basis — outer products — Example:
7. Matrices, Bras, and Kets — We can expand a matrix about all of the computational basis — outer products — This makes it easy to operate on kets and bras:
8. Matrices, Bras, and Kets — Example:
9. Projectors — The projector onto a state (which is of unit norm) is given by — Note that — and that
10. Measurement Rule — If we measure a quantum system whose wave function is — in the basis , then the probability of getting the outcome — corresponding to is given by
11. Measuring One of Two Qubits — Suppose we measure the first of two qubits in the computational basis. Then we can form the two projectors: — If the two qubit wave function is then the probabilities of — these two outcomes are
12. Measuring One of Two Qubits — Example: — Measure the first qubit:
13. Instantaneous Communication? — Suppose two distant parties each have a qubit and their — joint quantum wave function is — If one party now measures its qubit, then…
14. In Class Problem 1
15. You Are Now a Quantum Master
16. Important Single Qubit Unitaries — Pauli Matrices: — “bit flip” — “phase flip”
17. Important Single Qubit Unitaries — “bit flip” is just the classical not gate — Hadamard gate: — Jacques Hadamard
18. Single Qubit Manipulations — Use this to compute — But — So that
19. A Cool Circuit Identity — Using
20. Reversible Classical Gates — A reversible classical gate on bits is one to one function on — the values of these bits. — Example:
21. Reversible Classical Gates — A reversible classical gate on bits is one to one function on — the values of these bits. — We can represent reversible classical gates by a permutation
22. Quantum Versions of — Reversible Classical Gates — A reversible classical gate on bits is one to one function on — the values of these bits.
23. David Speaks — David — Deutsch — 1985
24. Deutsch’s Problem — Suppose you are given a black box which computes one of — the following four reversible gates: — “identity”
25. Classical Deutsch’s Problem — “identity” — NOT 2nd bit — controlled-NOT
26. Classical to Quantum Deutsch — “identity” — NOT 2nd bit — controlled-NOT
27. Quantum Deutsch — What if we perform Hadamards before and after the quantum gate:
28. That Last One
29. Again
30. Some Inputs
31. Quantum Deutsch
32. Quantum Deutsch — By querying with quantum states we are able to distinguish — the first two (constant) from the second two (balanced) with — only one use of the quantum gate!
33. In Class Problem 2
34. Quantum Teleportation — Alice — Bob — Alice wants to send her qubit to Bob.
35. Quantum Teleportation — Alice — Bob — Alice wants to send her qubit to Bob.
36. Quantum Teleportation — Classical — Alice — Bob
37. Classical Teleportation — Alice — Bob — (a.k.a. one time pad)
38. Classical Teleportation Circuit — Alice — Bob
39. No information in transmitted bit: — transmitted bit — And it works: — Bob’s bit
40. Quantum Teleportation — Alice — Bob — Alice wants to send her qubit to Bob.
41. Deriving Quantum Teleportation — Our path: We are going to “derive” teleportation — “SWAP” — “Alice”
42. Deriving Quantum Teleportation — Need some way to get entangled states — new equivalent circuit:
43. Deriving Quantum Teleportation — How to generate classical correlated bits: — Inspires: how to generate an entangled state:
44. Deriving Quantum Teleportation — like to use generate entanglement — Alice — Bob
45. Deriving Quantum Teleportation
46. Deriving Quantum Teleportation — entanglement — Alice — Bob
47. Deriving Quantum Teleportation — Use to turn around:
48. Deriving Quantum Teleportation
49. Deriving Quantum Teleportation — 50 % 0, 50 % 1 — 50 % 0, 50 % 1
50. Measurements Through Control — Measurement in the computational basis commutes — with a control on a controlled unitary. — classical
