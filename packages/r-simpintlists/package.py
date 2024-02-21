# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimpintlists(RPackage):
	"""The package contains BioGRID interactions for various organisms in a simple format

	The package contains BioGRID interactions for arabidopsis(thale cress), c.elegans, fruit fly, human, mouse, yeast( budding yeast ) and S.pombe (fission yeast) . Entrez ids, official names and unique ids can be used to find proteins. The format of interactions are lists. For each gene/protein, there is an entry in the list with "name" containing name of the gene/protein and "interactors" containing the list of genes/proteins interacting with it.
	"""
	
	bioc = "simpIntLists" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/simpIntLists_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/simpIntLists/simpIntLists_1.38.0.tar.gz"]

	version("1.38.0", md5="9dbe0a1f390843a49bb11d05ac5f2e28")


	# experiment