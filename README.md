# Treemaker
A python script that takes alignment file, constructs a pylogeny tree, preview the tree image and saves the phylogeny tree as a PHYLIP output tree file.

### Dependencies:
* Biopython
* matplotlib
* Bio.Phylo
* PAML package

Ensure PAML is installed correctly by following the steps here http://abacus.gene.ucl.ac.uk/software/paml.html

Things to note when using Maximum Likelihood, ensure the phylip file has 2 or more spaces between the sequences and sequence name.

To view help on the command line, load the python file followed by -h or -v for version.

Treemaker can be run directly on the commandline or simply running the python file by double-clicking like an ```exe``` file. The program asks for an alignment file which can be a Phylip file and then the user is asked to select a model for building the phylogeny tree. Models are Parsimony tree constructor, Distance Tree constructor which can either be Neighbour joining OR Unweighted pair group method with arithmetic mean (UPGMA) and Maximum Likelihood using TN93 model. The program then proceeds to build the phylogeny tree and then saves it in the same directory where the alignment file was imported with same name of alignment file.

Example:

```TREEMAKER v0.1 is a phylogeny tree builder that takes alignment files and constructs a relationship tree. Written by Idowu Olawoye @idowuolawoye

Enter path to Alignment file:C:\Users\Idowu\AppData\Local\Programs\Python\Python36\biopython-1.70\Tests\Phylip\reference_dna2 - Copy.phy

                1.Parsimony Tree constructor
                2.Distance Tree constructor (Neighbour Joining)
                3.Distance Tree constructor (UPGMA)
                4.Maximum Likelihood using TN93 model

What model will you like to use?3
SingleLetterAlphabet() alignment with 6 rows and 39 columns
CGATGCTTACCGCCGATGCTTACCGCCGATGCTTACCGC Archaeopt
CGTTACTCGTTGTCGTTACTCGTTGTCGTTACTCGTTGT Hesperorni
TAATGTTAATTGTTAATGTTAATTGTTAATGTTAATTGT Baluchithe
TAATGTTCGTTGTTAATGTTCGTTGTTAATGTTCGTTGT B. virgini
CAAAACCCATCATCAAAACCCATCATCAAAACCCATCAT Brontosaur
GGCAGCCAATCACGGCAGCCAATCACGGCAGCCAATCAC B.subtilis

Building Tree...

Tree(rooted=True)
    Clade(branch_length=0, name='Inner5')
        Clade(branch_length=0.1126127132483844, name='Inner4')
            Clade(branch_length=0.2124773960216998, name='Inner1')
                Clade(branch_length=0.10714285714285715, name='B. virgini')
                Clade(branch_length=0.10714285714285715, name='Baluchithe')
            Clade(branch_length=0.06645569620253161, name='Inner2')
                Clade(branch_length=0.25316455696202533, name='Brontosaur')
                Clade(branch_length=0.25316455696202533, name='Hesperorni')
        Clade(branch_length=0.08670750276854927, name='Inner3')
            Clade(branch_length=0.27906976744186046, name='B.subtilis')
            Clade(branch_length=0.27906976744186046, name='Archaeopt')


DONE.

Tree file can be found in C:\Users\Idowu\AppData\Local\Programs\Python\Python36\biopython-1.70\Tests\Phylip\reference_dna2 - Copy.phy.newick
```
### References
1. Cock PA, Antao T, Chang JT, Chapman BA, Cox CJ, Dalke A, Friedberg I, Hamelryck T, Kauff F, Wilczynski B and de Hoon MJL (2009) Biopython: freely available Python tools for computational molecular biology and bioinformatics. Bioinformatics, 25, 1422-1423
2. Ziheng Yang; PAML 4: Phylogenetic Analysis by Maximum Likelihood, Molecular Biology and Evolution, Volume 24, Issue 8, 1 August 2007, Pages 1586–1591, https://doi.org/10.1093/molbev/msm088
