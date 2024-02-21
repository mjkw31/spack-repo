# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeDvirilisEnsemblDvircaf1(RPackage):
	"""Full genome sequences for Drosophila virilis (assembly dvir_caf1)

	Full genome sequences for Drosophila virilis (assembly dvir_caf1, GenBank assembly accession GCA_000005245.1) as provided by Ensembl and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Dvirilis.Ensembl.dvircaf1" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Dvirilis.Ensembl.dvircaf1_1.4.3.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Dvirilis.Ensembl.dvircaf1/BSgenome.Dvirilis.Ensembl.dvircaf1_1.4.3.tar.gz"]

	version("1.4.3", md5="6a6a6dc7b2d68a741c85525045a67890", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Dvirilis.Ensembl.dvircaf1_1.4.3.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation