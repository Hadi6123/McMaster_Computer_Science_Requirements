from abc import ABC

# not required but a good idea
class DataStrategy(ABC):
    def getData(self): pass


class YearOneStrategy(DataStrategy):

    def getData(self):
        tableData = [
            {'Course Code':'COMPSCI 1MD3', 'Course Name':'Introduction to Programming', 'Description':'Introduction to fundamental programming concepts: values and types, expressions and evaluation, control flow constructs and exceptions, recursion, input/output and file processing.', 'Requirements': "One of MATH 1K03, 1LS3, Grade 12 Advanced Functions and Introductory Calculus U, Grade 12 Calculus and Vectors, or registration or credit in ARTSSCI 1D06", 'Units': 3},
            {'Course Code':'COMPSCI 1JC3', 'Course Name':'Introduction to Computational Thinking', 'Description':'Exploration of thinking that is inspired, supported, and enabled by computing. Survey of the salient ideas, methods, and technologies in the major areas of computing including basic data types, logic, operating systems, computer networking, web computing, information security, digital media, software development, and problem solving techniques. Introduction to the fundamentals of functional programming.', 'Requirements': "One of MATH 1K03, Grade 12 Advanced Functions and Introductory Calculus U, Grade 12 Calculus and Vectors, or registration in Computer Science 1", 'Units': 3},
            {'Course Code':'COMPSCI 1DM3', 'Course Name':'Discrete Mathematics for Computer Science', 'Description':'Sets, functions, relations, trees and graphs; counting principles, modular arithmetic, discrete probabilities; induction and recursion, recurrence relations.', 'Requirements': "MATH 1B03 or MATH 1ZC3 or registration in the Honours Computer Science as a Second Degree (B.A.Sc.)", 'Units': 3},
            {'Course Code':'COMPSCI 1XD3', 'Course Name':'Computer Science Practice and Experience: Introduction to Software Design Using Web Programming', 'Description':'Introduction to different aspects of design: Identifying user needs, goals and desires and translating them into software, and structuring and communicating the structure of software to improve reliability, readability and adaptability. Topics include web languages and protocols, types and design patterns', 'Requirements': " COMPSCI 1JC3; COMPSCI 1MD3 or MATH 1MP3 ", 'Units': 3},
            {'Course Code':'COMPSCI 1XC3', 'Course Name':'Computer Science Practice and Experience: Development Basics', 'Description':'Acquiring familiarity with professional software development settings via practical experience with interaction with UNIX-like systems, programming in C, with documentation, testing, benchmarking, profiling and debugging; shell interaction and programming, pipes and filters; revision control.', 'Requirements': "One of COMPSCI 1MD3 or ENGINEER 1D04 or MATH 1MP3", 'Units': 3},
            {'Course Code':'MATH 1B03', 'Course Name':'Linear Algebra I', 'Description':'Vector spaces given by solutions to linear systems. Linear independence, dimension. Determinants. Eigenvalues, eigenvectors and diagonalisation. Complex numbers.', 'Requirements': "Grade 12 Calculus and Vectors U or MATH 1F03", 'Units': 3},
            {'Course Code':'MATH 1ZA3', 'Course Name':'Engineering Mathematics I', 'Description':'Functions: limits, continuity, derivatives, optimization, curve sketching. Antiderivative, definite integral, techniques of integration, with applications', 'Requirements': "Registration in a program in Engineering", 'Units': 3},
            {'Course Code':'MATH 1ZB3', 'Course Name':'Engineering Mathematics II', 'Description':'Techniques of integration, applications of definite integrals, differential equations, polar coordinates, parametrized curves. Sequences, infinite series, power series. Partial derivatives.', 'Requirements': "MATH 1ZA3", 'Units': 3},
        ]
        
        return tableData


