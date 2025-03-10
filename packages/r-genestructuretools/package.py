# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenestructuretools(RPackage):
	"""Tools for spliced gene structure manipulation and analysis

	GeneStructureTools can be used to create in silico alternative splicing events, and analyse potential effects this has on functional gene products.
	"""
	
	bioc = "GeneStructureTools" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GeneStructureTools_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GeneStructureTools/GeneStructureTools_1.22.0.tar.gz"]

	version("1.22.0", md5="513385498b639ea6acc724bb3795de38")

	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-bsgenome-mmusculus-ucsc-mm10", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
