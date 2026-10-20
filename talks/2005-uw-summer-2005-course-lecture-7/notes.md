# CSEP 590tv: Quantum Computing
- **Event / Venue:** UW Summer 2005 Course - Lecture 7 (2005)
- **Format:** `PPT` (`Lecture7.ppt`)
- **Slides:** 63

## Extracted Slide Text

1. CSEP 590tv: Quantum Computing — Dave Bacon — Aug 3, 2005 — Today’s Menu
2. Administrivia — Hand in HW #5. — Pick up HW solutions. — Pick up the Take Home Final!
3. Review — David — Deutsch — Richard
4. Review — qubits — Deutsch-Jozsa Algorithm — Bernsetein-Vazirani Algorithm
5. Review — Dan — Simon — 1994: Simon’s Algorithm
6. Review — n qubits — n qubits — Simon’s algorithm
7. Today: — Factoring
8. One Time Pads — Alice — Bob — 0010101111010001
9. Public Key Cryptography — Interesting history: — 1st schemes “known in public” where put forth by — Diffie and Hellman in 1976 (key exchange) and
10. Computational Complexity — P : decision problems which can be solved without error in — polynomial time on a deterministic classical Turing machine. — Decision problems: problem with a yes/no answer.
11. Computational Complexity — NP : decision problems which can be solved without error in — a polynomial time on a classical nondeterministic Turing machine. Shorthand, decision problems which, given a solution, and you can verify this solutio
12. One Million Dollars — NP — NP=P — OR
13. Public Key Cryptography — 1. There probably exist computational problems that are HARD. — 2. Can we use these to perform secure cryptography by basing — the security of the problem on the difficulty of the hard problem?
14. Public Key Cryptography Roughly — Alice — Bob — Instructions for how
15. Public Key Encryption RSA — Alice — Bob — Alice generates two random large primes, and
16. Public Key Encryption: RSA — Alice — Bob — Public Key:
17. Public Key Encryption: RSA — Alice — Bob — Public Key:
18. Public Key Encryption: RSA — Alice — Bob — Public Key:
19. Factoring — NPC — NP — Factoring: Is one of the factors less than k?
20. Shor’s Algorithm — 18819881292060796383869723946165043 — 98071635633794173827007633564229888 — 59715234665485319060606504743045317
21. Shor’s Algorithm — What were the key insights which Shor used? — Simon’s problem work’s because the function has a symmetry: — In this case the symmetry is a symmetry
22. Period Finding — Given: A function from 0,1,…,N-1 to some n bit numbers — Promise: The function is guaranteed to satisfy — Problem: Find the hidden period
23. Shor’s Algorithm — What were the key insights which Shor used? — 1. Period finding — 2. Period finding can be perform efficiently on a quantum
24. Order-Finding and Factoring — Factor N — choose x coprime to N (Euclid’s algorithm for gcd) — Order finding: find smallest r such that
25. Order-Finding and Period-Finding — Order finding: find r such that — Find the period of — What were the key insights which Shor used?
26. Fourier Transforms — Function of a single bit: — We could equally well deal with — Because we can “invert”:
27. Fourier Transforms — Output: — The Hadmard is performing this transform (up to a constant) — on the AMPLITUDES of our wave function!
28. Fourier Transforms — Function on N different inputs: — We can the define the following N new numbers to represent — the function:
29. Nth Root Of Unity — Unit modulus: — Nth root of unity: — Re
30. Nth Root Of Unity — The big sum: — for — for
31. Nth Root Of Unity — The sum of all sums: — Re — Im
32. Fourier Transforms — Function on N different inputs: — We can the define the following N new numbers to represent — the function:
33. Fourier Transforms — It works!....
34. Fourier Transforms — Example:
35. Fourier Transforms — Example: — Fourier transformed coefficients:
36. Unitarity & Fourier Transforms — Output: — New amplitudes are Fourier transform of old amplitudes!
37. Quantum Fourier Transform — The quantum Fourier transform: — See it in action:
38. Quantum Fourier Transform — The quantum Fourier transform: — But is it unitary?
39. Quantum Fourier Transform — And about that inverse QFT: — It performs the inverse Fourier transform on the amplitudes!
40. In Class Problem #1
41. Period Finding — quantum — oracle — Problem: find in as few
42. Fourier — to the Rescue — probability
43. Shor’s Algorithm — To Factor N on a quantum computer: — Select x coprime to N — Use the quantum computer to find the period of
44. QFT over 2n — This circuit requires O(n2) “elementary” gates — QFTs for all other Ns can similarly be implemented.
45. Fourier — to the Rescue — O(n3) “elementary” gates — modular exponentiation
46. Shor’s Algorithm — To Factor N on a quantum computer: — Select x coprime to N — Use the quantum computer to find the period of
47. Shor’s Algorithm — 18819881292060796383869723946165043 — 98071635633794173827007633564229888 — 59715234665485319060606504743045317
48. Grover’s Problem — n qubit — 1qubit — Suppose we have a black box
49. Grover’s Algorithm — n qubit — Use the black box in a particular way — Grover oracle:
50. The Grover Iterate — n qubits
