# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCircseqaligntk(RPackage):
	"""A toolkit for end-to-end analysis of RNA-seq data for circular genomes

	CircSeqAlignTk is designed for end-to-end RNA-Seq data analysis of circular genome sequences, from alignment to visualization. It mainly targets viroids which are composed of 246-401 nt circular RNAs. In addition, CircSeqAlignTk implements a tidy interface to generate synthetic sequencing data that mimic real RNA-Seq data, allowing developers to evaluate the performance of alignment tools and workflows.
	"""
	
	homepage = "https://github.com/jsun/CircSeqAlignTk"
	bioc = "CircSeqAlignTk" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CircSeqAlignTk_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CircSeqAlignTk/CircSeqAlignTk_1.4.0.tar.gz"]

	version("1.4.0", md5="2c3b93fca2c2974a45af093edf7d9558")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-rbowtie2", type=("build", "run"))
	depends_on("r-rhisat2", type=("build", "run"))
