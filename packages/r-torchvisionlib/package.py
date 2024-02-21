# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTorchvisionlib(RPackage):
	"""Additional Operators for Image Models

	Implements additional operators for computer vision models, including
    operators necessary for image segmentation and object detection deep learning
    models.
	"""
	
	cran = "torchvisionlib" 

	version("0.4.0", md5="f4820397b7a252ee7d586ecf535fd506")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-torch", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
