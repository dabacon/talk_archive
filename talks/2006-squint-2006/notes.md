# New Algorithms for the Nonabelian Hidden Subgroup Problem
- **Event / Venue:** SQUINT 2006 (2006)
- **Format:** `PPT` (`newalgo.ppt`)
- **Slides:** 31

## Extracted Slide Text

1. New Algorithms for the Nonabelian Hidden Subgroup Problem — g1H — g2H — g3H
2. Looking For New Algorithms — 1996:
3. Hidden Subgroup Problem
4. quant-ph/0501044 “Optimal measurements for the dihedral hidden subgroup problem,” Bacon, Childs, van Dam — quant-ph/0501056 “The Symmetric Group Defies Strong Fourier Sampling: Part I”, Moore, Russell, Schulman — quant-ph/0501177 “The Symme
5. quant-ph/0501044 “Optimal measurements for the dihedral hidden subgroup problem,” Bacon, Childs, van Dam — quant-ph/0501056 “The Symmetric Group Defies Strong Fourier Sampling: Part I”, Moore, Russell, Schulman — quant-ph/0501177 “The Symme
6. The Problem — Problem: Fix a group G (known) and a subgroup — H• G (unknown). Given query access to a function — f : G → S that is constant and distinct on left cosets
7. Why We Care — Graph Isomorphism — Unique k-Shortest Vector — In a Lattice
8. Standard Query Model — Uf — constant and distinct on different left cosets of H: — Hidden Subgroup State
9. Given: — Single Copy — Copies — Given:
10. quant-ph/0501056 “The Symmetric Group Defies Strong Fourier Sampling: Part I”, Moore, Russell, Schulman — quant-ph/0501177 “The Symmetric Group Defies Strong Fourier Sampling: Part II,” Moore, Russell — quant-ph/0510185 “On the quantum hard
11. Nattering Nabobs — of Negativism — “Our result can be viewed as a negative result because highly entangled measurements seem hard to implement in general.” — - Hallgren, Roetteler, Sen
12. HSP as State Distinction — Given: — Determine: — Maximize: probability of successfully identifying H
13. HSP as State Distinction — Given: — Determine: — Maximize: probability of successfully identifying H
14. Holevo’s Condition — Given: — with probability pi — Outcome:
15. Pretty Good — with equal probabilities — Given: — Observation:
16. Heisenberg Group — Margrethe Bohr to Heisenberg (from the play “Copenhagen”) — “Your talent is for ski-ing too fast for anyone to see where — you are. For always being in more than one position at a time,
17. Heisenberg Group — Semidirect product group — Elements of the group: — Multiplication rule:
18. Heisenberg HSP — We can restrict to subgroups of the form — General version of theorem from [Ettinger, Hoyer 98]
19. Heisenberg HS State — Restricted subgroups: — Random coset states: — Coset labels:
20. Optimal Measumrent — The optimal measurement for k copies is again the — pretty good measurement. — For one copy, the probability of successfully
21. HS States — Perform the QFT over to the first two registers: — Measure these two registers:
22. HS States — Two copies: — Compute v and w:
23. Uncompute — If we could erase the b1,b2 values: — Then a QFT over would find d1 and d2. — Remember v and w are a function of b1 and b2.
24. Solving Equations — Compute v and w: — For fixed x1,x2,y1,y2 let be the set of b1,b2 — solutions to these equations.
25. Solving Equations — Easier to think about the inverse (do it unitarily): — i.e. given v and w, transform to superposition over — solutions to the equations
26. Solving Equations — Assuming y1,y2,y1+y2 do not equal 0 (prob O(1/p)), — then — solutions have
27. Solving Equations — Focus on when there are two solutions. — We can use standard finite arithmetic to find these — solutions. Use to create labeled superposition of
28. Heisenberg HSP Solved — This allows us to perform: — Which has a O(1/2) fidelity squared with the — state we desire.
29. Efficient Quantum Circuit
30. (Non-Homework) Extensions — This algorithm can be extended to an efficient — quantum algorithm for all — Also, certain metacyclic groups
31. Conclusion — PGM is often optimal for distinguishing HS states — and can lead to new efficient algorithms. — Efficient algorithm for Heisenberg, generalizations.
