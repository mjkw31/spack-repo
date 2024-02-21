# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmhelprs(RPackage):
	"""Helper Functions for Linear Model Analysis

	A collection of helper functions for multiple
  regression models fitted by lm(). Most of them are simple
  functions for simple tasks which can be done with coding,
  but may not be easy for occasional users of R. Most of
  the tasks addressed are those sometimes needed when
  using the 'manymome' package (Cheung and Cheung, 2023,
  <doi:10.3758/s13428-023-02224-z>) and 'stdmod' package
  (Cheung, Cheung, Lau, Hui, and Vong, 2022,
  <doi:10.1037/hea0001188>). However, they can also be used
  in other scenarios.
	"""
	
	homepage = "https://sfcheung.github.io/lmhelprs/"
	cran = "lmhelprs" 

	version("0.2.0", md5="44d1d20971a6e53912d4729edb4d7862")

	depends_on("r@2.10:", type=("build", "run"))
