# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrugs(RPackage):
	"""Interface to the 'OpenBUGS' MCMC Software

	Fully-interactive R interface to the 'OpenBUGS' software for Bayesian analysis using MCMC sampling.  Runs natively and stably in 32-bit R under Windows.  Versions running on x86Linux and on 64-bit R under Windows are in "beta" status and less efficient.
	"""
	
	cran = "BRugs"

	version("0.9-2", md5="de753658f47fda8f8a74b32757a9f038")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
