# Quantum Computing
- **Event / Venue:** UW Architecture 2008 (2008)
- **Format:** `KEY` (`arch.key.zip`)
- **Slides:** 93

## Extracted Slide Text

1. Quantum Computing | Architectures | Dave Bacon | University of Washington
2. A Simple Question | Why is computation physically possible? | bits | behind the bit
3. Category Errors | Analog / Digital | 0.998213123.... | vs
4. Analog Probabilistic | Digital Deterministic | bits | behind the bit
5. Deeper | bits | noisy bits | quantum bit
6. Quantum Propaganda | I think I can safely say that nobody | understands quantum mechanics. | Niels Bohr
7. Hogwash | They understand it | They use it | But do they believe it?
8. What is Quantum Theory? | Electromagnetism | Weak force | Strong force
9. Bits, Pbits, Qubits | Configurations: | Description: | Observation:
10. Interference | measure | 50% | 100%
11. Garden of Re-forking Paths | 0.6 | 0.4 | 0.5
12. Quantum Computers | Peter Shor, 1994: | Quantum computers can efficiently factor | No known classical efficient algorithm.
13. Stop Worrying and Love Quantum Theory
14. Quantum Algorithms | Shor’s Algorithm | Breaks RSA and Diffie-Hellmann | Grov’er
15. A Simple Question | Why is computation physically possible? | bits | behind the bit
16. A Theory Solution | Error Correction | 0→000 | 1→111
17. Perfection Through Concatenation | failure | probability | cp 2
18. Fault-Tolerant Computation | von Neumann 1952
19. Quantum Circuit | Time | Preparation | Gates
20. Quantum Challenges | Quantum info | cannot be copied: | “no fan-out”
21. Error Correction | Peter Shor | Andrew Steane | classical error
22. Fault-Tolerant Quantum Computation | Must design quantum circuits which succeed even when | every element of the circuit (preparation, unitary gates, | Measurements) can fail.
23. Threshold Theorem, 1996 | QC | “decoherence” | “imprecision”
24. Architectures For Quantum Computers | Systems-level challenges to achieving scalable, fault-tolerant | quantum computation | Error Correction
25. Building Blocks | qubits | stationary | walking
26. Ion Trap | 2 9 Be + Ions in an Ion Trap | Oscillating electric | fields trap ions
27. Where’s the Qubit? | Energy | orbitals | Each ion = 1 qubit
28. http://iontrap.physics.lsa.umich.edu/ | research/trap | Sketch Ion Trap QC | “electrodes”
29. Time Scales | walking | Example: | ion trap qubits
30. Quantum Memory Hierarchy | Memory error rates << Errors during computation | Error correction more frequent during computation | More ancillas (used for error correction) in compute region
31. Quantum Memory Hierarchy | Slow memory / Fast compute leads to standard cache ideas… | except…
32. Communication | P f =(p 0 ) k | Distance k | Exponential
33. Quantum Teleportation | 1 qubit | 2 bits | Alice wants to send to Bob
34. Moving Qubits | Teleportation channel | entangled qubits | Entanglement distillation
35. Teleportation Units | classical control | Purification | Teleportation
36. Quantum Architectures | New generation of tools in order to aid in the design of quantum computing architectures….
37. Tools! | High level | description of | fault-tolerant
38. High Level Languages | operator dft(qureg q) { // main operator | const n=#q; // set n to length of input | int i; int j; // declare loop counters
39. Quantum Assembly Language | qubit q0 | qubit q1 | qubit q2
40. Scheduler | Example from Chuang group at http://www.media.mit.edu/quanta
41. Further Resources | Quantum Computing For Computer Scientists (David Mermin): | http://people.ccmr.cornell.edu/~mermin/qcomp/CS483.html | “Standard” Textbook:
42. Quantum Architectures | Today: a taste | ....becoming extremely important | 5-8 qubit ion trap machines
43. DiVincenzo’s Criteria | David | DiVincenzo | 1. Well defined qubits in a scalable architecture
44. Ion Trap | 2 9 Be + Ions in an Ion Trap | Oscillating electric | fields trap ions
45. Where’s the Qubit? | Energy | orbitals | Each ion = 1 qubit
46. Scalable? | Well defined qubits in a scalable architecture? | Solid state qubits seem to have a huge advantage for scalability.
47. Measurement | Energy | laser | decay
48. Single Qubit Operations | Energy | Laser 1 | Laser 2
49. Initialization | laser | decay | Laser 1
50. Universal Computers | Turing machine reads state of tape at current position. | Based on this reading and state of machine, Turing machine writes new symbol at current position and possibly moves left or right, and updates state. | Certain 
51. Universal Quantum Computer | U(2) | a quantum computer which can be programmed to perform any algorithmic manipulation on quantum information. | Set of Universal Quantum Gates
52. stationary | Coupling Two Qubits | sloshing mode | These modes can be used as a bus between the qubits.
53. What is the Problem? | Real quantum systems are open quantum systems! | system | environment
54. More Obstructions | FAULTY CONTROL | System | Controller
55. Games | Shor’s Algorithm | Breaks RSA and Diffie-Hellmann | Grov’er
56. Games | Shor’s Algorithm | Breaks RSA and Diffie-Hellmann | Grov’er
57. AND-OR Tree Evaluation | Shor’s Algorithm | Breaks RSA and Diffie-Hellmann | Grov’er
58. AND-OR Tree Evaluation | Shor’s Algorithm | Breaks RSA and Diffie-Hellmann | Grov’er
