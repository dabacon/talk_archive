# Turning Stabilizer Codes Local
- **Event / Venue:** DARPA 2011 Poster (2011)
- **Format:** `KEY` (`darpaposter.key.zip`)
- **Slides:** 24

## Extracted Slide Text

1. Turning Stabilizer Codes Local | Dave Bacon and Jonathan Shi | QW Theory Group | University of Washington
2. A QuEST | Do self-correcting quantum systems exist in realistic | settings? | realistic = local in less than three spatial dimension
3. Not Realistic (But Cool) | cube operators: | link operators: | The toric code in 4 spatial dimensions is a local self-correcting system (six body interactions)
4. Codes | 4D toric code has | a) Local check operators | b) Distance (lowest weight error that is not detectable) that scales as L2 on 4D lattice of length L
5. Definitions | c-Local code: exists a set of stabilizer generators whose weight ≤ c | weight of Pauli operator = # of operators ≠ I | I⨂X⨂X⨂Y⨂Y⨂I⨂Z⨂I has weight 5
6. Main Result | For every [[n,k,d]] stabilizer code, there exists a [[N,k,r,d]] stabilizer subsystem code, N=O(n2), whose syndrome measurements can be made using c-neighboring measurements (c constant) in D≥2 dimensions. | Translation: every 
7. Intuition of the Construction | 1. While stabilizers for a QEC code are not local, | the QEC syndrome measuring circuits can be made | local. QEC is local in space-time.
8. There’s a Code in My Wire | Vertex operators at v: | Consider stabilizer code with stabilizer generators all | vertex operator on a line except first one:
9. There’s a Code in My Wire | Add a gauge qubit (X on first qubit) | new stabilizer: | new gauge logical operators:
10. There’s a Code in My Wire | Z info | localized here | X info
11. There’s a Code in My Wire | Modulo gauge, information can be localized here | [n,1,r,1] subsystem code | Measurement based quantum computing from a subsystem code perspective
12. Subsystem Construction | Take: set of n-qubit Pauli operators | These: generate a group | This: group = r qubit Pauli group + abelian group
13. Main Idea (WAKE UP) | Circuit for measuring syndrome of a [n,k,d] stabilizer code | MBQC scheme for circuit, convert to subsystem code on N qubits | Claim: RHS code is [N,k,d] code*
14. Dictionary | circuit to labeled graph | labeled graph describes group | include: vertex operators for
15. Circuit, Circuit, Graph | Simplest stabilizer code with stabilizer | convert to | dictionary’s gate set
16. 12 Gauge Qubits | 2 Stabilizers | 1 Logical Qubit | Subsystem code
17. Modulo gauge and stabilizer group logical Z can be made weight 1, but logical X can only be made weight 2 | Stabilizers can be measured as product of low weight measurements (blue vertex operators, pink X operators) | Code Properties
18. For Syndrome Circuits | Modulo gauge operators stabilizers are (a) stabilizer of code with ancillas used to measure then (b) ancillas measurement operators | Modulo gauge/stabilizer operators, logical operators are logical operators for cod
19. An Obstacle | equiv | swap
20. An Obstacle | Need to design circuits that do not lower weight of | logicals as they are propagated back through code using gauge operators (FT-like criteria) | weight d logical
21. Main Result Redux | For every [[n,k,d]] stabilizer code, there exists a [[N,k,r,d]] stabilizer subsystem code, N=O(n2), whose syndrome measurements can be made using c-neighboring measurements (c constant) in D≥2 dimensions. | Take FT syndr
22. FAQ | Q: Why fault-tolerant syndrome measuring circuits? | - These maintain the distance of the code, actually we don’t need exactly FT circuits, but can get away with a slightly looser criteria. | Q: But aren’t fault-tolerant circuits prob
23. QuEST | What happens when we construct a Hamiltonian out of the codes we have constructed above? Self-correcting? | energy | QEC codwords
24. QW | Grads | Gregory Crosswhite (Physics) | Isaac Crosson (Physics)
