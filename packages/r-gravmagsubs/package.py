# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGravmagsubs(RPackage):
	"""Gravitational and Magnetic Attraction of 3-D Vertical
Rectangular Prisms

	Computes the gravitational and magnetic anomalies generated by
  3-D vertical rectangular prisms at specific observation points using the
  method of Plouff (1976) <doi:10.1190/1.1440645>.
	"""
	
	homepage = "https://code.usgs.gov/gmegsc/gravmagsubs"
	cran = "gravmagsubs"

	version("1.0.1", md5="efe8725a03511ebe32be612f7db408bf")

	depends_on("r-rcpp", type=("build", "run"))
