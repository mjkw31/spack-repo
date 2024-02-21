# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethinheritsim(RPackage):
	"""Simulating Whole-Genome Inherited Bisulphite Sequencing Data

	Simulate a multigeneration methylation case versus control experiment with inheritance relation using a real control dataset.
	"""
	
	homepage = "https://github.com/belleau/methInheritSim"
	bioc = "methInheritSim" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/methInheritSim_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/methInheritSim/methInheritSim_1.24.0.tar.gz"]

	version("1.24.0", md5="c695628dcb686ee7e6a3f4ee134481ff")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-methylkit", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
