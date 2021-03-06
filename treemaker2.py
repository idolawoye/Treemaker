"""
A python3 script that takes alignment files and constructs phylogeny
"""
print("TREEMAKER v0.1 is a phylogeny tree builder that takes alignment files and constructs a relationship tree. Written by Idowu Olawoye @idowuolawoye\n")

import argparse
from Bio import Seq
from Bio import AlignIO
from Bio.Phylo.PAML import baseml

parser = argparse.ArgumentParser(description='A phylogeny tree builder.')
parser.add_argument('-V','--version',action='version', version='TREEMAKER v0.1 Released 27/06/2018')

args= parser.parse_args()

aln = str(input("Enter path to Alignment file:"))
 
while aln:
	print("""
		1.Parsimony Tree constructor
		2.Distance Tree constructor (Neighbour Joining)
		3.Distance Tree constructor (UPGMA)
		4.Maximum Likelihood using TN93 model
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

		Phylo.write(pars_tree, aln+".newick", 'newick')
		print("DONE.\n")
		print('Tree file can be found in', aln+'.newick')
		Phylo.draw(pars_tree)
		break
	if align =="4":
		out = str(input("Enter path to output file and filename:"))
		work_dir = str(input("Enter path to working directory:"))
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
		Phylo.write(pars_tree, aln+".newick", 'newick')
		with open(aln,'r') as original:
			allLines = original.readlines()
		allLines[0] = allLines[0].rstrip() + "I\n"
		modifyFile = open(aln,'w')
		for i in allLines:
			modifyFile.write(i)
		modifyFile.close()

		bml = baseml.Baseml()
		bml.alignment = aln
		bml.tree = aln+".newick"
		bml.out_file = out
		bml.working_dir = work_dir
		bml.set_options(runmode=2, model=6)
		bml.run()
		
		with open (out, 'r') as result:
			lines = result.readlines()
		print("Best tree found:")
		print(lines[-1])
		last = lines[-1]
		newtree = open(out+".newick", "w")
		newtree.write(last)
		newtree.close()
		print("Maximum Likelihood tree built with TN93 model found in:")
		print(work_dir)
	else:
		print("\n Not valid")
		break

