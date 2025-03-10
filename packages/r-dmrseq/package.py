# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmrseq(RPackage):
	"""Detection and inference of differentially methylated regions from Whole Genome Bisulfite Sequencing

	This package implements an approach for scanning the genome to detect and perform accurate inference on differentially methylated regions from Whole Genome Bisulfite Sequencing data. The method is based on comparing detected regions to a pooled null distribution, that can be implemented even when as few as two samples per population are available. Region-level statistics are obtained by fitting a generalized least squares (GLS) regression model with a nested autoregressive correlated error structure for the effect of interest on transformed methylation proportions.
	"""
	
	bioc = "dmrseq" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/dmrseq_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/dmrseq/dmrseq_1.22.0.tar.gz"]

	version("1.22.0", md5="a8181423ea50609ae16545b9f8bb1895")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bsseq", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-bumphunter", type=("build", "run"))
	depends_on("r-delayedmatrixstats@1.1.13:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-outliers", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-annotatr", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