class YearTwoStrategy(DataStrategy):

    def getData(self):
        tableData = [
            {'Course Code':'COMPSCI 2AC3', 'Course Name':'Automata and Computability', 'Description':'Finite state machines, regular languages, regular expressions, applications of regular languages, grammars, context-free languages, models of computation, computability and decidability.',
                    'Requirements': "COMPSCI 2LC3, COMPSCI 2C03", 'Units': 3},
            {'Course Code':'COMPSCI 2C03', 'Course Name':'Data Strcutures and Algorithms', 'Description':'Basic data structures: stacks, queues, hash tables, and binary trees; searching and sorting; graph representations and algorithms, including minimum spanning trees, traversals, shortest paths; introduction to algorithmic design strategies; correctness and performance analysis.', 
                    'Requirements': "One of the following: COMPSCI 1DM3 or 2DM3; COMPSCI 1XC3 or 1XD3 or 1MD3 or MATH 1MP3, and registration in an Honours Computer Science program or in one of Mathematics and Computer Science, Economics and Computer Science, Arts & Sciences and Computer Science OR COMPSCI 1DM3 with a result of at least B, and one of COMPSCI 1XC3 or 1XD3 or 1MD3 or MATH 1MP3 with a result of at least B", 'Units': 3},
            {'Course Code':'COMPSCI 2DB3', 'Course Name':'Databases', 'Description':'Data modelling, integrity constraints, principles and design of relational databases, relational algebra, SQL, query processing, transactions, concurrency control, recovery, security and data storage.', 
                    'Requirements': "COMPSCI 2LC3 OR COMPSCI 2DM3", 'Units': 3},
            {'Course Code':'COMPSCI 2GA3', 'Course Name':'Computer Architecture', 'Description':'Introduction to logic gates, computer arithmetic, instruction-set architecture, assembly programming, translation of high-level languages into assembly. Computer system organization: datapath and control, pipelining, memory hierarchies, I/O systems; measures of performance.', 
                    'Requirements': "One of the following: COMPSCI 1XC3 and 1DM3 and registration in an Honours Computer Science program or in one of Mathematics and Computer Science, Economics and Computer Science, Arts & Sciences and Computer Science OR COMPSCI 1XC3 and 1DM3, each with a result of at least B", 'Units': 3},
            {'Course Code':'COMPSCI 2LC3', 'Course Name':'Logical Reasoning for Computer Science', 'Description':'Introduction to logic and proof techniques for practical reasoning: propositional logic, predicate logic, structural induction; rigorous proofs in discrete mathematics and programming.', 
                    'Requirements': "One of the following: COMPSCI 1DM3, 1JC3; one of COMPSCI 1MD3, 1XC3, 1XD3, and registration in an Honours Computer Science program or in one of Mathematics and Computer Science, Economics and Computer Science, Arts & Sciences and Computer Science OR COMPSCI 1DM3, 1JC3, and one of COMPSCI 1MD3, 1XC3, 1XD3, each with a result of at least B", 'Units': 3},
            {'Course Code':'COMPSCI 2ME3', 'Course Name':'Introduction to Software Development', 'Description':'Classes and inheritance, class invariants, interface specifications; object-oriented design patterns; exception handling; tools for interface documentation, testing, program analysis; requirements documentation; quality attributes; development models.', 
                    'Requirements': "One of the following: COMPSCI 1XC3 or 1XD3, and registration in an Honours Computer Science program or in one of Mathematics and Computer Science, Economics and Computer Science, Arts & Sciences and Computer Science OR COMPSCI 1DM3 and one of 1XC3 and 1XD3, each with a result of at least B", 'Units': 3},
            {'Course Code':'COMPSCI 2SD3', 'Course Name':'Concurrent Systems', 'Description':'Models of concurrency: process algebras, Petri nets, temporal logics and model checking; concurrency as software structuring principle: processes, threads, synchronization mechanisms, resource management and sharing; deadlock, safety and liveness; design, verification and testing of concurrent systems.', 
                    'Requirements': "COMPSCI 2C03, 2LC3 or 2DM3, 2ME3", 'Units': 3},
            {'Course Code':'COMPSCI 2XC3', 'Course Name':'Computer Science Practice and Experience: Algorithms and Software Design', 'Description':'Implementation of computational solutions to practical problems that combine algorithmic design and analysis with software design principles, through an experiential approach in simulated workplace environments. Communication skills: Technical documentation and presentation.', 
                    'Requirements': "COMPSCI 1XC3, 2C03, 2ME3", 'Units': 3}
        ]
        
        return tableData

