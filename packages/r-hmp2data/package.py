# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmp2data(RPackage):
	"""16s rRNA sequencing data from the Human Microbiome Project 2

	HMP2Data is a Bioconductor package of the Human Microbiome Project 2 (HMP2) 16S rRNA sequencing data. Processed data is provided as phyloseq, SummarizedExperiment, and MultiAssayExperiment class objects. Individual matrices and data.frames used for building these S4 class objects are also provided in the package.
	"""
	
	homepage = "https://github.com/jstansfield0/HMP2Data"
	bioc = "HMP2Data" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/HMP2Data_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/HMP2Data/HMP2Data_1.16.0.tar.gz"]

	version("1.16.0", md5="f334416386d2c1af677494e1fd5743d6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))

	# experiment