# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsocat(RPackage):
	"""Isotope Origin Clustering and Assignment Tools

	This resource provides tools to create, compare, and post-process 
    spatial isotope assignment models of animal origin. It generates 
    probability-of-origin maps for individuals based on user-provided tissue and 
    environment isotope values (e.g., as generated by IsoMAP, Bowen et al. [2013] 
    <doi:10.1111/2041-210X.12147>) using the framework established in Bowen et al.
    (2010) <doi:10.1146/annurev-earth-040809-152429>). The package 'isocat' can then 
    quantitatively compare and cluster these maps to group individuals by 
    similar origin. It also includes techniques for applying four approaches 
    (cumulative sum, odds ratio, quantile only, and quantile simulation) with 
    which users can summarize geographic origins and probable distance traveled 
    by individuals. Campbell et al. [2020] establishes several of the functions
    included in this package <doi:10.1515/ami-2020-0004>.
	"""
	
	cran = "isocat" 

	version("0.2.6", md5="3f480d8e54e63f2098b098784f8ef9d2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
