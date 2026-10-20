# CSEP 590tv: Quantum Computing
- **Event / Venue:** UW Summer 2005 Course - Lecture 1 (2005)
- **Format:** `PPT` (`Lecture1.ppt`)
- **Slides:** 96

## Extracted Slide Text

1. CSEP 590tv: Quantum Computing — Dave Bacon — June 22, 2005 — Today’s Menu
2. Administrivia — Le Syllabus — Course website: http://www.cs.washington.edu/csep590 — [power point, homework assignments, solutions]
3. Administrivia — Textbook: — “Quantum Computation and Quantum Information” — by Michael Nielsen and Isaac Chuang
4. Administrivia — Homework: due in class the week after handed out — 1. Extra day if you email me — 2. One homework, one full week extension, email me
5. Administrivia — Quick survey — Linear Algebra: ? Do You Remember It: ? — Quantum Theory: ?
6. In the Beginning… — Alan Turing — 1936- “On computable numbers, with an application to the Entscheidungsproblem” — 1947- First transistor
7. Moore’s Law — AIDS virus — Mitochondria — Eukaryotic cells
8. This Is the End? — 1. Ride the wave to atomic size computers? — 2. How do machines of atomic size operate?
9. molecular transistors — Argument by Unproven — Technology — 1. Ride the wave to atomic size computers?
10. This Is the End? — 2. How do machines of atomic size operate? — “Classical Laws” — “Quantum Laws”
11. This Is the End? — 2. How do machines of atomic size operate? — Richard Feynman — David Deutsch
12. Query Complexity — n bit strings — set — How many times do we need to query
13. The Work of Crazies — Richard — Feynman — “Can Quantum Systems be Probabilistically Simulated
14. Crazies…Still Working — Dan — Simon — 1994:
15. The Factoring Firestorm — 18819881292060796383869723946165043 — 98071635633794173827007633564229888 — 59715234665485319060606504743045317
16. This Course — Quantum theory the easy way — Quantum computers — Quantum algorithms (Shor, Grover, Adiabatic, Simulation)
17. Slander — I think I can safely say that nobody — understands quantum mechanics. — Niels Bohr
18. Quantum Theory — Electromagnetism — Weak force — Strong force
19. Our Path — Probabilistic information processing device — Quantum information processing device
20. Probabilistic Information — Processing Device — Rule 1 (State Description) — Machine has N states
21. Rule 1 — Machine has N states — 0,1,2,…,N-1 — N dimensional real vector
22. Probabilistic Information — Processing Device — Rule 1 (State Description) N states, probability vector — Rule 2 (Evolution)
23. Rule 2 — Evolution: — If we are in state 0, then with probability Aj,0 switch to state j — If we are in state 1, then with probability Aj,1 switch to state j
24. Rule 2 — these are probabilities — stochastic matrix — If in state 0 switch to state 0 with probability 0.4
25. Probabilistic Information — Processing Device — Rule 1 (State Description) N states, probability vector — Rule 2 (Evolution) N x N stochastic matrix
26. Rule 3 — Simple measurement: If we simply look at our device, then we — see the states with the probabilities given by the probability — vector.
27. Rule 3 — Measurement — k vectors — measurement outcomes
28. Rule 3 Update Rule — What is the probability vector after a measurement? — Bayes’ Rule: — B := outcome A := being in state
29. Rule 3 In Action — Two state machine with probability vector: — Three outcome measurement (k=3) — Probability of these three outcomes:
30. Probabilistic Information — Processing Device — Rule 1 (State Description) N states, probability vector — Rule 2 (Evolution) N x N stochastic matrix
31. Rule 4 — N States — M States — NM States
32. Rule 4 In Action — AB — contrast with
33. Probabilistic Information — Processing Device — Rule 1 (State Description) N states, probability vector — Rule 2 (Evolution) N x N stochastic matrix
34. Quantum Information — Processing Device — Rule 1 (State Description) N states, vector of amplitudes — Rule 2 (Evolution) N x N unitary matrix
35. Rule 1 (State Description) — Quantum Rule 1 — Rule 1 (State Description) — Machine has N states
36. Quantum Rule 1 — Machine has N states — 0,1,2,…,N-1 — N dimensional complex vector (vector of amplitudes)
37. Quantum Rule 1 — Example: 2 state device — unit vector: — inner product
38. Quantum Rule 1 — Dirac notation — “Mathematicians tend to despise Dirac notation, because it can prevent them — from making important distinctions, but physicists love it, because they are
39. Quantum Rule 1, Probabilities? — If we measure our quantum information processing machine, — (in the state basis) when our description is , then the — probability of observing state is .
40. Quantum Rule 1, Philosophy — Unfortunately, we often call the unit complex vector, the state of — The system. This is like calling the probability distribution the — State of the system and confuses our description of the system
41. Quantum Rule 1, Nomenclature — Complex unit vector — Vector of amplitudes — Wave function
42. Rule 2 (Evolution) N x N unitary matrix — The evolution in time of our description of the device is specified by an N x N unitary matrix , such that if the description of the state before the evolution is given by the wave function then the
43. Quantum Rule 2 — before evolution — after evolution — Unitary evolution:
44. Unitary Matrix? — Unitary N x N matrix: an invertible N x N complex matrix — whose inverse is equal to it’s conjugate transpose. — Invertible: there exists an inverse of U, such that
45. Quantum Rule 2, Example — Conjugate: — Conjugate — transpose:
46. Properties of Unitary Matrices — row vectors — are orthonormal: — column vectors are also orthonormal
47. Special Unitary Matrices — Global phase has no observable consequence — versus — Special unitary matrices:
48. Rule 2 (Evolution) N x N unitary matrix — Rule 1 (State Description) N states, vector of amplitudes — Quantum Information — Processing Device
49. Quantum Rule 3 — probabilities sum to 1: — completeness — probability
50. The Computational Basis — We have already described measurements with outcomes — Measurement operators: — state of system after measurement is
