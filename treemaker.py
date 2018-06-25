"""
A python3 script that takes alignment files and creates a treefile using SNP variant
"""
print("TREEMAKER v0.1 is a phylogeny tree builder that takes alignment files and constructs a relationship tree. Written by Idowu Olawoye\n")

from Bio import Seq
from Bio import AlignIO

aln = str(input("Enter path to Alignment file:"))

align = AlignIO.parse (aln, 'phylip')
for alignment in align:
	print(alignment)
	print('')
print('Building Tree...\n')

from Bio.Phylo.TreeConstruction import *
scorer= ParsimonyScorer()
searcher = NNITreeSearcher(scorer)
constructor = ParsimonyTreeConstructor(searcher)
pars_tree = constructor.build_tree(alignment)
print(pars_tree)
print('\n')
from Bio import Phylo
#Generates parsimony tree using maximum likelihood? You can save treefile
Phylo.write(pars_tree, aln+".newick", 'newick')
print("DONE.\n")
print('Tree file can be found in', aln+'.newick')
Phylo.draw(pars_tree)

