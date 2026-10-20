# Graph Isomorphism Beyond the Hidden Subgroup Problem
- **Event / Venue:** MIT2011 (2011)
- **Format:** `KEY` (`GI.key.zip`)
- **Slides:** 48

## Extracted Slide Text

1. Graph Isomorphism Beyond the Hidden Subgroup Problem | Dave Bacon | University of Washington
2. Happy Star Wars Day!
3. Namespace Overload | Institute for Extreme Quantum Computing | Institute for Extreme Quantum Information | Institute for Extreme Quantum Information Science
4. Graph Isomorphism | GI: Given two graphs G1=(V1,E1) and G2=(V2,E2), | does there exist a bijection, f, from vertex set V1 to vertex set V2, such that (u,v) is in E1 iff (f(u),f(v)) is in E2? | f ?
5. Goldilocks | Yet no known polynomial time algorithm (neither | classical nor quantum) for GI. | not Goldilocks
6. Hidden Subgroup Problem | Given: a group G, a finite set S, and a function f | from G to S that is constant and distinct on left cosets of an unknown subgroup H. | Determine: Set of generators for H.
7. Hidden Subversive Problem | couriers | Solvable in constant time
8. Hidden Subgroup Approach to Graph Isomorphism | Group: | (or ) | Function:
9. Hidden Subgroup Obstacles | Hidden subgroup state: | [Hallgren, Moore, Roettler, Russell, Sen 2006]: | Quantum algorithm that uses hidden subgroup states must perform measurement that are joint across O(n log n) hidden subgroup states
10. Symmetries and GI | Abelian HSP is good for finding hidden subgroups of large (nearly Abelian) groups (=> Shor’s algorithm) | GI is efficiently solvable when eigenvalues of the adjacency matrix are of bounded degeneracy | Automorphism group
11. Large Object | Factoring is to Period Finding as | Graph Isomorphism is to ? | ? perhaps not = HSP
12. A Story - The Physicist | Terry Rudolph | The eigenvalues (spectrum) of an adjacency matrix is a graph invariant. | Eigenvalues are not enough to distinguish all non-isomorphic graphs
13. A Story - The Physicist | Terry Rudolph | One quantum particle: | Two quantum particles:
14. A Story - The Physicist | Terry Rudolph | Two quantum hard-core bosons: | [arXiv:quant-ph/0206068]
15. A Story - The Physicist | Terry Rudolph | Strongly regular graphs, however | are not distinguished by two hard-core bosons spectra. Three hard-core bosons spectra did seem to work....
16. A Story - Some Blogger | August 15th, 2006 | Quantum computers are not known to not solve NP-complete problems in polynomial time
17. A Story - The Physicist | Terry Rudolph
18. A Story - The Mathematician | Greg | Kuperberg
19. A Story - Weisfeiler-Lehman | [32,23] | [3,23,1]
20. A Story - Weisfeiler-Lehman | [32,23] | 4=[3,23] | 3=[32,22]
21. A Story - k-dim WL | Boris | Weisfeiler | Roughly corresponds to considering subsets of size k, and running a refining algorithm.
22. A Story - Cai, Furer, Immerman 1992 | Jin-Yi Cai | Martin Furer | Neil Immerman
23. A Story - The Mathematician | Greg | Kuperberg
24. A Story - The Mathematician | k hard-core bosons don’t solve graph isomorphism for same reason k-dim WL algorithm fails! | Babe | Ruth
25. New (Quantum) Approaches to Graph Isomorphism | Cellular algebra is a subalgebra of that is | Closed under conjugate transpose | Closed under Hadamard product
26. Standard Basis | Every CA has a standard basis | 1. Ri are 0/1 matrices | 2. Form a `disjoint union’ of J
27. A Tale of Two Algebras | 1. Adjacency matrix of graph => cellular algebra | 2. Permutation group => centralizer algebra of | Centralizer algebra of permutation group is a cellular algebra.
28. Dreamland | Automorphism group of graph is permutation group, | construct its centralizer (cellular algebra) | Basis of this algebra are 1-orbits and 2-orbits of automorphism group (i.e. finding this basis would allow you to solve find orbi
29. m-dim WL | ith term | Big cellular algebra: | basis
30. m-dim WL cont. | cellular algebra: | Graph isomorphism can be solved assuming you | can calculate the basis in the case of m=n.
31. A Quantum Approach | We are not afraid of objects like | Questions: | Hadamard product? (use max entangled states?)
32. An Extreme Problem | Kids don’t listen to us old dudes, work on quantum algorithms for graph isomorphism instead (statement not meant to be paradox free)
33. A Conspiracy Theory
