# Tht Yuo Cna Reda Ths Snetnce
- **Event / Venue:** Singapore 2005 - Hidden Subgroup Problem (2005)
- **Format:** `PPT` (`hsp.ppt`)
- **Slides:** 44

## Extracted Slide Text

1. Tht Yuo Cna Reda Ths Snetnce — Impls Tat Yor Mnid Cna Efncenlty Solev — NP-Cmoplet Prbolems???
2. New Quantum Algorithms for the — Hidden Subgroup Problem — Dave Bacon — Department of Computer Science & Engineering
3. Quantum Algorithms — “If I had a good idea in quantum algorithms, that is what I’d be — working on.” – John Preskill 2004 — Preskill
4. When I was a Grad Student… — Quantum Algorithms — Factoring, discrete log [Shor 94] — Unstructured search [Grover 96]
5. State of the Art — Quantum Algorithms — Factoring, discrete log [Shor 94] — Unstructured search [Grover 96]
6. The Problem — Problem: Fix a group G (known) and a subgroup — H• G (unknown). Given query access to a function — f : G → S that is constant and distinct on left cosets
7. Groups — Set of elements with a binary operation “• ” — Binary operation satisfies: — 1. Closure: g1• g2 is in the set
8. Left Cosets — Subset of group which is itself a group. — Subgroups — Let H be a subgroup of G.
9. Anatomy of Our Problem — Problem: Fix a group G (known) and a subgroup — H• G (unknown). Given query access to a function — f : G → S that is constant and distinct on left cosets
10. The Hidden Subgroup Saga — Why is everyone so interested in the HSP? — 2. An efficient algorithm for the HSP for the — symmetric group would given an efficient
11. The Hidden Subgroup Success — Abelian groups [Shor 94; Kitaev 95] — [Püschel, Rötteler, Beth 98] — Normal subgroups [Hallgren, Russell, Ta-Shma 00]
12. Standard Query Model — Uf — constant and distinct on different left cosets of H: — hidden subgroup state
13. HSP as State Distinction — Given: — Determine: — Maximize: probability of successfully identifying H
14. Query Complexity of HSP — Given: k=O(log(N)) standard queries to HSP — Exists: an inefficient quantum algorithm which — solves any HSP.
15. Holevo’s Condition — Given: — with probability pi — Outcome:
16. Pretty Good — with equal probabilities — Given: — Observation:
17. Hidden Reflection — Given: — with equal a priori probability — Dihedral HSP
18. Must Work Hard — Theorem: [Bacon, Childs, van Dam 05] — Determining the hidden reflection requires — O(log(N)) copies of the hidden subgroup states.
19. POE — A Strange Lock — Rotation: — Reflection:
20. Dihedral HSP — Dihedral group — G = DN: symmetry group of a — N-sided regular polygon.
21. Dihedral HSP Facts — Efficient algorithm — for DHSP — Efficient algorithm for
22. One Copy — One copy of the Hidden Subgroup state: — Basis change: — Punishment
23. Multi Copy — number of subsets of x which sum to t — More Punishment
24. Stop The — Punishment — Optimal PGM — Note: Entangled measurement over k copies
25. Success Probability — Probability of correctly guessing reflection: — number of subsets of x which sum to t — p is related to a phase transition
26. Subset Sum Problem — Given: — k integers from — i.e. , and a target
27. The Subset Sum Landscape — Given: — k integers from — i.e. , and a target
28. Success Probability — Probability of correctly guessing reflection: — number of subsets of x which sum to t — k dimensional vector of elements of
29. Must Work Hard — Theorem: [Bacon, Childs, van Dam 05] — Determining the hidden reflection requires — O(log(N)) copies of the hidden subgroup states.
30. Heisenberg Group — Semidirect product group — Elements of the group: — Multiplication rule:
31. Heisenberg HSP — We can restrict to subgroups of the form — General version of theorem from [Etinger, Hoyer 98]
32. Heisenberg HS State — Restricted subgroups: — Random coset states: — Coset labels:
33. Optimal Measumrent — The optimal measurement for k copies is again the — pretty good measurement. — For one copy, the probability of successfully
34. HS States — Perform the QFT over to the first two registers: — Measure these two registers:
35. HS States — Two copies: — Compute v and w:
36. Uncompute — If we could erase the b1,b2 values: — Then a QFT over would find d1 and d2. — Remember v and w are a function of b1 and b2.
37. Solving Equations — Compute v and w: — For fixed x1,x2,y1,y2 let be the set of b1,b2 — solutions to these equations.
38. Solving Equations — Easier to think about the inverse (do it unitarily): — i.e. given v and w, transform to superposition over — solutions to the equations
39. Solving Equations — Assuming y1,y2,y1+y2 do not equal 0 (prob O(1/p)), — then — solutions have
40. Solving Equations — Focus on when there are two solutions. — We can use standard finite arithmetic to find these — solutions. Use to create labeled superposition of
41. Heisenberg HSP Solved — This allows us to perform: — Which has a O(1/2) fidelity squared with the — state we desire.
42. Extensions — This algorithm can be extended to an efficient — quantum algorithm for all — Also, certain metacyclic groups
43. Open — The PGM is not optimal for all groups, what is the — optimal multicopy measurement? — Other groups for which this technique works?
44. Conclusion — Subgroups for which multicopy queries are — necessary. — PGM is often optimal for distinguishing HS states.
