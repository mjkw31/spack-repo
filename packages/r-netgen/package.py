# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetgen(RPackage):
	"""Network Generator for Combinatorial Graph Problems

	Methods for the generation of a wide range of network geographies,
    e.g., grid networks or clustered networks. Useful for the generation of
    benchmarking instances for the investigation of, e.g., Vehicle-Routing-Problems
    or Travelling Salesperson Problems.
	"""
	
	homepage = "https://github.com/jakobbossek/netgen"
	cran = "netgen" 

	version("1.3.2", md5="63c7ac5ee371b4bb6b95c95b52f53f7b")

	depends_on("r-bbmisc@1.6:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.2:", type=("build", "run"))
	depends_on("r-lhs@0.10:", type=("build", "run"))
	depends_on("r-checkmate@1.8:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph@0.7.1:", type=("build", "run"))
	depends_on("r-stringr@0.6.2:", type=("build", "run"))
