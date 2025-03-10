# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpvsnp(RPackage):
	"""Gene set analysis methods for SNP association p-values that lie in genes in given gene sets

	Gene set analysis methods exist to combine SNP-level association p-values into gene sets, calculating a single association p-value for each gene set. This package implements two such methods that require only the calculated SNP p-values, the gene set(s) of interest, and a correlation matrix (if desired). One method (GLOSSI) requires independent SNPs and the other (VEGAS) can take into account correlation (LD) among the SNPs. Built-in plotting functions are available to help users visualize results.
	"""
	
	bioc = "cpvSNP" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/cpvSNP_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/cpvSNP/cpvSNP_1.34.0.tar.gz"]

	version("1.34.0", md5="2edb50570eb609c9962e57d36d70ceba")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-gseabase@1.24:", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
