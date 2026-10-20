# Symmetry and Quantum Algorithms
- **Event / Venue:** UW CS Theory Seminar 2009 (2009)
- **Format:** `KEY` (`uwtheory09.key.zip`)
- **Slides:** 94

## Extracted Slide Text

1. Symmetry and Quantum Algorithms | Dave Bacon | University of Washington | Department of
2. Quantum Propaganda | I think I can safely say that nobody understands quantum mechanics. | Niels Bohr | Nobel Prize 1922
3. Hogwash | They understand it | They use it | It just defies their sensibilities
4. These Are a Few of My Favorite Norms | p-norm: | “0-norm” (not really a norm) | number of nonzero
5. Deterministic | Enforce | “Description” of n bits: | “Description” = vector with one nonzero entry
6. Probabilistic | Enforce | “Description” of n bits: | “Description” = vector whose absolute values sum
7. Quantum | Enforce | “Description” of n bits: | “Description” = vector whose absolute values squared
8. Quantum Algorithms | CS time | state | preparation
9. Physicist’s Notation | = column vector (ket) | = row vector (bra) | = inner product
10. Physicist’s Notation II | When you need to combine 1 and 2 norms, use the | density matrix: | with probability
11. Quantum Algorithms | 18819881292060796383869723946165043 | 98071635633794173827007633564229888 | 59715234665485319060606504743045317
12. Quantum Algorithms | Grover Type | Unstructured Search | [Grover 96]
13. On Quantum Algorithms | HELP WANTED Quantum programmer. Only skill necessary is ability to type in large RSA keys. Pay inversely commensurate with years since Ph.D. completed. | HELP WANTED Real estate agent. Best market since bubble popped
14. Quantum Algorithms | 01 01 00 11 00 01 10 11 | Na | N1/2
15. Quantum Algorithms | 0101101110011011 | Farhi, Goldstone, and Gutman, “A Quantum Algorithm for the Hamiltonian NAND Tree” 2007 | right going initial wave packet
16. Questions | Where does the power of quantum algorithms come from? | Where does the power of classical algorithms come from? | Why are quantum algorithms sometimes exponentially more powerful than classical computers?
17. The Symmetry “Conjecture” | Vague version 1: Quantum computers exponentially outperform classical computers because they can efficiently “exploit” symmetry | Vague version II: Permutation groups admit unitary representations which can be us
18. Example | Two probability distributions p and q over {1,2,..2N} | Both are evenly distributed over subset size N | p equals q
19. Example | Two amplitude distributions p and q over {1,2,..2N} | Both are evenly distributed over subset size N | p equals q
20. The Swap Test | SWAP | What’s this got to do with symmetry?
21. Symmetry | Under unitary basis change this becomes | Classical probabilistic transforms are stochastic and | cannot perform this basis change.
22. Cognitive Dissonance | Algorithms that offer exponential speedups but don’t seem to exploit symmetry
23. Simon’s Problem | Given: A function with n bit strings as input and one bit as | output | Promise: The function is guaranteed to satisfy
24. Classical Simon’s Problem | query pairs | If we find such that then | Querying the function m times….
25. Quantum Simon’s Problem | n qubits
26. Quantum Simon’s Problem | For random uniformly distributed | Symmetry: | Symmetry • Simultaneously diagonalize symmetry operators
27. Quantum Simon’s Problem | n qubits
28. Quantum Simon’s Problem | Measuring this state, uniformly distributed random such that | Multiple runs: | random
29. Moral | Symmetries | Diagonalize with respect to symmetry | Quantum algorithm
30. Representation Theory in 1 Slide | Group | Unitary representation of group | Irreducible representations of a group (irreps):
31. Simon’s Problem Redux | Group | addition bitwise mod 2 | Representation of group
32. More Simon’s Problem Redux | random | uniform | are irrep labels
33. Symmetry Interpretation | Clebsch-Gordan transform: | So the “addition” of Gaussian elimination in Simon’s algorithm | can be interpreted as a Clebsch-Gordan transform….
34. The Second Basis Change Learned In Quantum Mechanics: | Singlet: | Triplet: | Clebsch-Gordan Transform
35. Collective Unitaries | Symmetry Under n Collective Unitary Rotations
36. Singlet: | Triplet: | The Symmetric Group | Transform Under
37. Quantum Schur Transform | n d-dimensional | systems | (n qudits)
38. The Plethora of Uses of Schur | Optimal spectrum estimation | [M. Keyl and R. F. Werner. Phys. Rev. A, 2001] | Universal distortion-free entanglement concentration
39. But Efficient? | QFT | Schur | Who would need to efficiently calculate Clebsch-Gordan
40. Efficient Schur | [D. Bacon, I.L. Chuang, A. Harrow, Phys. Rev. Lett. 2006] | [D. Bacon, I.L. Chuang, A. Harrow, SODA 2007] | Schur transform to accuracy time
41. The Plethora of Uses of Schur | Optimal spectrum estimation | [M. Keyl and R. F. Werner. Phys. Rev. A, 2001] | Universal distortion-free entanglement concentration
42. But Quantum Algorithms?
43. The Hidden Subgroup Problem | Setup: Fix a group (known) and a subgroup (unknown). Given query access to a function f : → S that is constant and distinct on left (right) cosets of in . We say that f hides . | Problem: Find a generating set 
44. Why the Fuss? | efficient algorithm for HSP | over (or ) | efficient algorithm for the
45. Graph Isomorphism | Problem: Is there a 1-to-1 mapping from the vertices to the | vertices such that the edges are respected, ? | Mapping to the HSP:
46. Standard Query Model | U f | Oracle: | Query in equal superposition over group elements
47. You Down With Symmetry? | hidden subgroup state | Symmetry under left regular representation: | Fourier transform over finite group
48. Multicopy | Can we make a measurement on | copies and | learn the subgroup?
49. You Down With Symmetry? | hidden subgroup state | Symmetry under left regular representation: | Symmetry of two copies?
50. Heisenberg Group | Semidirect product group | Elements of the group: | Multiplication rule:
51. Multicopy Success! | [D. Bacon, A.M. Childs, and W. van Dam FOCS 2005] | Efficient algorithm for the Heisenberg HSP: | PGM/optimal measurement approach:
52. Clebsch-Gordan Transform | To The Rescue? | does not have a Clebsch-Gordan related symmetry | Problem:
53. Conjugate Subgroups | Two subgroups, and , are conjugate if there exists an | element of the group such that | This is an equivalence relation among the subgroups of
54. Hidden Subgroup Conjugacy Problem | Setup: Fix a group (known) and a subgroup (unknown). Given query access to a function f : → S that is constant and distinct on left (right) cosets of in . We say that f hides . | Problem: identify the con
55. Symmetries of HSCP States | Hidden subgroup conjugate state | Hidden subgroup conjugate states | In context of optimal measurement method (PGM)
56. Symmetries of HSCP States | Clebsch-Gordan transform for the regular representation of | finite groups: | What is the extra symmetry of the multiple HSCP states?
57. Relationships | How do the hidden subgroup problem (HSP) and the | hidden subgroup conjugacy problem (HSCP) differ? | 1. If group is abelian, HSCP=HSP
58. General Circuit
59. [Bacon, arXiv:quant-ph/0612107] | Heisenberg HSCP and HSP | Heisenberg HSCP ⇒ Heisenberg HSP | Conjugate subgroups are all normal subgroups
60. [Bacon, arXiv:quant-ph/0612107] | Heisenberg HSCP, CG Way | i labels set of conjugate subgroups
61. [Bacon, arXiv:quant-ph/0612107] | Heisenberg HSCP, CG Way | i can be found by performing (which can be done with high prob) | and performing a QFT
62. Krovi and Roetteler: Weyl-Heisenberg Groups | Heisenberg HSP Lesson | Clebsch-Gordan transform can be used to help | solve HSPs
63. Fin | Clebsch-Gordan transform reveals essential symmetry of efficiently solvable nonabelian hidden subgroup problems….Can they lead us further, the $10 9 question | funded by | ARO
64. QW | funded by | Graduate Students | Gregory Crosswhite (Physics)
65. Uses of Schur | Young diagram | What does this remind you of? | like probabilities like the spectrum of a density operator
66. You Down With Symmetry? | And now, I will, for symmetries sake give the entire talk in reverse.
67. Graph Isomorphism | Problem: Is there a 1-to-1 mapping from the vertices to the | vertices such that the edges are respected, ? | Mapping to the HSP:
