# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDada2(RPackage):
	"""Accurate sample inference from amplicon data with single nucleotide
	resolution"""

	homepage = "https://benjjneb.github.io/dada2/"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/dada2_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/dada2/dada2_1.30.0.tar.gz"]

	version("1.30.0", md5="096baf34b4618af27b1b430945d3a189", url="https://www.bioconductor.org/packages/release/bioc/src/contrib/dada2_1.30.0.tar.gz")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biostrings@2.42.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-reshape2@1.4.1:", type=("build", "run"))
	depends_on("r-shortread@1.32:", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-iranges@2.6:", type=("build", "run"))
	depends_on("r-xvector@0.16:", type=("build", "run"))
	depends_on("r-biocgenerics@0.22:", type=("build", "run"))
