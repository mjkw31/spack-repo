# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlgem(RPackage):
	"""Detect differential expression in microarray and proteomics datasets with the Power Law Global Error Model (PLGEM)

	The Power Law Global Error Model (PLGEM) has been shown to faithfully model the variance-versus-mean dependence that exists in a variety of genome-wide datasets, including microarray and proteomics data. The use of PLGEM has been shown to improve the detection of differentially expressed genes or proteins in these datasets.
	"""
	
	homepage = "http://www.genopolis.it"
	bioc = "plgem" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/plgem_1.74.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/plgem/plgem_1.74.0.tar.gz"]

	version("1.74.0", md5="caa3e3fe048da49643b34bde9fcb834a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
