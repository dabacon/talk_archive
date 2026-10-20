# The Hidden Subgroup Conjugacy
- **Event / Venue:** Poster - sandiego06 (2006)
- **Format:** `PPT` (`sandiego06.ppt`)
- **Slides:** 34

## Extracted Slide Text

1. The Hidden Subgroup Conjugacy — Problem and Beyond — Dave Bacon — Computer Science & Engineering, University of Washington
2. State of the Art — Quantum Algorithms — Factoring, discrete log [Shor 94] — Unstructured search [Grover 96]
3. The Hidden Subgroup Problem — Setup: Fix a group (known) and a subgroup (unknown). Given query access to a function f : → S that is constant and distinct on left (right) cosets of in . We say that f hides . — Problem: Find a generating set 
4. Why the Fuss? — efficient algorithm for HSP — over (or ) — efficient algorithm for the
5. Hidden Subgroup Successes — Abelian groups [Shor 94; Kitaev 95] — [Püschel, Rötteler, Beth 98] — Normal subgroups [Hallgren, Russell, Ta-Shma 00]
6. Standard Query Model — Uf — Oracle: — Query in equal superposition over group elements
7. Graph Isomorphism — Problem: Is there a 1-to-1 mapping from the vertices to the — vertices such that the edges are respected, ? — Mapping to the HSP:
8. Conjugate Subgroups — Two subgroups, and , are conjugate if there exists an — element of the group such that — This is an equivalence relation among the subgroups of
9. Hidden Subgroup Conjugacy Problem — Setup: Fix a group (known) and a subgroup (unknown). Given query access to a function f : → S that is constant and distinct on left (right) cosets of in . We say that f hides . — Problem: identify the con
10. Relationships — How do the hidden subgroup problem (HSP) and the — hidden subgroup conjugacy problem (HSCP) differ? — 1. If group is abelian, HSCP=HSP
11. Graph Isomorphism — adjacency — matrix — adjacency
12. Dihedral Group — Dihedral group — group of symmetries of a N sided — regular polygon
13. Dihedral HSP — Theorem [Ettinger, Hoyer 98] — Sufficient to solve Dihedral HSP when subgroups are — limited to
14. Modification — Modify the function hiding the subgroup: — If is even, then is constant and distinct on left cosets — of
15. Modification — Modify the function hiding the subgroup: — left cosets: — Using more functions, we can determine 2nd least significant
16. Why the HSCP? — The HSCP has more symmetry than the HSP
17. Multiple Queries — If we make a single measurement on the — HS state, can we distinguish different — In general, NO
18. Multiple Queries — Can we make a measurement on — copies and — learn the subgroup?
19. Symmetries — left regular representation — right regular representation — they commute
20. Symmetries of HS States — left regular representation — right regular representation
21. Symmetries of HS States — left regular representation — right regular representation — via Schur’s lemma this implies
22. State Distinguishablity — Given with probability — Find measurement which maximizes probability of successfully — identifying
23. State Distinguishablity — HSCP: we don’t care about which subgroup, just it’s conjugacy. New problem — HSC state — Probability:
24. Single HSC State — Single HSC state is completely diagonalized (like Abelian!)
25. Dihedral HSCP — 2 one dimensional irreps — Dihedral group — two dimensional irreps
26. Optimal Measurement? — Pretty good measurement: — For Dihedral group HSCP, PGP is — But this is not the optimal measurement!
27. Multiple Query HSC States — Diagonal representation of the group
28. Clebsch-Gordan Decomposition — Averaging over this representation, — implies
29. General Circuit
30. Quantum Algorithms for HSCP — 1. Prepare m copies of the HS state. — 2. Perform the QFT over on each copy. — efficient circuits for most groups of interest
31. The Second Role of Symmetry — Without efficient circuits for the quantum Fourier transform, — all is for naught! — Second role of symmetries:
32. Clebsch-Gordan — [Bacon, Chuang, Harrow 04,06] Schur Transform — Clebsch-Gordan transform for U(d) — U(d) subgroup adapted basis (Gelfand-Zetlin basis)
33. The To Do List! — Are the hidden subgroup conjugacy problem and the hidden subgroup problem equivalent? — For which groups are they equivalent? — Explicit understanding of the Clebsch-Gordan symmetry involved in the dihedral and symmetric g
34. Gregory Crosswhite, Graduate Student, Physics — Funded by — Dave Bacon, Research Assistant Professor — Paul Pham, Graduate Student, CS