class YearThreeStrategy(DataStrategy):
    
    def getData(self):
        tableData = [
            {'Course Code':'COMPSCI 3AC3', 'Course Name':'Algorithms and Complexity', 'Description':'Basic computability models; the Church-Turing thesis, complexity classes; P versus NP; NP-completeness, reduction techniques; algorithmic design strategies; flows, distributed algorithms, advanced techniques such as randomization.', 'Requirements': "COMPSCI 2C03 or SFWRENG 2C03, COMPSCI 2AC3 or 2FA3 or SFWRENG 2FA3 ", 'Units': 3},
            {'Course Code':'COMPSCI 3MI3', 'Course Name':'Principles of Programming Languages', 'Description':'Principles of definition of and reasoning about programming languages and domain-specific languages; use of semantics for interpretation and in program analyses for correctness, security and efficiency.', 'Requirements': "COMPSCI 2C03, and COMPSCI 2LC3 or 2DM3, and COMPSCI 2AC3 or 2FA3, and COMPSCI 2ME3 ", 'Units': 3},
            {'Course Code':'COMSCI 3N03', 'Course Name':'Computer Networks and Security', 'Description':'Physical networks, TCP/IP protocols, switching methods, network layering and components, network services. Information security, computer and network security threats, defence mechanisms, encryption.', 'Requirements': "Credit or registration in COMPSCI 3SH3", 'Units': 3},
            {'Course Code':'COMPSCI 3SH3', 'Course Name':'Computer Science Practice and Experience: Operating Systems', 'Description':'Processes and threads, synchronization and communication; scheduling, memory management; file systems; resource protection; structure of operating systems.', 'Requirements': "COMPSCI 2SD3 or 3SD3, COMPSCI 2C03, and COMPSCI 2GA3", 'Units': 3},
            {'Course Code':'COMPSCI 3TB3', 'Course Name':'Syntax-Based Tools and Compilers', 'Description':'Lexical analysis, syntax analysis, type checking; syntax-directed translation, attribute grammars; compiler structure; implications of computer architecture; mapping of programming language concepts; code generation and optimization.', 'Requirements': "COMPSCI 2C03 or SFWRENG 2C03, and COMPSCI 2GA3 or SFWRENG 2GA3 or 3GA3, and COMPSCI 2AC3 or 2FA3 or SFWRENG 2FA3, and COMPSCI 3MI3 or registration in Level IV or above of a Software Engineering program", 'Units': 3},
            {'Course Code':'STATS 2D03', 'Course Name':'Introduction to Probability', 'Description':'Combinatorics, independence, conditioning; Poisson-process; discrete and continuous distributions with statistical applications; expectation, transformations moment-generating functions joint, marginal and conditional distributions; covariance and correlation; central limit theorem.', 'Requirements': "One of ARTSSCI 1D06 A/B, MATH 1AA3, 1LT3, 1NN3, 1XX3, 1ZB3, 1ZZ5 or ISCI 1A24 A/B", 'Units': 3},
        ]
        
        return tableData

class YearFourStrategy(DataStrategy):
    
    def getData(self):
        tableData = [
            {'Course Code':'COMPSCI 4ZP6 A/B', 'Course Name':'Capstone Project', 
             'Description':'Students, in teams of two to four students, undertake a substantial project in an area of computer science by performing each step of the software life cycle. The lecture component presents an introduction to software management and project management.', 
             'Requirements': "Registration in Level IV of an Honours Computer Science program, Honours Business Informatics or Honours Computer Science as a Second Degree (B.A.Sc.) ", 'Units': 6}
        ]
        
        return tableData
