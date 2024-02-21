# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcsea(RPackage):
	"""Methylated CpGs Set Enrichment Analysis

	Identification of diferentially methylated regions (DMRs) in predefined regions (promoters, CpG islands...) from the human genome using Illumina's 450K or EPIC microarray data. Provides methods to rank CpG probes based on linear models and includes plotting functions.
	"""
	
	bioc = "mCSEA" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/mCSEA_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/mCSEA/mCSEA_1.22.0.tar.gz"]

	version("1.22.0", md5="8bac97f11934f91da5250521a7b26f75")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mcseadata", type=("build", "run"))
	depends_on("r-homo-sapiens", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
