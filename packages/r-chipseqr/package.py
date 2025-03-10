# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipseqr(RPackage):
	"""Identifying Protein Binding Sites in High-Throughput Sequencing Data

	ChIPseqR identifies protein binding sites from ChIP-seq and nucleosome positioning experiments. The model used to describe binding events was developed to locate nucleosomes but should flexible enough to handle other types of experiments as well.
	"""
	
	bioc = "ChIPseqR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ChIPseqR_1.56.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ChIPseqR/ChIPseqR_1.56.0.tar.gz"]

	version("1.56.0", md5="8696d6a783d26d8c6225ec4e3f294110")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges@2.5.14:", type=("build", "run"))
	depends_on("r-hilbertvis", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
	depends_on("r-timsac", type=("build", "run"))
