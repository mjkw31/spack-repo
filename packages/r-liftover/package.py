# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLiftover(RPackage):
	"""Changing genomic coordinate systems with rtracklayer::liftOver

	The liftOver facilities developed in conjunction with the UCSC browser track infrastructure are available for transforming data in GRanges formats.  This is illustrated here with an image of the EBI/NHGRI GWAS catalog that is, as of May 10 2017, distributed with coordinates defined by NCBI build hg38.
	"""
	
	homepage = "https://www.bioconductor.org/help/workflows/liftOver/"
	bioc = "liftOver" 
	urls = ["https://www.bioconductor.org/packages/release/workflows/src/contrib/liftOver_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/workflows/src/contrib/Archive/liftOver/liftOver_1.26.0.tar.gz"]

	version("1.26.0", md5="65b97e4b79a79c7a4bbdebcb647f1faf")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-gwascat", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-homo-sapiens", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))

	# workflow