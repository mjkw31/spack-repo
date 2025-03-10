# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssign(RPackage):
	"""Adaptive Signature Selection and InteGratioN (ASSIGN)

	ASSIGN is a computational tool to evaluate the pathway deregulation/activation status in individual patient samples. ASSIGN employs a flexible Bayesian factor analysis approach that adapts predetermined pathway signatures derived either from knowledge-based literature or from perturbation experiments to the cell-/tissue-specific pathway signatures. The deregulation/activation level of each context-specific pathway is quantified to a score, which represents the extent to which a patient sample encompasses the pathway deregulation/activation signature.
	"""
	
	homepage = "https://compbiomed.github.io/ASSIGN/"
	bioc = "ASSIGN" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ASSIGN_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ASSIGN/ASSIGN_1.38.0.tar.gz"]

	version("1.38.0", md5="c03c8eedec6379aa0fac65d11377fdf8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-rlab", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
