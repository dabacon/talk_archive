# Recent Progress In Quantum Algorithms
- **Event / Venue:** aqis07 (2007)
- **Format:** `PPT` (`aqis07.ppt`)
- **Slides:** 49

## Extracted Slide Text

1. Dave Bacon — University of Washington — AQIS07 [Kyoto, Japan, September 2007]
2. The Goal of This Talk — 80s-early 90s: foundational work — 1994: Shor’s algorithm — 1996: Grover’s algorithm
3. HELP WANTED Quantum programmer. Only skill necessary is ability to type in large RSA keys. Salary commiserates with expe — HELP WANTED Real estate agent. Best market since bubble popped in 07. Join a dedicated — HE — ne
4. Graph Isomorphism — Are these two graphs isomorphic? — Graph isomorphism is in NP• coAM — No known polynomial time algorithm
5. Adjacency matrix of G1• G2 with edges permuted by • — Graph Isomorphism — [For simplicity, assume graphs rigid] — If isomorphic, exists a subgroup {e,• } which leaves function constant
6. The Hidden Subgroup Problem — Setup: Fix a group (known) and a subgroup (unknown). Given query access to a function f : → S that is constant and distinct on left (right) cosets of in . We say that f hides . — Problem: Find a generating set 
7. Why the Fuss? — efficient algorithm for HSP — over (or ) — efficient algorithm for the
8. A Strawman — BQP, PP, NP, PostBQP, MIT…. — What makes you think the hidden subgroup — approach to solving graph isomorphism is the
9. Philosonomicon — What is the difference between classical and quantum computing? — [The fair comparison is with probabilistic classical computing] — Configurations:
10. Some Outrageous Statements — Classical Reversible Deterministic Computation: — Is nothing more than the study of the properties — of certain generating sets of a very large
11. Group Representation Theory — Group: set of elements with binary multiplication operation — (satisfying closure, associativity, identity and inverse) — For finite and compact groups we can decompose representation
12. Comparison of Symmetry — Classically, suppose we have a probability distribution with — What can you do? — Quantum mechanically, suppose we have a density matrix with
13. The Hidden Subgroup Problem — Setup: Fix a group (known) and a subgroup (unknown). Given query access to a function f : → S that is constant and distinct on left (right) cosets of in . We say that f hides . — Problem: Find a generating set 
14. Start Simple — Two possible hidden subgroups — or — 50%
15. Symmetry — I give you a symmetric probability distribution — how does this help you? — I give you a symmetric quantum density matrix
16. One More Outrageous Statements — The Symmetry Speedup Hypothesis of Quantum Computing — Every exponential quantum speedup in quantum algorithms — is fundamentally the result of exploiting symmetries.
17. Successes — abelian groups — almost abelian groups — near Hamiltonian groups
18. Standard Query Model — Uf — Oracle: — Query in equal superposition over group elements
19. HSP Symmetries — Symmetry — left regular representation: — Transform/Consequence
20. HSP Multiple Registers — symmetric group — Schur Transform — Given m copies of HSP can we perform some measurement on
21. Hidden Subgroup Conjugacy Problem — Setup: Fix a group (known) and a subgroup (unknown). Given query access to a function f : → S that is constant and distinct on left (right) cosets of in . We say that f hides . — Problem: identify the con
22. Why This Approach? — HSCP = HSP for many “solved” cases — Abelian, Normal subgroups, more (this talk) — HSCP possesses more symmetry than HSP
23. Multicopy HSP and HSCP — Single query — Multiple queries — HSP
24. HSCP Symmetries — State — Symmetry — right regular representation
25. Clebsch-Gordan Transform — Clebsch-Gordan series — mulitplicity — If all then we say “multiplicity-free”
26. General HSCP Circuit — multiplicity — space
27. …Is the CG transform really — useful for HSP algorithms?
28. Simon’s Problem — Simon: Given a function f:{0,1}^n →{0,1}^n such that f(x)=f(x• y), y• 0 — Problem: Find y• {0,1}^n by querying f — Simon’s algorithm:
29. Simon’s Problem Redux — Simon: Hidden subgroup problem over with subgroups order two — QFT on is nothing more than the Hadamard transform — But what is Gaussian Elimination?
30. …Is the CG transform really — useful for non-abelian — HSP algorithms?
31. Heisenberg Group — Semidirect product group: — Group of upper triangular matrices: — (Related to theory of discrete radar)
32. HSP and HSCP — Heisenberg group — Solving HSCP ⇒ Identifying • of ⇒ normal HS algorithm — Result: Heisenberg HSP = Heisenberg HSCP
33. Heisenberg CG Series — p2 1D irreps — p (p-1)D irreps — Clebsch-Gordan series:
34. [Bacon, arXiv:quant-ph/0612107] — Heisenberg HSCP, CG Way — i labels set of conjugate subgroups
35. Heisenberg HSCP, CG Way — i can be found by performing — and performing a QFT — Clebsch-Gordan transform over Heisenberg group is related
36. PGM/optimal measurement approach [Bacon,Childs, van Dam 05] — Heisenberg HSP Comparison — Two copy state: — CG symmetry reduces this to
37. Nonabelian Simon’s Problem — Generalize Simon’s problem to where is a fixed size — nonabelian group with an order two subgroup. — Alagic, Moore, Russell (2006) found a subexponential, but still
38. A New Quantum HSP Algorithm — Simon’s problem over the n-fold product of the — dihedral group of order eight
39. Dihedral Group of Order Eight — Group of symmetries of the square: — Rotation ≡ s, s4=e — Reflection ≡ r, r2=e and rsr=s-1
40. A Warm-up — HSCP on D4, distinguish parity of k, {e,rsk} — Partial QFT + measurement yields random — Note that if a Hadamard will reveal parity of l
41. A Warm-up, Part II — Three copies, — CNOT+SWAP, cascaded — Now there is a multiplicity. Example:
42. A New Quantum HSP Algorithm — Simon’s problem over the n-fold product of the — dihedral group of order eight — Multiplicity space algorithm for to find subgroups:
43. Sketch of Algorithm — Random along with state — Run this m=n+2 times — parity strings of
44. Fin — A new quantum algorithm or hidden — symmetries of multiple squares — The quantum algorithm for the Heisenberg HSP can be
45. Hidden Polynomial Function Graph — Problem — Given: — Multivariate polynomial
46. Hidden Parabolas — Constant on “parabola”s — Identify: Coefficients — (2 and 4, in example)
47. Quantum Hidden Parabolas — Query function over all inputs — Measure and throw away function register: — QFT second register, measure and throw away
48. Quantum Hidden Parabolas — Two runs: — Solve equations (which have p2 solutions with high probability) — for allowing state to be
49. Hidden Polynomial Function Graph — Problem — Result: — Efficient quantum algorithm for HPFGP for
