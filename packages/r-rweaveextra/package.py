# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRweaveextra(RPackage):
	"""Sweave Drivers with Extra Tricks Up their Sleeve

	Weave and tangle drivers for Sweave extending the
  standard drivers with additional code chunk options. Currently,
  these are only options to completely ignore, or skip, code chunks on
  weaving, tangling, or both. Chunks ignored on weaving are not parsed
  and are written out verbatim on tangling. Chunks ignored on tangling
  are processed as usual on weaving, but completely left out of the
  tangled scripts.
	"""
	
	homepage = "https://gitlab.com/vigou3/RweaveExtra"
	cran = "RweaveExtra" 

	version("1.0-0", md5="88a249c98734812813eaf5a79cd3be2b")

	depends_on("r@4.1.0:", type=("build", "run"))
