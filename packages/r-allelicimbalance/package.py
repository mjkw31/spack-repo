# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAllelicimbalance(RPackage):
	"""Investigates Allele Specific Expression.

	Provides a framework for allelic specific expression investigation using
	RNA-seq data."""

	bioc = "AllelicImbalance"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/AllelicImbalance_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/AllelicImbalance/AllelicImbalance_1.40.0.tar.gz"]

	version("1.40.0", md5="9eb6991f47f1337aef63f9ce750db08a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-genomicranges@1.31.8:", type=("build", "run"))
	depends_on("r-summarizedexperiment@0.2:", type=("build", "run"))
	depends_on("r-genomicalignments@1.15.6:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-bsgenome@1.47.3:", type=("build", "run"))
	depends_on("r-variantannotation@1.25.11:", type=("build", "run"))
	depends_on("r-biostrings@2.47.6:", type=("build", "run"))
	depends_on("r-s4vectors@0.17.25:", type=("build", "run"))
	depends_on("r-iranges@2.13.12:", type=("build", "run"))
	depends_on("r-rsamtools@1.99.3:", type=("build", "run"))
	depends_on("r-genomicfeatures@1.31.3:", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
