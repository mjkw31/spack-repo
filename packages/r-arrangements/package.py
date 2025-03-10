# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArrangements(RPackage):
	"""Fast Generators and Iterators for Permutations, Combinations, Integer
	Partitions and Compositions.

	Fast generators and iterators for permutations, combinations, integer
	partitions and compositions. The arrangements are in lexicographical order
	and generated iteratively in a memory efficient manner. It has been
	demonstrated that 'arrangements' outperforms most existing packages of
	similar kind. Benchmarks could be found at
	<https://randy3k.github.io/arrangements/articles/benchmark.html>."""

	cran = "arrangements"

	version("1.1.9", md5="7bcc173930f14c27fb5a6af6f51f4877")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("gmp@4.2.3:", type=("build", "link", "run"))
