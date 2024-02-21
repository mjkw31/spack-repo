# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasicstarrseq(RPackage):
	"""Basic peak calling on STARR-seq data

	Basic peak calling on STARR-seq data based on a method introduced in "Genome-Wide Quantitative Enhancer Activity Maps Identified by STARR-seq" Arnold et al. Science. 2013 Mar 1;339(6123):1074-7. doi: 10.1126/science. 1232542. Epub 2013 Jan 17.
	"""
	
	bioc = "BasicSTARRseq" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BasicSTARRseq_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BasicSTARRseq/BasicSTARRseq_1.30.0.tar.gz"]

	version("1.30.0", md5="45c21fe93b28467ae466fd4017792494")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
