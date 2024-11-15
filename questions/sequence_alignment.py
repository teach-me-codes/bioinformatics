questions = [
    {
        'Main question': 'What is Sequence Alignment in the context of bioinformatics?',
        'Explanation': 'The concept of Sequence Alignment involves arranging DNA, RNA, or protein sequences to identify regions of similarity that may indicate functional, structural, or evolutionary relationships. It is a fundamental tool in bioinformatics for comparing sequences and inferring biological information.',
        'Follow-up questions': ['How is Sequence Alignment used to analyze evolutionary relationships between species?', 'Can you describe the difference between global and local alignment algorithms?', 'What are the key challenges faced when aligning sequences with differing lengths and mutations?']
    },
    {
        'Main question': 'How do tools like BLAST contribute to Sequence Alignment processes?',
        'Explanation': 'The role of tools like BLAST (Basic Local Alignment Search Tool) in bioinformatics is to enable rapid sequence comparison. BLAST uses heuristic algorithms to find local sequence alignments that are statistically significant.',
        'Follow-up questions': ['What factors influence the choice between using BLAST and ClustalW for sequence alignment tasks?', 'Can you explain the concept of E-value in BLAST searches and its significance in result interpretation?', 'How does database selection impact the accuracy and speed of sequence alignments using tools like BLAST?']
    },
    {
        'Main question': 'What are the primary applications of Sequence Alignment in biological research?',
        'Explanation': 'The diverse applications of Sequence Alignment include identifying conserved motifs, predicting protein structures, annotating genes, and elucidating evolutionary histories.',
        'Follow-up questions': ['How does multiple sequence alignment differ from pairwise sequence alignment in terms of biological insights gained?', 'In what ways can Sequence Alignment aid in predicting the functional consequences of genetic variations?', 'Can you discuss any examples where Sequence Alignment has led to significant discoveries in the field of molecular biology?']
    },
    {
        'Main question': 'How do scoring matrices like BLOSUM and PAM enhance the accuracy of Sequence Alignments?',
        'Explanation': 'Scoring matrices like BLOSUM and PAM assign scores to aligned residues based on their evolutionary relationships, guiding sequence alignment algorithms.',
        'Follow-up questions': ['What criteria are considered when selecting an appropriate scoring matrix for a given sequence alignment task?', 'How do substitution matrices like BLOSUM differ from distance matrices in molecular phylogenetics?', 'Can you explain how scoring matrices influence the computational complexity of sequence alignment algorithms?']
    },
    {
        'Main question': 'How does dynamic programming optimize Sequence Alignment algorithms?',
        'Explanation': 'Dynamic programming, as seen in algorithms like Needleman-Wunsch and Smith-Waterman, finds the optimal alignment between sequences efficiently by calculating alignment scores and traceback paths.',
        'Follow-up questions': ['What are the computational advantages of dynamic programming over heuristic methods in sequence alignment?', 'How do gap penalties influence alignment outcomes in dynamic programming algorithms?', 'Explain the significance of the recurrence relation in dynamic programming for solving alignment problems.']
    },
    {
        'Main question': 'What are the differences between global and local Sequence Alignment algorithms?',
        'Explanation': 'Global alignment finds the best overall match between sequences, while local alignment identifies regions of similarity regardless of overall sequence similarity.',
        'Follow-up questions': ['How are scoring schemes adjusted to accommodate gaps in global and local alignment algorithms?', 'When is local alignment more appropriate than global alignment for sequence comparison?', 'What are the advantages of employing both global and local alignment strategies in sequence database searches?']
    },
    {
        'Main question': 'How can mismatch penalties influence the outcome of Sequence Alignments?',
        'Explanation': 'Mismatch penalties assign costs to mismatched residues during alignment, impacting the choice of optimal alignments and overall alignment quality.',
        'Follow-up questions': ['Considerations for setting mismatch penalties for different sequences?', 'Relationship between mismatch penalties and alignment sensitivity versus specificity?', 'How do mismatch penalty strategies affect alignment complexity and accuracy?']
    },
    {
        'Main question': 'What role do gap opening and extension penalties play in Sequence Alignment algorithms?',
        'Explanation': 'Gap penalties introduce and extend gaps between aligned sequences, balancing alignment quality by managing costs.',
        'Follow-up questions': ['How do gap penalties impact overall alignment similarity score?', 'Concept of affine gap penalties and their advantages over linear gaps?', 'Optimization strategies for gap penalties in sequence alignment tasks?']
    },
    {
        'Main question': 'How do iterative alignment algorithms like PSI-BLAST improve the accuracy of sequence database searches?',
        'Explanation': 'Iterative algorithms like PSI-BLAST refine search results and detect remote homologs by building profiles of conserved regions for increased sensitivity.',
        'Follow-up questions': ['Key parameters for optimizing PSI-BLAST search performance?', 'How does database size affect iterative alignment effectiveness?', 'Challenges or limitations with iterative alignment strategies in sequence analysis?']
    },
    {
        'Main question': 'What are the advantages of using multiple sequence alignment techniques?',
        'Explanation': 'Benefits of multiple sequence alignment include identifying conserved residues, inferring evolutionary relationships, and predicting protein structures based on conservation patterns.',
        'Follow-up questions': ['Impact of input sequence quality on multiple alignment accuracy?', 'How do profile-based methods enhance sequence search sensitivity?', 'Computational challenges with scaling up multiple sequence alignment?']
    }
]