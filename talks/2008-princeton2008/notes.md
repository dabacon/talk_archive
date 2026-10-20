# Quantum Algorithms Using Clebsch-Gordan Transforms
- **Event / Venue:** Princeton2008 (2008)
- **Format:** `PPT` (`princeton.ppt`)
- **Slides:** 65

## Extracted Slide Text

1. Dave Bacon — University of Washington
2. Quantum Computers — 18819881292060796383869723946165043 — 98071635633794173827007633564229888 — 59715234665485319060606504743045317
3. “Only time will tell if and when the problems of building a — quantum computer can be overcome…. the development — of a fully operational quantum computer would imperil — our personal privacy, destroy electronic commerce and
4. Err…can you — fix my computer? — Smaller transistors, please! — Physicists and Computer Scientists
5. A Golden Era — Email I received from Wim van Dam about FOCS 2006: — Leslie Valiant in his great talk on 'accidental algorithms': "We have all these complexity classes, and we don't know at all if they are different... It would be a nightmar
6. Ronald de Wolf (CWI) — From a 2003 review of three quantum computing books: — “Finally, to all those currently working on yet another book on quantum computing: what this field needs most is more algorithms, not more books.” — HELP WANTED Q
7. Grover-Type — Shor-Type — Factoring, Discrete Logarithm — [Shor 94]
8. Clichéd Question: Where does the power of quantum computers come from? — Retort: Where does the power of classical computers come from? — = powerful exactly why? — NP
9. 1. Lessons from a simple quantum algorithm — 2. Lessons from the symmetric and unitary groups — 3. When at first you don’t succeed…..symmeterize — 4. Quantum algorithms from Clebsch-Gordan transforms
10. Simon’s Problem — Given: A function with n bit strings as input and one bit as — output — Promise: The function is guaranteed to satisfy
11. Classical Simon’s Problem — query pairs — If we find such that then — Querying the function m times….
12. Quantum Simon’s Problem — n qubits — n qubits
13. Quantum Simon’s Problem — For random uniformly distributed — Symmetry: — Symmetry • Simultaneously diagonalize symmetry operators
14. Quantum Simon’s Problem — n qubits — n qubits
15. Quantum Simon’s Problem — Measuring this state, uniformly distributed random such that — Multiple runs: — random
16. Symmetries — Diagonalize with respect to symmetry — Quantum algorithm — Quantum
17. Representation Theory in 1 Slide — Group — Representation of group — Irreducible representations of a group (irreps):
18. Simon’s Problem Redux — Group — addition bitwise mod 2 — Representation of group
19. More Simon’s Problem Redux — random — uniform — are irrep labels
20. Symmetry Interpretation — Clebsch-Gordan transform: — So the “addition” of Gaussian elimination in Simon’s algorithm — can be interpreted as a Clebsch-Gordan transform….
21. Singlet: — Triplet: — Clebsch-Gordan Transform — What Use?
22. Collective Unitaries — Symmetry Under n Collective Unitary Rotations
23. Singlet: — Triplet: — The Symmetric Group — Transform Under
24. Quantum Schur Transform — n d-dimensional — systems — (n qudits)
25. Uses of Schur — Young diagram — What does this remind you of? — like probabilities like the spectrum of a density operator
26. The Plethora of Uses of Schur — Optimal spectrum estimation — [M. Keyl and R. F. Werner. Phys. Rev. A, 2001] — Universal distortion-free entanglement concentration
27. But Efficient? — QFT — Schur — Who would need to efficiently calculate Clebsch-Gordan
28. Efficient Schur — [D. Bacon, I.L. Chuang, A. Harrow, Phys. Rev. Lett. 2006] — [D. Bacon, I.L. Chuang, A. Harrow, SODA 2007] — Schur transform to accuracy time
29. The Plethora of Uses of Schur — Optimal spectrum estimation — [M. Keyl and R. F. Werner. Phys. Rev. A, 2001] — Universal distortion-free entanglement concentration
30. But Quantum Algorithms?
31. The Hidden Subgroup Problem — Setup: Fix a group (known) and a subgroup (unknown). Given query access to a function f : → S that is constant and distinct on left (right) cosets of in . We say that f hides . — Problem: Find a generating set 
32. “The quantum measurement problem refers to a set of people.” — - Hideo Mabuchi — “The hidden subgroup problem refers to a subgroup of people.” — Hidden Subgroup Disease
33. Why the Fuss? — efficient algorithm for HSP — over (or ) — efficient algorithm for the
34. Graph Isomorphism — Problem: Is there a 1-to-1 mapping from the vertices to the — vertices such that the edges are respected, ? — Mapping to the HSP:
35. Standard Query Model — Uf — Oracle: — Query in equal superposition over group elements
36. You Down With Symmetry? — hidden subgroup state — Symmetry under left regular representation: — Fourier transform over finite group
37. Multicopy — Can we make a measurement on — copies and — learn the subgroup?
38. You Down With Symmetry? — hidden subgroup state — Symmetry under left regular representation: — Symmetry of two copies?
39. Heisenberg Group — Semidirect product group — Elements of the group: — Multiplication rule:
40. Multicopy Success! — [D. Bacon, A.M. Childs, and W. van Dam FOCS 2005] — Efficient algorithm for the Heisenberg HSP: — PGM/optimal measurement approach:
41. Clebsch-Gordan Transform — To The Rescue? — does not have a Clebsch-Gordan related symmetry — Problem:
42. Graph Isomorphism — Problem: Is there a 1-to-1 mapping from the vertices to the — vertices such that the edges are respected, ? — Mapping to the HSP:
43. Conjugate Subgroups — Two subgroups, and , are conjugate if there exists an — element of the group such that — This is an equivalence relation among the subgroups of
44. Hidden Subgroup Conjugacy Problem — Setup: Fix a group (known) and a subgroup (unknown). Given query access to a function f : → S that is constant and distinct on left (right) cosets of in . We say that f hides . — Problem: identify the con
45. Symmetries of HSCP States — Hidden subgroup conjugate state — Hidden subgroup conjugate states — In context of optimal measurement method (PGM)
46. Symmetries of HSCP States — Clebsch-Gordan transform for the regular representation of — finite groups: — What is the extra symmetry of the multiple HSCP states?
47. Relationships — How do the hidden subgroup problem (HSP) and the — hidden subgroup conjugacy problem (HSCP) differ? — 1. If group is abelian, HSCP=HSP
48. General Circuit
49. [Bacon, arXiv:quant-ph/0612107] — Heisenberg HSCP and HSP — Heisenberg HSCP ⇒ Heisenberg HSP — Conjugate subgroups are all normal subgroups
50. [Bacon, arXiv:quant-ph/0612107] — Heisenberg HSCP, CG Way — i labels set of conjugate subgroups
