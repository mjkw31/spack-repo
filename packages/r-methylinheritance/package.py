# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylinheritance(RPackage):
	"""Permutation-Based Analysis associating Conserved Differentially Methylated Elements Across Multiple Generations to a Treatment Effect

	Permutation analysis, based on Monte Carlo sampling, for testing the hypothesis that the number of conserved differentially methylated elements, between several generations, is associated to an effect inherited from a treatment and that stochastic effect can be dismissed.
	"""
	
	homepage = "https://github.com/adeschen/methylInheritance"
	bioc = "methylInheritance" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/methylInheritance_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/methylInheritance/methylInheritance_1.26.0.tar.gz"]

	version("1.26.0", md5="0242605800daea10c810fa356cb2cf0c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-methylkit", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rebus", type=("build", "run"))
