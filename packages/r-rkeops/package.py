# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRkeops(RPackage):
	"""Kernel Operations on GPU or CPU, with Autodiff, without Memory
Overflows

	The 'KeOps' library lets you compute generic reductions of
	very large arrays whose entries are given by a mathematical formula
	with CPU and GPU computing support. It combines a tiled reduction
	scheme with an automatic differentiation engine. It is perfectly
	suited to the efficient computation of Kernel dot products and the
	associated gradients, even when the full kernel matrix does not fit
	into the GPU memory.
	"""
	
	homepage = "https://www.kernel-operations.io/rkeops/"
	cran = "rkeops"

	version("2.2.2", md5="de562db012b60ed240908446d0feec74")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("python@3.5.0:", type=("build", "link", "run"))
