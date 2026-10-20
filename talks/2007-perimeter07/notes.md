# Shor’s Algorithm
- **Event / Venue:** Perimeter07 (2007)
- **Format:** `PPT` (`blackberryhole07.ppt`)
- **Slides:** 63

## Extracted Slide Text

1. Nothing Here
2. Quantum Algorithms Using Clebsch-Gordan Transforms — Dave Bacon — Department of Computer Science & Engineering — University of Washington
3. A Brief History of Hiring in Quantum Computing
4. Err…can you — fix my computer? — Smaller transistors, please! — Physics and Computer Science
5. Email I received from Wim van Dam about FOCS 2006: — Leslie Valiant in his great talk on 'accidental algorithms': "We have all these complexity classes, and we don't know at all if they are different... It would be a nightmare if they turn 
6. They’re Not Scared? — Q: Does quantum computing really belong in CS departments, as opposed to physics departments? — A: It belongs if we want it to belong! In my experience, the physicists have a bigger hurdle than the computer scientists 
7. Can Physicist Contribute Quantum Algorithms? — Bottom fig. from quantph/0702144, Farhi, Goldstone, Guttman — energy — time:
8. Factor N: — Find — Either: or must share a — common divisor with
9. Why hard? — Measure second register — First register is (nearly) — symmetric under translation
10. symmetry under — translation — change to momentum basis! — Perform a Fourier Transform!
11. Efficient quantum circuit for quantum Fourier transform: — [Efficient = O(poly[# qubits]) — Factoring — Period Finding
12. Symmetries — Quantum algorithms — The Second Basis Change We Learn In Quantum Mechanics?
13. Singlet: — Triplet: — Clebsch-Gordan Transform — What Use?
14. Collective Unitaries — Symmetry Under n Collective Unitary Rotations
15. Singlet: — Triplet: — The Symmetric Group — Transform Under
16. Quantum Schur Transform — n d-dimensional — systems — (n qudits)
17. Uses of Schur — Young diagram — What does this remind you of? — like probabilities like the spectrum of a density operator
18. The Plethora of Uses of Schur — Optimal spectrum estimation — [M. Keyl and R. F. Werner. Phys. Rev. A, 2001] — Universal distortion-free entanglement concentration
19. But Efficient? — QFT — Schur — Who would need to efficiently calculate Clebsch-Gordan
20. Efficient Schur — [D. Bacon, I.L. Chuang, A. Harrow, Phys. Rev. Lett. 2006] — [D. Bacon, I.L. Chuang, A. Harrow, SODA 2007] — Schur transform to accuracy time
21. The Plethora of Uses of Schur — Optimal spectrum estimation — [M. Keyl and R. F. Werner. Phys. Rev. A, 2001] — Universal distortion-free entanglement concentration
22. But Algorithms?
23. The Hidden Subgroup Problem — Setup: Fix a group (known) and a subgroup (unknown). Given query access to a function f : → S that is constant and distinct on left (right) cosets of in . We say that f hides . — Problem: Find a generating set 
24. “The quantum measurement problem refers to a set of people.” — - Hideo Mabuchi — “The hidden subgroup problem refers to a subgroup of people.” — Hidden Subgroup Disease
25. Why the Fuss? — efficient algorithm for HSP — over (or ) — efficient algorithm for the
26. Graph Isomorphism — Problem: Is there a 1-to-1 mapping from the vertices to the — vertices such that the edges are respected, ? — Mapping to the HSP:
27. Standard Query Model — Uf — Oracle: — Query in equal superposition over group elements
28. You Down With Symmetry? — hidden subgroup state — Symmetry under left regular representation: — Fourier transform over finite group
29. Multicopy — Can we make a measurement on — copies and — learn the subgroup?
30. You Down With Symmetry? — hidden subgroup state — Symmetry under left regular representation: — Symmetry of two copies?
31. Heisenberg Group — Semidirect product group — Elements of the group: — Multiplication rule:
32. Multicopy Success! — [D. Bacon, A.M. Childs, and W. van Dam FOCS 2005] — Efficient algorithm for the Heisenberg HSP: — PGM/optimal measurement approach:
33. Clebsch-Gordan Transform — To The Rescue? — does not have a Clebsch-Gordan related symmetry — Problem:
34. Graph Isomorphism — Problem: Is there a 1-to-1 mapping from the vertices to the — vertices such that the edges are respected, ? — Mapping to the HSP:
35. Conjugate Subgroups — Two subgroups, and , are conjugate if there exists an — element of the group such that — This is an equivalence relation among the subgroups of
36. Hidden Subgroup Conjugacy Problem — Setup: Fix a group (known) and a subgroup (unknown). Given query access to a function f : → S that is constant and distinct on left (right) cosets of in . We say that f hides . — Problem: identify the con
37. Relationships — How do the hidden subgroup problem (HSP) and the — hidden subgroup conjugacy problem (HSCP) differ? — 1. If group is abelian, HSCP=HSP
38. Symmetries of HSCP States — Hidden subgroup conjugate state — Hidden subgroup conjugate states — In context of optimal measurement method (PGM)
39. Symmetries of HSCP States — Clebsch-Gordan transform for the regular representation of — finite groups: — What is the extra symmetry of the multiple HSCP states?
40. General Circuit
41. [Bacon, arXiv:quant-ph/0612107] — Heisenberg HSCP and HSP — Heisenberg HSCP ⇒ Heisenberg HSP — Conjugate subgroups are all normal subgroups
42. [Bacon, arXiv:quant-ph/0612107] — Heisenberg HSCP, CG Way — i labels set of conjugate subgroups
43. [Bacon, arXiv:quant-ph/0612107] — Heisenberg HSCP, CG Way — i can be found by performing — and performing a QFT
44. Heisenberg HS State — Restricted subgroups: — Random coset states: — Coset labels:
45. HS States — Perform the QFT over to the first two registers: — Measure these two registers:
46. HS States — Two copies: — Compute v and w:
47. Uncompute — If we could erase the b1,b2 values: — Then a QFT over would find d1 and d2. — Remember v and w are a function of b1 and b2.
48. Solving Equations — Compute v and w: — For fixed x1,x2,y1,y2 let be the set of b1,b2 — solutions to these equations.
49. Solving Equations — Easier to think about the inverse (do it unitarily): — i.e. given v and w, transform to superposition over — solutions to the equations
50. Solving Equations — Assuming y1,y2,y1+y2 do not equal 0 (prob O(1/p)), — then — solutions have
