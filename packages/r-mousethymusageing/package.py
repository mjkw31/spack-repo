# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMousethymusageing(RPackage):
	"""Single-cell Transcriptomics Data of the Ageing Mouse Thymus

	This package provides data access to counts matrices and meta-data for single-cell RNA sequencing data of thymic epithlial cells across mouse ageing using SMARTseq2 and 10X Genommics chemistries. Access is provided as a data package via ExperimentHub. It is designed to facilitate the re-use of data from Baran-Gale _et al._ in a consistent format that includes relevant and informative meta-data.
	"""
	
	bioc = "MouseThymusAgeing" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/MouseThymusAgeing_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/MouseThymusAgeing/MouseThymusAgeing_1.10.0.tar.gz"]

	version("1.10.0", md5="cf1889c22fa9e5ac5899a4d911907a90")

	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

	# experiment