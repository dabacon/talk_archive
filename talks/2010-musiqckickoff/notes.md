# Quantum State and Process Tomography
- **Event / Venue:** MUSIQCKickoff (2010)
- **Format:** `KEY` (`KickItOff.key.zip`)
- **Slides:** 32

## Extracted Slide Text

1. Quantum State and Process Tomography | (and Quantum Algorithms) | Dave Bacon (University of Washington) | MUSIQC Kickoff Meeting
2. QW (“Q”-Dub) Theory Group | Dave Bacon | Aram Harrow | Gregory Crosswhite (Physics)
3. Overview | To verify the workings of the MUSIQC prototypes, we must provide tools for characterizing the basic operating units acting alone and acting together. | For small systems this is tractable, but for larger systems this quickly beco
4. Goals | Provide tools and protocols necessary for the experimentalists to perform tractable heralded ansatz tomography (state and process). Pass results of this onto system model / FT efforts. | Design quantum algorithms that are specifical
5. Qubits Tomography | State: | Process: | Subtleties:
6. Not All States Are Created Equal | Separable states on n qubits | parameters | We would like to consider methods for
7. Matrix Product States | total parameters | If D is polynomial in n, then # parameters poly in n | (D exponential in n captures all possible pure states)
8. Matrix Product States | OMG
9. Matrix Product States | matrix
10. Matrix Product States | -dim vector | matrices | If D is polynomial in n then this calculation is polytime
11. Matrix Product States | Efficiently classically store information about state | Use this information to efficiently calculate results of few-qubit measurements | Shouldn’t have “holes”: inefficient use can capture generic state
12. Matrix Product State Tomography | Can we make polynomial # measurement on n qubit state and learn a MPS description of the state (if it exists)? | [Cramer, Plenio arXiv:1002.3780] | [Flammia, Gross, Bartlett, Somma arXiv:1002.3839]
13. MPS Pure State Tomography | Basic idea: | Perform traditional (or compressed sensing based) tomography on constant k contiguous qubits | Solve for MPS using variational method, DMRG based method, quantum 2-SAT approach
14. Matrix Product State Tomography | [Cramer, Plenio arXiv:1002.3780] | - Compressed sensing approach to obtaining local density matrices | [Flammia, Gross, Bartlett, Somma arXiv:1002.3839]
15. Heralded Tomography | [Flammia, Gross, Bartlett, Somma arXiv:1002.3839] | By constructing the “parent Hamiltonian” of a MPS description one can use this to verify the accuracy of the MPS | “Announces when it fails”
16. Symmetrized Tomography | If states (processes) are symmetric with respect to some group, this can reduce the size of their description | Example: permutationally invariant qubit mixed states | [Toth, Wieczorek, Gross, Krischek, Schwemmer, W
17. Tomography Tool Chest | Variety of tomography protocols: MPS, Symmetry based, Compressed sensing, MERA + other ansatz based methods | Estimation procedures: MPS and MERA (Variational, DMRG, Quantum 2-SAT), Maximum likelihood, Hedged maximum
18. Quantum Algorithms | Factoring | Discrete Log | Grover Search
19. Quantum Algorithms | Which to choose? | System optimization study will identify what reasonable fault-tolerant quantum error correction plus algorithm can be implemented on MUSIQC | In the mean time....
20. Starting a War With DMRG | MUSIQC-80 will be in a size range where | Simulating it using the best classical methods will start to be come difficult | Design efficient MUSIQC executable quantum circuits which have large MPS descriptions and 
21. Why MPS classically efficient? | To keep the matrix problems arising in DMRG, one enforces | this is nothing more than condition that A is valid quantum superoperator! | DMRG works because it is simulating D dimensional quantum circuit!
22. Conclusion | MPS Tomography and Symmetrized Tomography provide tractable methods for analyzing MUSIQC architecture. | Will produce toolkit that describes measurement protocol and processes measurement data to execute this tomography | Quant
