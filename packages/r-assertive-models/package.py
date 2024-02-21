# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssertiveModels(RPackage):
	"""Assertions to Check Properties of Models.

	A set of predicates and assertions for checking the properties of models.
	This is mainly for use by other package developers who want to include
	run-time testing features in their own packages. End-users will usually
	want to use assertive directly."""

	cran = "assertive.models"

	version("0.0-2", md5="93672bbfaa32c656ab6956e71aa0db67")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-assertive-base@0.0.2:", type=("build", "run"))
