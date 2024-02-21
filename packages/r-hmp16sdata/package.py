# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmp16sdata(RPackage):
	"""16S rRNA Sequencing Data from the Human Microbiome Project

	HMP16SData is a Bioconductor ExperimentData package of the Human Microbiome Project (HMP) 16S rRNA sequencing data for variable regions 1–3 and 3–5. Raw data files are provided in the package as downloaded from the HMP Data Analysis and Coordination Center. Processed data is provided as SummarizedExperiment class objects via ExperimentHub.
	"""
	
	homepage = "https://github.com/waldronlab/HMP16SData"
	bioc = "HMP16SData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/HMP16SData_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/HMP16SData/HMP16SData_1.22.0.tar.gz"]

	version("1.22.0", md5="a137f917000e15acffca9bb0baac8fbb")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))

	# experiment