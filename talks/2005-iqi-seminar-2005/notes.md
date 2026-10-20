# Wasting Away In Hidden Subgroup Ville
- **Event / Venue:** IQI Seminar 2005 (2005)
- **Format:** `PPT` (`iqi05.ppt`)
- **Slides:** 52

## Extracted Slide Text

1. Wasting Away In Hidden Subgroup Ville — Dave Bacon — Department of Computer Science & Engineering — University of Washington
2. To: Dave Bacon — From: Patrick Hayden — > Tuesday, December 13: IQI Seminar > "Wasting away in hidden subgroup ville" Oh yes. I'm afraid we've seen this before. Obsessive-compulsive manic consumptive research disorder. There is no cure, but
3. In the Beginning There Was…Factoring — 18819881292060796383869723946165043 — 98071635633794173827007633564229888 — 59715234665485319060606504743045317
4. Reaction #1 — Run For the Hills — “Only time will tell if and when the problems of building a quantum computer can be overcome….As information becomes the world’s most valuable commodity, the economic, political and military fate of nations
5. Reaction #2 — Not Even Wrong — http://mywebpages.comcast.net/mycommon/Quantum_Computing_Myths.PDF
6. Reaction #3 — Dreams of Future Algorithms — “For my part I know nothing with any certainty, but the sight of the stars makes me dream.” – Vincent van Gogh
7. “I wasted time, — and now doth time waste me” — Caltech SURF, 1996 — “That was a hard problem.” – John Preskill
8. Revolutions — 1984: Green and Schwarz anomaly cancellations — 1994: Dualities between string theories — String Theory Revolutions
9. Hidden Subgroup Problem
10. Today — Where are we going? Why are we going there? — Structure of the Problem?
11. Shor’s Factoring Algorithm — Factoring can be reduced to order finding — Order finding can be reduced to period finding. — period=r
12. Groups — Group — elements: — group multiplication:
13. Shor’s Hidden Subgroup — iff — Given query access to a function with the promise — Subgroup
14. Shor’s Hidden Subgroup — Given query access to a function with the promise — is constant and distinct on cosets of
15. Cosets — Left cosets — Unless is normal, then the left and right cosets do not coincide — Right cosets
16. Hidden Subgroup Problem — Setup: Fix a group (known) and a subgroup (unknown). Given query access to a function f : → S that is constant and distinct on left (right) cosets of in . We say that f hides . — Problem: Find a generating set for 
17. Why the HSP? — efficient algorithm for HSP — over (or ) — efficient algorithm for the
18. Graph Isomorphism — Problem: Is there a 1-to-1 mapping from the vertices to the — vertices such that the edges are respected, ? — Mapping to the HSP:
19. Graph Isomorphism — Problem: Is there a 1-to-1 mapping from the vertices to the — vertices such that the edges are respected, ? — Mapping to the HSP:
20. Conjugate Subgroups — Two subgroups, and , are conjugate if there exists an — element of the group such that — This is an equivalence relation among the subgroups of
21. Hidden Subgroup Conjugacy Problem — Setup: Fix a group (known) and a subgroup (unknown). Given query access to a function f : → S that is constant and distinct on left (right) cosets of in . We say that f hides . — Problem: identify the con
22. Graph Isomorphism — Problem: Is there a 1-to-1 mapping from the vertices to the — vertices such that the edges are respected, ? — Mapping to the HSCP:
23. Relationships — How do the hidden subgroup problem (HSP) and the — hidden subgroup conjugacy problem (HSCP) differ? — 1. If group is abelian, HSCP=HSP
24. Dihedral Group — Dihedral group — group of symmetries of a N sided — regular polygon
25. Dihedral HSP — Theorem [Ettinger, Hoyer 98] — Sufficient to solve Dihedral HSP when subgroups are — limited to
26. Modification — Modify the function hiding the subgroup: — If is even, then is constant and distinct on left cosets — of
27. Modification — Modify the function hiding the subgroup: — left cosets: — Using more functions, we can determine 2nd least significant
28. HSP and HSCP — More generally, we can ask if this method can be extended to work for any group/set of subgroups?
29. Why the HSCP? — The HSCP has more “symmetry” than the HSP
30. Standard Query Model — constant and distinct on different left cosets of — hidden subgroup state — random left coset state
31. Multiple Queries — If we make a single measurement on the — HS state, can we distinguish different — NO
32. Multiple Queries Approaches — Existential — explicit measurement, — exponentially sized circuit
33. Symmetries — left regular representation — right regular representation — they commute
34. Symmetries of HS States — left regular representation — right regular representation
35. Symmetries of HS States — left regular representation — right regular representation — via Schur’s lemma this implies
36. State Distinguishablity — Given with probability — Find measurement which maximizes probability of successfully — identifying
37. State Distinguishablity — HSCP: we don’t care about which subgroup, just it’s conjugacy. New problem — HSC state — Probability:
38. Single HSC State — Single HSC state is completely diagonalized (like Abelian!)
39. Dihedral HSCP — 2 one dimensional irreps — Dihedral group — two dimensional irreps
40. Optimal Measurement? — Pretty good measurement: — For Dihedral group HSCP, PGP is — But this is not the optimal measurement!
41. Multiple Query HSC States — Diagonal representation of the group
42. Multiple Query HSC States — Diagonal representation of the group
43. Clebsch-Gordan Decomposition — Averaging over this representation, — implies
44. General Circuit
45. Quantum Algorithms for HSCP — 1. Prepare m copies of the HS state. — 2. Perform the QFT over on each copy. — efficient circuits for most groups of interest
46. Schur Transform — (work with Aram Harrow and Isaac Chaung) — set of all partitions of n — (all Young Diagrams with n rows)
47. A Partial Solution — Generalized Kitaev circuit can be — used to project onto CG subspaces
48. A Partial Solution — Representation theory problem: — Given, irreps, and sum in CG series, — perform permutation between
49. What’s My Point? — HSCP is (in the important instances at least) — polynomial time equivalent to the HSP — 2. In the same way that symmetry implies we should
50. The Future — Efficient circuits for Clebsch-Gordan transforms over — finite groups? — Identification of symmetries of the multiplicity space of
