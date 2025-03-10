# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCasper(RPackage):
	"""Characterization of Alternative Splicing based on Paired-End Reads

	Infer alternative splicing from paired-end RNA-seq data. The model is based on counting paths across exons, rather than pairwise exon connections, and estimates the fragment size and start distributions non-parametrically, which improves estimation precision.
	"""
	
	bioc = "casper" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/casper_2.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/casper/casper_2.36.0.tar.gz"]

	version("2.36.0", md5="4c9fc29e3b92d5b493953ea97436556a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocgenerics@0.31.6:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-ebarrays", type=("build", "run"))
	depends_on("r-gaga", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
