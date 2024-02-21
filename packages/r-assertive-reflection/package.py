# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssertiveReflection(RPackage):
	"""Assertions for Checking the State of R.

	A set of predicates and assertions for checking the state and capabilities
	of R, the operating system it is running on, and the IDE being used. This
	is mainly for use by other package developers who want to include run-time
	testing features in their own packages. End-users will usually want to use
	assertive directly."""

	cran = "assertive.reflection"

	version("0.0-5", md5="e5b52b04481fe2b713a668262fb1c642")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-assertive-base@0.0.7:", type=("build", "run"))
