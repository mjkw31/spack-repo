# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsims(RPackage):
	"""Bird Point Count Simulator

	A highly scientific and utterly addictive 
  bird point count simulator 
  to test statistical assumptions, aid survey design,
  and have fun while doing it.
  The simulations follow time-removal and distance sampling models 
  based on Matsuoka et al. (2012) <doi:10.1525/auk.2012.11190>,
  Solymos et al. (2013) <doi:10.1111/2041-210X.12106>,
  and Solymos et al. (2018) <doi:10.1650/CONDOR-18-32.1>,
  and sound attenuation experiments by 
  Yip et al. (2017) <doi:10.1650/CONDOR-16-93.1>.
	"""
	
	homepage = "https://github.com/psolymos/bSims"
	cran = "bSims" 

	version("0.3-0", md5="e04d2d5d7e8f462a2b93f0df2a723b6e")

	depends_on("r-intrval", type=("build", "run"))
	depends_on("r-mefa4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-deldir@1.0.2:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
