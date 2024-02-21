# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssertiveSets(RPackage):
	"""Assertions to Check Properties of Sets.

	A set of predicates and assertions for checking the properties of sets.
	This is mainly for use by other package developers who want to include
	run-time testing features in their own packages. End-users will usually
	want to use assertive directly."""

	cran = "assertive.sets"

	version("0.0-3", md5="060f193e9ae8c91487cf3478720d920c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-assertive-base@0.0.7:", type=("build", "run"))
