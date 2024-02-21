# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylaiddata(RPackage):
	"""MethylAid-summarized data for 2800 Illumina 450k array samples and 2620 EPIC array samples

	A data package containing summarized Illumina 450k array data on 2800 samples and summarized EPIC data for 2620 samples. The data can be use as a background data set in the interactive application.
	"""
	
	bioc = "MethylAidData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/MethylAidData_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/MethylAidData/MethylAidData_1.34.0.tar.gz"]

	version("1.34.0", md5="95cc72b436067e4a8046564381101e04")

	depends_on("r-methylaid", type=("build", "run"))
	depends_on("r@3.2:", type=("build", "run"))

	# experiment