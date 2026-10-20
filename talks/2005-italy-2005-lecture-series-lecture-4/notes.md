# Quantum Computing
- **Event / Venue:** Italy 2005 Lecture Series - Lecture 4 (2005)
- **Format:** `PPT` (`ItalyLecture4.ppt`)
- **Slides:** 61

## Extracted Slide Text

1. Quantum Computing — Dave Bacon — Department of Computer Science & Engineering — University of Washington
2. Summary of Last Lecture
3. Classical Promise Problem — Query Complexity — Given: A black box which computes some function — k bit input
4. Quantum Promise Query Complexity — Given: A quantum gate which, when used as a classical device — computes a reversible function — k qubit input
5. Functions — We can write the unitary — k qubit input — k qubit output
6. Functions — Note that the transform is unitary — When — precisely when f(x) is
7. Functions — One to one — Example: — Not one to one:
8. An Aside on Functions — n qubits — k qubits — function from n bits
9. An Aside on Functions — n qubits — k qubits — function from n bits
10. From This Perspective — “identity” — NOT 2nd bit — controlled-NOT
11. Query Complexities — black box — Exact classical — query complexity
12. Quantum Algorithms — David — Deutsch — Richard
13. Quantum Algorithms — 1993: Bernstein-Vazirani Algorithm — (recursive) — Umesh
14. The Factoring Firestorm — 18819881292060796383869723946165043 — 98071635633794173827007633564229888 — 59715234665485319060606504743045317
15. Deutsch-Jozsa Problem — Given: A function with n bit strings as input and one bit as — output — (this will be a non-reversible function)
16. Classical Deutsch-Jozsa — constant — balanced — Problem: determine whether the function is constant or
17. Classical Deutsch-Jozsa — constant — balanced — Problem: determine whether the function is constant or
18. Quantum Deutsch-Jozsa — Given: A quantum gate on n+1 qubits strings which calculates — the promised f — n qubit
19. Trick 1: Phase Kickback — Input a superposition over second register: — Function is computed into phase:
20. Trick 2: Hadamarding Qubits — Note: — and
21. Tricks 1 and 2 Together — qubits
22. Tricks 1 and 2 Together — n qubits
23. Function in the Phase — constant — balanced
24. Function in the Phase — When the function is constant: — When the function is balanced: — amplitude in zero state
25. Quantum Deutsch-Jozsa — qubits — If function is constant, r is always 0. — If function is balanced, r is never 0.
26. Deutsch-Jozsa — David — Deutsch — Richard
27. Bernstein-Vazirani Problem — Given: A function with n bit strings as input and one bit as — output — Promise: The function is of the form
28. Classical Bernstein-Vazirani — Given: A function with n bit strings as input and one bit as — output — Promise: The function is of the form
29. Quantum Bernstein-Vazirani — n qubits
30. Hadamard It!
31. Quantum Bernstein-Vazirani — qubits — We can determine using only a single quantum query!
32. Bernstein-Vazirani — 1993: Bernstein-Vazirani Algorithm — (non-recursive) — Umesh
33. Bernstein-Vazirani — 1993: Bernstein-Vazirani Algorithm — (recursive) — Umesh
34. Simon’s Problem — Given: A function with n bit strings as input and one bit as — output — Promise: The function is guaranteed to satisfy
35. Classical Simon’s Problem — Promise: The function is guaranteed to satisfy — Suppose we start querying the function and build up a list — of the pairs
36. Quantum Simon’s Problem — black box — Unlike previous problems, we can’t use the phase kickback — trick because there is no structure in the function.
37. Quantum Simon’s Problem — n qubits — n qubits
38. Quantum Simon’s Problem — Measure the second register — Using the promise on the function — This implies that after we measure, we have the state
39. Quantum Simon’s Problem — Measuring this state in the computational basis at this time — does us no good…. — For random uniformly distributed
40. Quantum Simon’s Problem — n qubits — n qubits
41. Quantum Simon’s Problem — Measuring this state, we obtain uniformly distributed random — values of such that — If we have eliminated the possible values of by half
42. Quantum Simon’s Problem — On values of which are 0, this doesn’t restrict — On values of which are 1, the corresponding must — XOR to 0. This restricts the set of possible ‘s by half.
43. (Z2)n Vectors — Think about the bit strings as vectors in — If single run eliminates half, multiple runs….how to solve? — vectors in
44. (Z2)n Vectors — Example: — We can multiply these vectors by a scalar in — Example:
45. (Z2)n Vectors — dot product of vectors in — Example:
46. (Z2)n Vectors — vectors in — one possible basis:
47. (Z2)n Vectors — vectors in — But we can expand in about a different set of vectors — Example:
48. (Z2)n Vectors — vectors in — But we can expand in about a different set of vectors — When these n vectors are linearly independent
49. Quantum Simon’s Problem — Think about the bit strings as vectors in — Multiple runs of the quantum algorithm yield equations — random
50. (Z2)n Vectors — Notice that if y is one of vectors with only one 1: — th bit — then this implies
