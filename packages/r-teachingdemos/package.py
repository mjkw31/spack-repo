# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTeachingdemos(RPackage):
	"""Demonstrations for Teaching and Learning.

	Demonstration functions that can be used in a classroom to demonstrate
	statistical concepts, or on your own to better understand the concepts
	or the programming."""

	cran = "TeachingDemos"

	version("2.12.1", md5="222dadfab4352ba610ad72b699e7ba10")

	depends_on("r@2.10:", type=("build", "run"))
