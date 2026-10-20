# CSEP 590tv: Quantum Computing
- **Event / Venue:** UW Summer 2005 Course - Lecture 6 (2005)
- **Format:** `PPT` (`Lecture6.ppt`)
- **Slides:** 92

## Extracted Slide Text

1. CSEP 590tv: Quantum Computing — Dave Bacon — July 27, 2005 — Today’s Menu
2. Administrivia — Turn in HW #4. — Pick up HW #5. — #1
3. Recap — Quantum teleportation: — 50 % 0, 50 % 1 — 50 % 0, 50 % 1
4. Recap — n qubit computational qubit basis: — n bit string — n qubit computational qubit wave functions:
5. Recap — n qubit computational qubit basis: — n bit string — n qubit computational qubit wave functions:
6. Recap — Hadamard orthogonality relationship: — or
7. Classical Promise Problem — Query Complexity — Given: A black box which computes some function — k bit input
8. Quantum Promise Query Complexity — Given: A quantum gate which, when used as a classical device — computes a reversible function — k qubit input
9. Functions — We can write the unitary — k qubit input — k qubit output
10. Functions — Note that the transform is unitary — When — precisely when f(x) is
11. Functions — One to one — Example: — Not one to one:
12. An Aside on Functions — n qubits — k qubits — function from n bits
13. An Aside on Functions — n qubits — k qubits — function from n bits
14. From This Perspective — “identity” — NOT 2nd bit — controlled-NOT
15. Query Complexities — black box — Exact classical — query complexity
16. Quantum Algorithms — David — Deutsch — Richard
17. Quantum Algorithms — 1993: Bernstein-Vazirani Algorithm — (recursive) — Umesh
18. The Factoring Firestorm — 18819881292060796383869723946165043 — 98071635633794173827007633564229888 — 59715234665485319060606504743045317
19. Deutsch-Jozsa Problem — Given: A function with n bit strings as input and one bit as — output — (this will be a non-reversible function)
20. Classical Deutsch-Jozsa — constant — balanced — Problem: determine whether the function is constant or
21. Classical Deutsch-Jozsa — constant — balanced — Problem: determine whether the function is constant or
22. Quantum Deutsch-Jozsa — Given: A quantum gate on n+1 qubits strings which calculates — the promised f — n qubit
23. Trick 1: Phase Kickback — Input a superposition over second register: — Function is computed into phase:
24. Trick 2: Hadamarding Qubits — Note: — and
25. Tricks 1 and 2 Together — qubits
26. Tricks 1 and 2 Together — n qubits
27. Function in the Phase — constant — balanced
28. Function in the Phase — When the function is constant: — When the function is balanced: — amplitude in zero state
29. Quantum Deutsch-Jozsa — qubits — If function is constant, r is always 0. — If function is balanced, r is never 0.
30. Deutsch-Jozsa — David — Deutsch — Richard
31. Bernstein-Vazirani Problem — Given: A function with n bit strings as input and one bit as — output — Promise: The function is of the form
32. Classical Bernstein-Vazirani — Given: A function with n bit strings as input and one bit as — output — Promise: The function is of the form
33. Quantum Bernstein-Vazirani — n qubits
34. Hadamard It!
35. Quantum Bernstein-Vazirani — qubits — We can determine using only a single quantum query!
36. Bernstein-Vazirani — 1993: Bernstein-Vazirani Algorithm — (non-recursive) — Umesh
37. In Class Problem #1
38. Simon’s Problem — Given: A function with n bit strings as input and one bit as — output — Promise: The function is guaranteed to satisfy
39. Classical Simon’s Problem — Promise: The function is guaranteed to satisfy — Suppose we start querying the function and build up a list — of the pairs
40. Quantum Simon’s Problem — black box — Unlike previous problems, we can’t use the phase kickback — trick because there is no structure in the function.
41. Quantum Simon’s Problem — n qubits — n qubits
42. Quantum Simon’s Problem — Measure the second register — Using the promise on the function — This implies that after we measure, we have the state
43. Quantum Simon’s Problem — Measuring this state in the computational basis at this time — does us no good…. — For random uniformly distributed
44. Quantum Simon’s Problem — n qubits — n qubits
45. Quantum Simon’s Problem — Measuring this state, we obtain uniformly distributed random — values of such that — If we have eliminated the possible values of by half
46. Quantum Simon’s Problem — On values of which are 0, this doesn’t restrict — On values of which are 1, the corresponding must — XOR to 0. This restricts the set of possible ‘s by half.
47. (Z2)n Vectors — Think about the bit strings as vectors in — If single run eliminates half, multiple runs….how to solve? — vectors in
48. (Z2)n Vectors — Example: — We can multiply these vectors by a scalar in — Example:
49. (Z2)n Vectors — dot product of vectors in — Example:
50. (Z2)n Vectors — vectors in — one possible basis:
