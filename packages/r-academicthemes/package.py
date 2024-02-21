# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcademicthemes(RPackage):
	"""Colour Plots with Palettes from Academic Institutions

	Functionality to allow users to easily colour plots with the colour
    palettes of various academic institutions.
	"""
	
	homepage = "https://github.com/hwarden162/AcademicThemes"
	cran = "AcademicThemes" 

	version("0.0.1", md5="53451f81e9d3a6fd18ce6c5f32d3ee22")

	depends_on("r-ggplot2", type=("build", "run"))
