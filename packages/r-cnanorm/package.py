# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnanorm(RPackage):
	"""A normalization method for Copy Number Aberration in cancer samples

	Performs ratio, GC content correction and normalization of data obtained using low coverage (one read every 100-10,000 bp) high troughput sequencing. It performs a "discrete" normalization looking for the ploidy of the genome. It will also provide tumour content if at least two ploidy states can be found.
	"""
	
	homepage = "http://www.r-project.org"
	bioc = "CNAnorm" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CNAnorm_1.48.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CNAnorm/CNAnorm_1.48.0.tar.gz"]

	version("1.48.0", md5="b9d0f995f3466875285a152415863842")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
