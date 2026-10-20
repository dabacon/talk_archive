# Quantifying Time Travel
- **Event / Venue:** newdirections2011 (2011)
- **Format:** `KEY` (`timetravelfoundations.key.zip`)
- **Slides:** 52

## Extracted Slide Text

1. Quantifying Time Travel | Dave Bacon | Department of Computer Science & Engineering | Department of Physics
2. At Christmas Time I | Do Foundations
3. Physics => Computer Science | Today I will act like a theoretical computer scientist and try to think simply about “models of computing” or “information processing protocols.” If you are a physicist please cover your ears if it gets to be t
4. Theoretical CS | "If you think this Universe is bad, you should see some of the others." | — Philip K. Dick
5. Turing Machine | Machine with finite set of states | TM | time
6. Non-deterministic Turing Machine | time | Transition function: Given symbol under machine + state, transition to one of a set of (write symbol, update state, and move) | accept when one of the branches is in an
7. Baby Bathwater | “Time is nature's way of keeping everything from happening at once. | Space is what prevents everything from happening to me.” | - attributed to John Wheeler
8. Causal Structure | Time | Space | d = (a⊕c)b
9. Bell’s Theorem | There is no local hidden variable | theory that can explain the | correlations predicted by quantum
10. What If... | ....every subsystem could interact non-locally with every other subsystem in the universe? | MEGA NONLOCALITY
11. New Mystery | Why do A and B exhibit correlations, but A and E (B and E) do not?
12. One Answer | Correlations can exists between A and B because | they interacted in the past. | A and B must be able to remember they have
13. Identity = Shared Key? | exchange some information that allows A and B to identify each other | Whatever information E transmits to the rest of the universe, it shouldn’t destroy quantum correlations between A and B
14. Singlet Experiment | two outcome | projective measurements
15. Singlet Protocol | 1. Alice and Bob share two unit vectors, and , | uniformly distributed on the sphere | 2. Alice outputs
16. Pictorially
17. Proof Sketch | Both parties outputs change sign under | thus | Plus an ugly calculation
18. Babe Ruth | (a) [K. H. Schatten, PRA 48 103 (1993)] | (b) [N. Gisin, B. Gisin, Phys. Lett. A 260, 323 (1999)]
19. LHV + Classical Communication | Quantify the amount of classical communication needed to augment a local hidden variable theory in order to reproduce quantum theory | [T. Maudlin 1992], [Brassard, Cleve, Tapp 1999], [Steiner 2000] | (Quanti
20. Open Question | Is it always possible to augment a local hidden | variable theory with an amount of communication | bounded by the dimension of the quantum system
21. Progress | Bipartite quantum state | subsystems of dimension d | d x d observables with eigenvalues +1, -1
22. Progress | Simulate correlation: | [Toner and Regev 2009] | This experiment can be simulated with local hidden variables plus two bits of communication (indpendent of d).
23. Embarrassment | n=d2
24. Open Question | Is it always possible to augment a local hidden | variable theory with an amount of communication | bounded by the dimension of the quantum system
25. A Problem | exchange some information that allows A and B to identify each other | Whatever information E transmits to the rest of the universe, it shouldn’t destroy quantum correlations between A and B
26. Singlet Protocol + Eve | 1. Alice and Bob share two unit vectors, and , | uniformly distributed on the sphere | 2. Alice outputs
27. A Problem | exchange some information that allows A and B to identify each other | Whatever information E transmits to the rest of the universe, it shouldn’t destroy quantum correlations between A and B | A and B must be able to “authentica
28. Is There a `Better’ Solution? | “Transactional interpretation?” | Closed time like curves? | NEXT: A Complexity Theory approach to thinking
29. Closed Timelike Curves | Normally theoretical physicists ask, “What are the laws of physics?” and/or “What do those laws predict about the Universe?” … We ask, instead, “What constraints do the laws of physics place on the activities of an 
30. Closed Timelike Curves | Use stable wormhole plus | time dilation to make a time machine | but is this
31. Closed Timelike Curves | space | time | V+
32. Qubits in Spacetime | space | time | initial conditions specifying
33. Qubits in Spacetime | space | time | Allow CTC qubits to interact with chronology respecting qubits
34. Consistency | space | time | to (Quantum Theory) add (Consistency) in presence of (CTCs)
35. Consistency? | consistency: | input-ouput: | non-linear in
36. Example | Consistency: | (single consistent CTC state) | Output is unambiguous:
37. Example | Consistency: | Output is unambiguous if | Output is ambiguous if
38. Ambiguity | Deutsch’s proposed solution [Deutsch 1991]: | Another proposed solution [Bacon 2004]: ambiguity could be resolved by initial conditions of CTC generating region. | If one considers open quantum systems one can argue for unique f
39. Blowing Up Probabilities | Output is unambiguous if | By repeating n times we can distinguish | and
40. Back to CS Land | What is the computational power | of qubits with CTCs?
41. Cook-Levin Theorem | Theorem: the Boolean Satisfiability Problem | is NP-complete | Boolean formula (CNF):
42. Cook-Levin Theorem | Theorem: the Boolean Satisfiability Problem | is NP-complete | Boolean formula (CNF):
43. Power of CTCs | Then repeatedly apply: | Can solve NP-complete problems in polynomial time | [Brun 2002, Bacon 2003]
44. Power of Deutsch CTCs [2003] | NP | BQPCTC | BQP
45. Anything You Can Do | Replace quantum by classical | probabilistic computation | density matrix => probability distribution,
46. Power of CTCs [2003] | NP | BPPCTC | BPP
47. Power of Classical CTCs | NP | BQP | BPP
48. Is BQP in BPPCTC | Translation: is there an “efficient” simulation of quantum theory using classical computation and closed timelike curves? | Breakthrough | BPPCTC = BQPCTC = PSPACE
49. Power of Classical CTCs | NP | BQP | BPP
50. Is There a `Better’ Solution? | There exists an efficient way to simulate quantum theory using classical probabilistic evolutions plus closed timelike curves | But can we do this in a way that respects the interaction network of the systems
51. Breakthrough | Trouble? | Non linear theories lead to all sorts of craziness (faster than light transmission) and most interesting the linearity trap [Bennett et al 2009] | but
52. Breakthrough | Conclusion? | Classical local hidden variables + 1 bit can simulate projective measurements on singlet | Can local hidden variables + c bits simulate measurements on d dimensional systems with c=O(d)?
