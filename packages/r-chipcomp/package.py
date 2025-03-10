# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipcomp(RPackage):
	"""Quantitative comparison of multiple ChIP-seq datasets

	ChIPComp detects differentially bound sharp binding sites across multiple conditions considering matching control.
	"""
	
	bioc = "ChIPComp" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ChIPComp_1.32.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ChIPComp/ChIPComp_1.32.0.tar.gz"]

	version("1.32.0", md5="5294eab6ada6b66e52935843dd9acc6b")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
	depends_on("r-bsgenome-mmusculus-ucsc-mm9", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
