# CSEP 590tv: Quantum Computing
- **Event / Venue:** UW Summer 2005 Course - Lecture 5 (2005)
- **Format:** `PPT` (`Lecture5.ppt`)
- **Slides:** 53

## Extracted Slide Text

1. CSEP 590tv: Quantum Computing — Dave Bacon — July 20, 2005 — Today’s Menu
2. Administrivia — Turn in HW #3. It was meant to be harder than HWs #1 and #2. — Was it? — Pick up HW #4. It should be easier than HW #3.
3. Administrivia — July 20: multi qubit registers, begin quantum algorithms — July 27: quantum algorithms — Aug 3: quantum entanglement
4. Shuttling Around a Corner — Pictures snatched from Chris Monroe’s — University of Michigan website
5. Recap — Matrices in outer product notation — Projectors: — Measurement operators:
6. Recap — Deutsch’s problem. — Distinguishing between constant and balanced. — 2 classical queries
7. Teleportation — 50 % 0, 50 % 1 — 50 % 0, 50 % 1 — Bell basis measurement
8. Teleportation — ALICE — BOB — two qubits
9. Teleportation — ALICE — BOB — We have three qubits whose wave function is
10. Separable, Entangled, 3 Qubits — If we consider qubit 1 as one subsystem and qubits 2 and 3 as — another subsystem, then the state is separable across this divide — However, if we consider qubits 1 and 2 as one system and qubits 3 as one su
11. Separable, Entangled, 3 Qubits — Sometimes we will deal with entangled states across — non adjacent qubits: — How do we even “write” this?
12. Separable, Entangled, 3 Qubits
13. Separable, Entangled, 3 Qubits — When we don’t write subscripts we mean “standard ordering”
14. Teleportation — ALICE — BOB — We have three qubits whose wave function is
15. Teleportation — 50 % 0, 50 % 1 — 50 % 0, 50 % 1 — Bell basis measurement
16. Teleportation — Bell basis — Computational basis — Express this state in terms of Bell basis for first two qubits.
17. Teleportation — Bell basis — Computational basis
18. Teleportation — 50 % 0, 50 % 1 — 50 % 0, 50 % 1 — Bell basis measurement
19. Dropping The Tensor Symbol — Sometimes we will just “drop” the tensor symbol. — “Context” lets us know that there is an implicit tensor product.
20. Teleportation — 50 % 0, 50 % 1 — 50 % 0, 50 % 1 — Bell basis measurement
21. Bell Basis Measurement
22. Teleportation — 50 % 0, 50 % 1 — 50 % 0, 50 % 1 — Bell basis measurement
23. Teleportation — Given the wave function — Measure the first two qubits in the computational basis — Equal ¼ probability for all four outcomes and new states are:
24. Teleportation — 50 % 0, 50 % 1 — 50 % 0, 50 % 1 — Bell basis measurement
25. Teleportation — If the bits sent from Alice to Bob are 00, do nothing — If the bits sent from Alice to Bob are 01, apply a bit flip — If the bits sent from Alice to Bob are 10, apply a phase flip
26. Teleportation — 50 % 0, 50 % 1 — 50 % 0, 50 % 1 — Bell basis measurement
27. Alice — Bob — Alice — Bob
28. Teleportation — 1 qubit = 1 ebit + 2 bits — Teleportation says we can replace transmitting a qubit — with a shared entangled pair of qubits plus two bits of
29. Superdense Coding — Suppose Alice and Bob each have one qubit and the joint — two qubit wave function is the entangled state — Alice wants to send two bits to Bob. Call these bits and .
30. In Class Problem 1
31. Bell Basis — The four Bell states can be turned into each other using — operations on only one of the qubits:
32. Superdense Coding — Alice applies the following operator to her qubit: — Initially: — Bob can uniquely determine which of the four states he has
33. Superdense Coding — Bell basis — measurement
34. Teleportation — 1 qubit = 1 ebit + 2 bits — Teleportation says we can replace transmitting a qubit — with a shared entangled pair of qubits plus two bits of
35. Quantum Algorithms
36. Classical Promise Problem — Query Complexity — Given: A black box which computes some function — k bit input
37. Example — Suppose you are given a black box which computes one of — the following four reversible classical gates: — “identity”
38. Quantum Promise Query Complexity — Given: A quantum gate which, when used as a classical device — computes a reversible function — k qubit input
39. n Qubit Registers — Up until now, we have dealt with only 1,2,3, or 4 qubits. — Now we will deal with n qubits at a time! — n qubits
40. n Qubit States — n qubits have a wave function with complex numbers. — Writing complex numbers down, and keeping track of them — (in a naïve manner) is very computationally inefficient.
41. n Qubit States — properly normalized: — Example: — Notice how compact this 1st notation is.
42. n Qubit Hadamard — Hadamard all n qubits — n qubits — input
43. n Qubit Hadamard — Hadamard one qubit in computational basis: — Hadamard n qubits in computational basis:
44. n Qubit Hadamard — Addition can be done modulo 2 (turns plus to exclusive-or) — Again notice compactness of — notation.
45. Superposition Over All — If we start in the zero bitstring, then Hadmarding all n qubits — creates a superposition over all possible bitstrings:
46. Superposition Over All — Hadamarding the superposition over all states:
47. Superposition Over All
48. Superposition Over All — Could have found in easier fashion using
49. From Comp. Basis to Matrix — From the effect of the Hadamard on the computational basis — We can deduce the form of the matrix in outer product form:
50. Hadamard Basis Elements — Recall that the columns of a matrix form a basis. — What is this basis for the Hadamard? — The basis elements for the Hadmard are:
