# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsri(RPackage):
	"""Gene Set Regulation Index

	The GSRI package estimates the number of differentially expressed genes in gene sets, utilizing the concept of the Gene Set Regulation Index (GSRI).
	"""
	
	bioc = "GSRI" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GSRI_2.50.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GSRI/GSRI_2.50.0.tar.gz"]

	version("2.50.0", md5="686ab91e4ee0adeb4828a5b2ac2f6943")

	depends_on("r@2.14.2:", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-les@1.1.6:", type=("build", "run"))
