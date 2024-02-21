# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImmunoclust(RPackage):
	"""immunoClust - Automated Pipeline for Population Detection in Flow Cytometry

	immunoClust is a model based clustering approach for Flow Cytometry samples. The cell-events of single Flow Cytometry samples are modelled by a mixture of multinominal normal- or t-distributions. The cell-event clusters of several samples are modelled by a mixture of multinominal normal-distributions aiming stable co-clusters across these samples.
	"""
	
	bioc = "immunoClust" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/immunoClust_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/immunoClust/immunoClust_1.34.0.tar.gz"]

	version("1.34.0", md5="b83f47eaa19d45984b19f4071b455873")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
