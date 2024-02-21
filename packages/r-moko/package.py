# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoko(RPackage):
	"""Multi-Objective Kriging Optimization

	Multi-Objective optimization based on the Kriging metamodel.
  Important functions: mkm() (builder for the multiobjective models), MVPF() (sequential minimizator using variance reduction), 
  MEGO() (generalization of ParEgo) and HEGO() (minimizator using the expected hypervolume improvement).
  References are Passos and Luersen (2018) <doi:10.1590/1679-78254324>.
	"""
	
	homepage = "https://github.com/coldfir3/moko"
	cran = "moko" 

	version("1.0.3", md5="8bdde3bf680585d50ed8e08919638866")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dicekriging@1.5.5:", type=("build", "run"))
	depends_on("r-gensa@1.1.6:", type=("build", "run"))
	depends_on("r-emoa@0.5:", type=("build", "run"))
	depends_on("r-mco@1.0.15.1:", type=("build", "run"))
	depends_on("r-gpareto@1.0.2:", type=("build", "run"))
