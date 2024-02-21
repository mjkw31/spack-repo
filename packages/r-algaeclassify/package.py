# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlgaeclassify(RPackage):
	"""Tools to Standardize Phytoplankton Taxonomic Data and Perform
Functional Group Classifications

	Functions that facilitate the use of accepted taxonomic nomenclature, collection of
	functional trait data, and assignment of functional group classifications to phytoplankton
	species. Possible classifications include Morpho-functional group (MFG; Salmaso et al. 2015 
	<doi:10.1111/fwb.12520>) and CSR (Reynolds 1988; Functional morphology and the 
	adaptive strategies of phytoplankton. In C.D. Sandgren (ed). Growth and reproductive 
	strategies of freshwater phytoplankton, 388-433. Cambridge University Press, New York). 
	Versions 2.0.0 and later includes new functions for querying the 
	algaebase online taxonomic database (www.algaebase.org), however these functions require
	a valid API key that must be acquired from the algaebase admin. 
	Note that none of the algaeClassify authors are affiliated with algaebase in any way. Taxonomic 
	names can also be checked against a variety of taxonomic databases using 
	the geographic name resolution service (GNRS) via wrapper functions for the taxize package, 
	with convenient output format and unlikely names for phytoplankton taxa removed. In addition,
	currently accepted and outdated synonyms, and higher taxonomy, can be extracted for lists of 
	species from the ITIS database using wrapper functions for the ritis package.
	The algaeClassify package is a product of the GEISHA (Global Evaluation of the Impacts of 
	Storms on freshwater Habitat and Structure of phytoplankton Assemblages), funded by CESAB 
    (Centre for Synthesis and Analysis of Biodiversity) and the USGS John Wesley Powell Center for
	Synthesis and Analysis, with data and other support provided by members of GLEON 
	(Global Lake Ecology Observation Network). 
	DISCLAIMER: This software has been approved for release by the 
	U.S. Geological Survey (USGS). Although the software has been subjected to rigorous review, 
	the USGS reserves the right to update the software as needed pursuant to further analysis and 
	review. No warranty, expressed or implied, is made by the USGS or the U.S. Government as to the 
	functionality of the software and related material nor shall the fact of release constitute 
	any such warranty. Furthermore, the software is released on condition that neither the USGS 
	nor the U.S. Government shall be held liable for any damages resulting from its authorized 
	or unauthorized use.
	"""
	
	homepage = "https://doi.org/10.5066/F7S46Q3F"
	cran = "algaeClassify" 

	version("2.0.2", md5="6b28f249718207df29e26399b35dc18c")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-taxize", type=("build", "run"))
	depends_on("r-ritis", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
