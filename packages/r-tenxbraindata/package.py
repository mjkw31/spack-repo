# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTenxbraindata(RPackage):
	"""Data from the 10X 1.3 Million Brain Cell Study

	Single-cell RNA-seq data for 1.3 million brain cells from E18 mice, generated by 10X Genomics.
	"""
	
	bioc = "TENxBrainData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/TENxBrainData_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/TENxBrainData/TENxBrainData_1.22.0.tar.gz"]

	version("1.22.0", md5="1fa1b93ab8d144b860c83dc5741490a0")

	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-annotationhub@2.9.22:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

	# experiment