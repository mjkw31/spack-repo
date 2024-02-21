# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicscores(RPackage):
	"""Infrastructure to work with genomewide position-specific scores

	Provide infrastructure to store and access genomewide position-specific scores within R and Bioconductor.
	"""
	
	homepage = "https://github.com/rcastelo/GenomicScores"
	bioc = "GenomicScores" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GenomicScores_2.14.3.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GenomicScores/GenomicScores_2.14.3.tar.gz"]

	version("2.14.3", md5="eabfc2c53e94ac24ef186413e38872fc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-s4vectors@0.7.21:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocgenerics@0.13.8:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-iranges@2.3.23:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
