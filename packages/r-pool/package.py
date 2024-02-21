# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPool(RPackage):
	"""Object Pooling.

	Enables the creation of object pools, which make it less computationally
	expensive to fetch a new object. Currently the only supported pooled
	objects are 'DBI' connections."""

	cran = "pool"

	version("1.0.2", md5="ae035ad96eb24d12dbfea7b681b02efa")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-later@1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
