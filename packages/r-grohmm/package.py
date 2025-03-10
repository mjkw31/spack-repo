# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrohmm(RPackage):
	"""GRO-seq Analysis Pipeline

	A pipeline for the analysis of GRO-seq data.
	"""
	
	homepage = "https://github.com/Kraus-Lab/groHMM"
	bioc = "groHMM" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/groHMM_1.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/groHMM/groHMM_1.36.0.tar.gz"]

	version("1.36.0", md5="0b1077948ddc9895c57188ca2560bc10")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-s4vectors@0.17.25:", type=("build", "run"))
	depends_on("r-iranges@2.13.12:", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges@1.31.8:", type=("build", "run"))
	depends_on("r-genomicalignments@1.15.6:", type=("build", "run"))
	depends_on("r-rtracklayer@1.39.7:", type=("build", "run"))
