# The Symmetry Conjecture in Quantum Algorithms
- **Event / Venue:** UNM Physics Seminar 2009 (2009)
- **Format:** `KEY` (`seminar.key.zip`)
- **Slides:** 92

## Extracted Slide Text

1. The Symmetry Conjecture in Quantum Algorithms | Dave Bacon | University of Washington
2. Quantum Algorithms | 18819881292060796383869723946165043 | 98071635633794173827007633564229888 | 59715234665485319060606504743045317
3. A Golden Era | Email I received from Wim van Dam about FOCS 2006: | Leslie Valiant in his great talk on 'accidental algorithms': "We have all these complexity classes, and we don't know at all if they are different... It would be a nightmar
4. The State of Quantum Algorithms | Grover-Type | Shor-Type | Factoring, Discrete Logarithm
5. On Quantum Algorithms | Ronald de Wolf (CWI) | From a 2003 review of three quantum computing books: | “Finally, to all those currently working on yet another book on quantum computing: what this field needs most is more algorithms, not more
6. The Power Question | Where does the power of quantum algorithms come from? | Peter Shor’s | brain!
7. The Real Question: | Where does the power of quantum algorithms come from? | Where does the power of classical algorithms come from? | Why are quantum algorithms sometimes exponentially more efficient than classical algorithms?
8. The Symmetry Conjecture | Quantum computers exponentially outperform classical computers because groups admit unitary representations
9. An Example | Two probability distributions p and q over {1,2,..2N} | Both are evenly distributed over subset size N | p equals q
10. An Example | Two amplitude distributions p and q over {1,2,..2N} | Both are evenly distributed over subset size N | p equals q
11. Swap Test | Two amplitude distributions p and q over {1,2,..2N} | Both are evenly distributed over subset size N | p equals q
12. Symmetry | Under unitary basis change this becomes | Classical probabilistic transforms are stochastic and | cannot perform this basis change.
13. Cognitive Dissonance | Parts of exponentially faster quantum algorithms which don’t seem to be exploiting symmetry.
14. Simon’s Problem | Given: A function with n bit strings as input and one bit as | output | Promise: The function is guaranteed to satisfy
15. Classical Simon’s Problem | query pairs | If we find such that then | Querying the function m times….
16. Quantum Simon’s Problem | n qubits
17. Quantum Simon’s Problem | For random uniformly distributed | Symmetry: | Symmetry • Simultaneously diagonalize symmetry operators
18. Quantum Simon’s Problem | n qubits
19. Quantum Simon’s Problem | Measuring this state, uniformly distributed random such that | Multiple runs: | random
20. Moral | Symmetries | Diagonalize with respect to symmetry | Quantum algorithm
21. Representation Theory in 1 Slide | Group | Unitary representation of group | Irreducible representations of a group (irreps):
22. Simon’s Problem Redux | Group | addition bitwise mod 2 | Representation of group
23. More Simon’s Problem Redux | random | uniform | are irrep labels
24. Symmetry Interpretation | Clebsch-Gordan transform: | So the “addition” of Gaussian elimination in Simon’s algorithm | can be interpreted as a Clebsch-Gordan transform….
25. The Second Basis Change We Learn In Quantum Mechanics: | Singlet: | Triplet: | Clebsch-Gordan Transform
26. Collective Unitaries | Symmetry Under n Collective Unitary Rotations
27. Singlet: | Triplet: | The Symmetric Group | Transform Under
28. Quantum Schur Transform | n d-dimensional | systems | (n qudits)
29. Uses of Schur | Young diagram | What does this remind you of? | like probabilities like the spectrum of a density operator
30. The Plethora of Uses of Schur | Optimal spectrum estimation | [M. Keyl and R. F. Werner. Phys. Rev. A, 2001] | Universal distortion-free entanglement concentration
31. But Efficient? | QFT | Schur | Who would need to efficiently calculate Clebsch-Gordan
32. Efficient Schur | [D. Bacon, I.L. Chuang, A. Harrow, Phys. Rev. Lett. 2006] | [D. Bacon, I.L. Chuang, A. Harrow, SODA 2007] | Schur transform to accuracy time
33. The Plethora of Uses of Schur | Optimal spectrum estimation | [M. Keyl and R. F. Werner. Phys. Rev. A, 2001] | Universal distortion-free entanglement concentration
34. But Quantum Algorithms?
35. The Hidden Subgroup Problem | Setup: Fix a group (known) and a subgroup (unknown). Given query access to a function f : → S that is constant and distinct on left (right) cosets of in . We say that f hides . | Problem: Find a generating set 
36. “The quantum measurement problem refers to a set of people.” | - Hideo Mabuchi | “The hidden subgroup problem refers to a subgroup of people.” | Hidden Subgroup Disease
37. Why the Fuss? | efficient algorithm for HSP | over (or ) | efficient algorithm for the
38. Graph Isomorphism | Problem: Is there a 1-to-1 mapping from the vertices to the | vertices such that the edges are respected, ? | Mapping to the HSP:
39. Standard Query Model | U f | Oracle: | Query in equal superposition over group elements
40. You Down With Symmetry? | hidden subgroup state | Symmetry under left regular representation: | Fourier transform over finite group
41. Multicopy | Can we make a measurement on | copies and | learn the subgroup?
42. You Down With Symmetry? | hidden subgroup state | Symmetry under left regular representation: | Symmetry of two copies?
43. Heisenberg Group | Semidirect product group | Elements of the group: | Multiplication rule:
44. Multicopy Success! | [D. Bacon, A.M. Childs, and W. van Dam FOCS 2005] | Efficient algorithm for the Heisenberg HSP: | PGM/optimal measurement approach:
45. Clebsch-Gordan Transform | To The Rescue? | does not have a Clebsch-Gordan related symmetry | Problem:
46. Graph Isomorphism | Problem: Is there a 1-to-1 mapping from the vertices to the | vertices such that the edges are respected, ? | Mapping to the HSP:
47. Conjugate Subgroups | Two subgroups, and , are conjugate if there exists an | element of the group such that | This is an equivalence relation among the subgroups of
48. Hidden Subgroup Conjugacy Problem | Setup: Fix a group (known) and a subgroup (unknown). Given query access to a function f : → S that is constant and distinct on left (right) cosets of in . We say that f hides . | Problem: identify the con
49. Symmetries of HSCP States | Hidden subgroup conjugate state | Hidden subgroup conjugate states | In context of optimal measurement method (PGM)
50. Symmetries of HSCP States | Clebsch-Gordan transform for the regular representation of | finite groups: | What is the extra symmetry of the multiple HSCP states?
51. Relationships | How do the hidden subgroup problem (HSP) and the | hidden subgroup conjugacy problem (HSCP) differ? | 1. If group is abelian, HSCP=HSP
52. General Circuit
53. [Bacon, arXiv:quant-ph/0612107] | Heisenberg HSCP and HSP | Heisenberg HSCP ⇒ Heisenberg HSP | Conjugate subgroups are all normal subgroups
54. [Bacon, arXiv:quant-ph/0612107] | Heisenberg HSCP, CG Way | i labels set of conjugate subgroups
55. [Bacon, arXiv:quant-ph/0612107] | Heisenberg HSCP, CG Way | i can be found by performing (which can be done with high prob) | and performing a QFT
56. Krovi and Roetteler: Weyl-Heisenberg Groups | Heisenberg HSP Lesson | Clebsch-Gordan transform can be used to help | solve HSPs
57. Fin | Clebsch-Gordan transform reveals essential symmetry of efficiently solvable nonabelian hidden subgroup problems….Can they lead us further, the $10 9 question | funded by | ARO
58. You Down With Symmetry? | And now, I will, for symmetries sake give the entire talk in reverse.
59. QW | funded by | Graduate Students | Gregory Crosswhite (Physics)
60. Heisenberg HS State | Restricted subgroups: | Random coset states: | Coset labels:
61. HS States | Perform the QFT over to the first two registers: | Measure these two registers:
62. HS States | Two copies: | Compute v and w:
63. Uncompute | If we could erase the b 1 ,b 2 values: | Then a QFT over would find d 1 and d 2 . | Remember v and w are a function of b 1 and b 2 .
64. Solving Equations | Compute v and w: | For fixed x 1 ,x 2 ,y 1 ,y 2 let be the set of b 1 ,b 2 | solutions to these equations.
65. Solving Equations | Easier to think about the inverse (do it unitarily): | i.e. given v and w, transform to superposition over | solutions to the equations
66. Solving Equations | Assuming y 1 ,y 2 ,y 1 +y 2 do not equal 0 (prob O(1/p)), | then | solutions have
67. Solving Equations | Focus on when there are two solutions. | We can use standard finite arithmetic to find these | solutions. Use to create labeled superposition of
68. Heisenberg HSP Solved | This allows us to perform: | Which has a O(1/2) fidelity squared with the | state we desire.
