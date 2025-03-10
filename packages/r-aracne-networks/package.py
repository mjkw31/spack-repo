# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAracneNetworks(RPackage):
	"""ARACNe-inferred gene networks from TCGA tumor datasets

	This package contains ARACNe-inferred networks from TCGA tumor datasets. It also contains a function to export them into plain-text format.
	"""
	
	bioc = "aracne.networks" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/aracne.networks_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/aracne.networks/aracne.networks_1.28.0.tar.gz"]

	version("1.28.0", md5="42657d0acf4c1ba54aa2057fa4525d51")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-viper", type=("build", "run"))

	# experiment