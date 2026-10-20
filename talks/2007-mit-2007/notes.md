# Shor’s Algorithm
- **Event / Venue:** MIT 2007 (2007)
- **Format:** `PPT` (`mit07.ppt`)
- **Slides:** 61

## Extracted Slide Text

1. Quantum Algorithms Using Clebsch-Gordan Transforms — Dave Bacon — Department of Computer Science & Engineering — University of Washington
2. Err…can you — fix my computer? — Smaller transistors, please! — Physicists and Computer Scientists
3. When Physics and Computer — Science Collide — Email I received from Wim van Dam about FOCS 2006: — Leslie Valiant in his great talk on 'accidental algorithms': "We have all these complexity classes, and we don't know at all if they are diff
4. Theme
5. Physics and Quantum Algorithms — Bottom fig. from quantph/0702144, Farhi, Goldstone, Guttman — energy — time:
6. Factor N: — Find — Either: or must share a — common divisor with
7. Why hard? — Measure second register — First register is (nearly) — symmetric under translation
8. symmetry under — translation — change to momentum basis! — Perform a Fourier Transform!
9. Efficient quantum circuit for quantum Fourier transform: — [Efficient = O(poly[# qubits]) — Factoring — Period Finding
10. Symmetries — Quantum algorithms — The Second Basis Change We Learn In Quantum Mechanics?
11. Singlet: — Triplet: — Clebsch-Gordan Transform — What Use?
12. Collective Unitaries — Symmetry Under n Collective Unitary Rotations
13. Singlet: — Triplet: — The Symmetric Group — Transform Under
14. Quantum Schur Transform — n d-dimensional — systems — (n qudits)
15. Uses of Schur — Young diagram — What does this remind you of? — like probabilities like the spectrum of a density operator
16. The Plethora of Uses of Schur — Optimal spectrum estimation — [M. Keyl and R. F. Werner. Phys. Rev. A, 2001] — Universal distortion-free entanglement concentration
17. But Efficient? — QFT — Schur — Who would need to efficiently calculate Clebsch-Gordan
18. Efficient Schur — [D. Bacon, I.L. Chuang, A. Harrow, Phys. Rev. Lett. 2006] — [D. Bacon, I.L. Chuang, A. Harrow, SODA 2007] — Schur transform to accuracy time
19. The Plethora of Uses of Schur — Optimal spectrum estimation — [M. Keyl and R. F. Werner. Phys. Rev. A, 2001] — Universal distortion-free entanglement concentration
20. But Algorithms?
21. The Hidden Subgroup Problem — Setup: Fix a group (known) and a subgroup (unknown). Given query access to a function f : → S that is constant and distinct on left (right) cosets of in . We say that f hides . — Problem: Find a generating set 
22. “The quantum measurement problem refers to a set of people.” — - Hideo Mabuchi — “The hidden subgroup problem refers to a subgroup of people.” — Hidden Subgroup Disease
23. Why the Fuss? — efficient algorithm for HSP — over (or ) — efficient algorithm for the
24. Graph Isomorphism — Problem: Is there a 1-to-1 mapping from the vertices to the — vertices such that the edges are respected, ? — Mapping to the HSP:
25. Standard Query Model — Uf — Oracle: — Query in equal superposition over group elements
26. You Down With Symmetry? — hidden subgroup state — Symmetry under left regular representation: — Fourier transform over finite group
27. HSP as State Distinction — Given: — Determine: — Maximize: probability of successfully identifying H
28. Holevo’s Condition — Given: — with probability pi — Outcome:
29. Pretty Good — with equal probabilities — Given: — Observation:
30. POE — A Strange Lock — Rotation: — Reflection:
31. Hidden Reflection — Given: — with equal a priori probability — Dihedral HSP
32. Success Probability — Probability of correctly guessing reflection: — number of subsets of x which sum to t — k dimensional vector of elements of
33. Must Work Hard — Theorem: [Bacon, Childs, van Dam 05] — Determining the hidden reflection requires — O(log(N)) copies of the hidden subgroup states.
34. Multicopy — Can we make a measurement on — copies and — learn the subgroup?
35. You Down With Symmetry? — hidden subgroup state — Symmetry under left regular representation: — Symmetry of two copies?
36. Heisenberg Group — Semidirect product group — Elements of the group: — Multiplication rule:
37. Multicopy Success! — [D. Bacon, A.M. Childs, and W. van Dam FOCS 2005] — Efficient algorithm for the Heisenberg HSP: — PGM/optimal measurement approach:
38. Clebsch-Gordan Transform — To The Rescue? — does not have a Clebsch-Gordan related symmetry — Problem:
39. Graph Isomorphism — Problem: Is there a 1-to-1 mapping from the vertices to the — vertices such that the edges are respected, ? — Mapping to the HSP:
40. Conjugate Subgroups — Two subgroups, and , are conjugate if there exists an — element of the group such that — This is an equivalence relation among the subgroups of
41. Hidden Subgroup Conjugacy Problem — Setup: Fix a group (known) and a subgroup (unknown). Given query access to a function f : → S that is constant and distinct on left (right) cosets of in . We say that f hides . — Problem: identify the con
42. Graph Isomorphism — adjacency — matrix — adjacency
43. Relationships — How do the hidden subgroup problem (HSP) and the — hidden subgroup conjugacy problem (HSCP) differ? — 1. If group is abelian, HSCP=HSP
44. Symmetries of HSCP States — Hidden subgroup conjugate state — Hidden subgroup conjugate states — In context of optimal measurement method (PGM)
45. Symmetries of HSCP States — Clebsch-Gordan transform for the regular representation of — finite groups: — What is the extra symmetry of the multiple HSCP states?
46. General Circuit
47. Heisenberg HS State — Restricted subgroups: — Random coset states: — Coset labels:
48. HS States — Perform the QFT over to the first two registers: — Measure these two registers:
49. HS States — Two copies: — Compute v and w:
50. Uncompute — If we could erase the b1,b2 values: — Then a QFT over would find d1 and d2. — Remember v and w are a function of b1 and b2.
