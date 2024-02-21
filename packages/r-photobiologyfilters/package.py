# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhotobiologyfilters(RPackage):
	"""Spectral Transmittance and Spectral Reflectance Data

	Spectral 'transmittance' data for frequently used filters and 
    similar materials. Plastic sheets and films; photography filters; 
    theatrical gels; machine-vision filters; various types of window glass;
    optical glass and some laboratory plastics and glassware. Spectral 
    reflectance data for frequently encountered materials. Part of the
    'r4photobiology' suite, Aphalo P. J. (2015) <doi:10.19232/uv4pb.2015.1.14>.
	"""
	
	homepage = "https://docs.r4photobiology.info/photobiologyFilters/"
	cran = "photobiologyFilters" 

	version("0.5.2", md5="7f71d5a509539c8c82ac746d006e314e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-photobiology@0.10.4:", type=("build", "run"))
