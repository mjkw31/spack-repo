# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuratedbreastdata(RPackage):
	"""Curated breast cancer gene expression data with survival and treatment information

	Curated human breast cancer tissue S4 ExpresionSet datasets from over 16 clinical trials comprising over 2,000 patients. All datasets contain at least one type of outcomes variable and treatment information (minimum level: whether they had chemotherapy and whether they had hormonal therapy). Includes code to post-process these datasets.
	"""
	
	bioc = "curatedBreastData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/curatedBreastData_2.30.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/curatedBreastData/curatedBreastData_2.30.0.tar.gz"]

	version("2.30.0", md5="41383ff9e1295448ec0e8004789ab9d5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))

	# experiment