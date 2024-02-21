# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAllmll(RPackage):
	"""A subset of arrays from a large acute lymphoblastic leukemia (ALL) study

	This package provides probe-level data for 20 HGU133A and 20 HGU133B arrays which are a subset of arrays from a large ALL study. The data is for the MLL arrays. This data was published in Mary E. Ross, Xiaodong Zhou, Guangchun Song, Sheila A. Shurtleff, Kevin Girtman, W. Kent Williams, Hsi-Che Liu, Rami Mahfouz, Susana C. Raimondi, Noel Lenny, Anami Patel, and James R. Downing (2003) Classification of pediatric acute lymphoblastic leukemia by gene expression profiling Blood 102: 2951-2959
	"""
	
	bioc = "ALLMLL" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/ALLMLL_1.42.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/ALLMLL/ALLMLL_1.42.0.tar.gz"]

	version("1.42.0", md5="669e7ff030b6fea51c8013816bd6fae7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-affy@1.23.4:", type=("build", "run"))

	# experiment