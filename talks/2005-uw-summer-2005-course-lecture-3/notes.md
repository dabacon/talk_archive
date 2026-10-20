# Puzzle
- **Event / Venue:** UW Summer 2005 Course - Lecture 3 (2005)
- **Format:** `PPT` (`Lecture3.ppt`)
- **Slides:** 54

## Extracted Slide Text

1. Puzzle — Twin primes are two prime numbers whose difference is two. — For example, 17 and 19 are twin primes. — Puzzle: Prove that for every twin prime with one prime greater
2. CSEP 590tv: Quantum Computing — Dave Bacon — July 6, 2005 — Today’s Menu
3. Administrivia — Hand in Homework #1 — Pick up Homework #2 — Is anyone not on the mailing list?
4. Recap — The description of a quantum system is a complex vector — Measurement in computational basis gives outcome with — probability equal to modulus of component squared.
5. Recap — Qubits: — Measuring a qubit: — Unitary evolution of a qubit:
6. Goal of This Lecture — Finish off single qubits. Discuss change of basis. — Two qubits. Tensor products. — Deutsch’s Problem
7. Basis? — “Other coordinate system”
8. Resolving a Vector — unit vector — use the dot product to get the component of a vector — along a direction:
9. Expressing In a New Basis — “Other coordinate system”
10. Computational Basis — Computational basis: — is an orthonormal basis: — Kronecker delta
11. A Different Qubit Basis — A different orthonormal basis: — An orthonormal basis is complete if the number of basis elements — is equal to the dimension of the complex vector space.
12. Changing Your Basis — Express the qubit wave function — in the orthonormal complete basis — in other words find component of.
13. Example Basis Change — Express in this basis: — So:
14. Explicit Basis Change — Express in this basis: — So:
15. Basis — We can expand any vector in terms of an orthonormal basis: — Why does this matter? Because, as we shall see next, — unitary matrices can be thought of as either rotating a
16. Unitary Matrices, Row Vectors — Four equations: — Say the row vectors, are an orthonormal basis — For example:
17. Unitary Matrices, Column Vectors — Four equations: — Say the column vectors, are an orthonormal basis — For example:
18. Unitary Matrices, Row & Column — Row vectors — Are orthogonal — Example:
19. Unitary Matrices as “Rotations” — Unitary matrices represent — “rotations” of the complex — vectors
20. Unitary Matrices as “Rotations” — Unitary matrices represent — “rotations” of the complex — vectors
21. Rotations and Dot Products — Unitary matrices represent “rotations” of the complex vectors — Recall: rotations of real vectors preserve angles between vectors — and preserve lengths of vectors.
22. Unitary Matrices, Inner Products — Unitary matrices preserve the inner product of two complex — vectors: — Adjoint-ing rule: reverse order and adjoint elements:
23. Unitary Matrices, Backwards — We can also ask what input vectors given computational basis — vectors as their output: — Because of unitarity:
24. Unitary Matrices, Basis Change — If we express a state — in the row vector basis of — i.e. as
25. Measurement Again — Recall that if we measure a qubit in the computational basis, — the probability of the two outcomes 0 and 1 are — We can express is in a different notation, by using
26. Unitary and Measurement — Suppose we perform a unitary evolution followed by a — measurement in the computational basis: — What are the probabilities of the two outcomes, 0 and 1?
27. Measurement in a Basis — The unitary transform allows to “perform a measurement in — a basis differing from the computational basis”: — Suppose is a complete basis. Then we can
28. Measurement in a Basis — Example:
29. In Class Problem #1
30. Two Qubits — Two bits can be in one of four different states — 00 — 01
31. Two Qubits — Examples:
32. When Two Qubits Are Two — The wave function for two qubits has four components: — Sometimes we can write the wave function of two qubits — as the “tensor product” of two one qubit wave functions.
33. Two Qubits, Separable — Example:
34. Two Qubits, Entangled — Example: — Either — or
35. Measuring Two Qubits — If we measure both qubits in the computational basis, then we — get one of four outcomes: 00, 01, 10, and 11 — If the wave function for the two qubits is
36. Two Qubits, Measuring — Example: — Probability of 00 is — Probability of 01 is
37. Two Qubit Evolutions — Rule 2: The wave function of a N dimensional quantum system — evolves in time according to a unitary matrix . If the wave — function initially is then after the evolution correspond to
38. Two Qubit Evolutions
39. Manipulations of Two Bits — Two bits can be in one of four different states — We can manipulate these bits — 00
40. Manipulations of Two Qubits — Similarly, we can apply unitary operations on only one of the — qubits at a time: — Unitary operator that acts only on the first qubit:
41. Tensor Product of Matrices
42. Tensor Product of Matrices — Example:
43. Tensor Product of Matrices — Example:
44. Tensor Product of Matrices — Example:
45. Tensor Product of Matrices — Example:
46. Two Qubit Quantum Circuits — A two qubit unitary gate — Sometimes the input our output is known to be seperable: — Sometimes we act only one qubit
47. Some Two Qubit Gates — controlled-NOT — control — target
48. Computational Basis and Unitaries — Notice that by examining the unitary evolution of all computational — basis states, we can explicitly determine what the unitary matrix.
49. Linearity — We can act on each computational basis state and then resum — This simplifies calculations considerably
50. Linearity — Example:
