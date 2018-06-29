"""
A python3 script that takes alignment files and creates a treefile using SNP variant
"""
print("TREEMAKER v0.1 is a phylogeny tree builder that takes alignment files and constructs a relationship tree. Written by Idowu Olawoye @idowuolawoye\n")

import argparse

parser = argparse.ArgumentParser(description='A phylogeny tree builder.')
parser.add_argument('-V','--version',action='version', version='TREEMAKER v0.1 Released 27/06/2018')

args= parser.parse_args()
from Bio import Seq
from Bio import AlignIO

aln = str(input("Enter path to Alignment file:"))
 
while aln:
	print("""
		1.Parsimony Tree constructor
		2.Distance Tree constructor (Neighbour Joining)
		3.Distance Tree constructor (UPGMA)
		""")
	align=input("What model will you like to use?")
	if align=="1":
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
#Generates parsimony tree using maximum likelihood. Tree file is saved in newick format
		Phylo.write(pars_tree, aln+".newick", 'newick')
		print("DONE.\n")
		print('Tree file can be found in', aln+'.newick')
		Phylo.draw(pars_tree)
		break
	if align=="2":
		align = AlignIO.parse (aln, 'phylip')
		for alignment in align:
			print(alignment)
			print('')
			print('Building Tree...\n')
		from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
		from Bio.Phylo.TreeConstruction import DistanceCalculator
		calculator= DistanceCalculator('blosum62')
		constructor = DistanceTreeConstructor(calculator,'nj')
		pars_tree= constructor.build_tree(alignment)
		print(pars_tree)
		print('\n')
		from Bio import Phylo
#Generates parsimony tree using maximum likelihood. Tree file is saved in newick format
		Phylo.write(pars_tree, aln+".newick", 'newick')
		print("DONE.\n")
		print('Tree file can be found in', aln+'.newick')
		Phylo.draw(pars_tree)
		break
	if align=="3":
		align = AlignIO.parse (aln, 'phylip')
		for alignment in align:
			print(alignment)
			print('')
			print('Building Tree...\n')
		from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
		from Bio.Phylo.TreeConstruction import DistanceCalculator
		calculator= DistanceCalculator('blosum62')
		constructor = DistanceTreeConstructor(calculator,'upgma')
		pars_tree= constructor.build_tree(alignment)
		print(pars_tree)
		print('\n')
		from Bio import Phylo
#Generates parsimony tree using maximum likelihood. Tree file is saved in newick format
		Phylo.write(pars_tree, aln+".newick", 'newick')
		print("DONE.\n")
		print('Tree file can be found in', aln+'.newick')
		Phylo.draw(pars_tree)
		break
	else:
		print("\n Not valid")
		break

