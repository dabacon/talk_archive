# Quantum Computing
- **Event / Venue:** Italy 2005 Lecture Series - Lecture 2 (2005)
- **Format:** `PPT` (`ItalyLecture2.ppt`)
- **Slides:** 65

## Extracted Slide Text

1. Quantum Computing — Dave Bacon — Department of Computer Science & Engineering — University of Washington
2. Summary of Last Lecture
3. Summary of Last Lecture
4. Ion Trap — 2 9Be+ Ions in an Ion Trap — Oscillating electric — fields trap ions
5. Shuttling Around a Corner — Pictures snatched from Chris Monroe’s — University of Michigan website
6. Qubits — Two dimensional quantum systems are called qubits — A qubit has a wave function which we write as — Examples:
7. Measuring Qubits — A bit is a classical system with two possible states, 0 and 1 — A qubit is a quantum system with two possible states, 0 and 1 — When we observe a qubit, we get the result 0 or the result 1
8. Measuring Qubits — We are given a qubit with wave function — If we observe the system in the computational basis, then we — get outcome 0 with probability
9. Measuring Qubits Continued — When we observe a qubit, we get the result 0 or the result 1 — or — If before we observe the qubit the wave function of the qubit is
10. Measuring Qubits Continued — probability — probability — new wave function
11. Measuring Qubits — We are given a qubit with wave function — If we observe the system in the computational basis, then we — get outcome 0 with probability
12. Measuring Qubits — We are given a qubit with wave function — If we observe the system in the computational basis, then we — get outcome 0 with probability
13. Unitary Evolution for Qubits — Unitary evolution will be described by a two dimensional — unitary matrix — If initial qubit wave function is
14. Unitary Evolution for Qubits
15. Single Qubit Quantum Circuits — Circuit diagrams for evolving qubits — quantum wire — single line = qubit
16. Two Qubits — Two bits can be in one of four different states — 00 — 01
17. Two Qubits — Examples:
18. When Two Qubits Are Two — The wave function for two qubits has four components: — Sometimes we can write the wave function of two qubits — as the “tensor product” of two one qubit wave functions.
19. Two Qubits, Separable — Example:
20. Two Qubits, Entangled — Example: — Either — or
21. Measuring Two Qubits — If we measure both qubits in the computational basis, then we — get one of four outcomes: 00, 01, 10, and 11 — If the wave function for the two qubits is
22. Two Qubits, Measuring — Example: — Probability of 00 is — Probability of 01 is
23. Two Qubit Evolutions — Rule 2: The wave function of a N dimensional quantum system — evolves in time according to a unitary matrix . If the wave — function initially is then after the evolution correspond to
24. Two Qubit Evolutions
25. Manipulations of Two Bits — Two bits can be in one of four different states — We can manipulate these bits — 00
26. Manipulations of Two Qubits — Similarly, we can apply unitary operations on only one of the — qubits at a time: — Unitary operator that acts only on the first qubit:
27. Tensor Product of Matrices
28. Tensor Product of Matrices — Example:
29. Tensor Product of Matrices — Example:
30. Tensor Product of Matrices — Example:
31. Tensor Product of Matrices — Example:
32. Two Qubit Quantum Circuits — A two qubit unitary gate — Sometimes the input our output is known to be seperable: — Sometimes we act only one qubit
33. Some Two Qubit Gates — controlled-NOT — control — target
34. Computational Basis and Unitaries — Notice that by examining the unitary evolution of all computational — basis states, we can explicitly determine what the unitary matrix.
35. Linearity — We can act on each computational basis state and then resum — This simplifies calculations considerably
36. Linearity — Example:
37. Linearity — Example:
38. Some Two Qubit Gates — controlled-NOT — control — target
39. Quantum Circuits — controlled-H — Probability of 10: — Probability of 11:
40. Matrices, Bras, and Kets — So far we have used bras and kets to describe row and column — vectors. We can also use them to describe matrices: — Outer product of two vectors:
41. Matrices, Bras, and Kets — We can expand a matrix about all of the computational basis — outer products — Example:
42. Matrices, Bras, and Kets — We can expand a matrix about all of the computational basis — outer products — This makes it easy to operate on kets and bras:
43. Matrices, Bras, and Kets — Example:
44. Projectors — The projector onto a state (which is of unit norm) is given by — Note that — and that
45. Measurement Rule — If we measure a quantum system whose wave function is — in the basis , then the probability of getting the outcome — corresponding to is given by
46. Measuring One of Two Qubits — Suppose we measure the first of two qubits in the computational basis. Then we can form the two projectors: — If the two qubit wave function is then the probabilities of — these two outcomes are
47. Measuring One of Two Qubits — Example: — Measure the first qubit:
48. Instantaneous Communication? — Suppose two distant parties each have a qubit and their — joint quantum wave function is — If one party now measures its qubit, then…
49. Important Single Qubit Unitaries — Pauli Matrices: — “bit flip” — “phase flip”
50. Important Single Qubit Unitaries — “bit flip” is just the classical not gate — Hadamard gate: — Jacques Hadamard
