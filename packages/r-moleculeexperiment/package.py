# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoleculeexperiment(RPackage):
	"""Prioritising a molecule-level storage of Spatial Transcriptomics Data

	MoleculeExperiment contains functions to create and work with objects from the new MoleculeExperiment class. We introduce this class for analysing molecule-based spatial transcriptomics data (e.g., Xenium by 10X, Cosmx SMI by Nanostring, and Merscope by Vizgen). This allows researchers to analyse spatial transcriptomics data at the molecule level, and to have standardised data formats accross vendors.
	"""
	
	homepage = "https://github.com/SydneyBioX/MoleculeExperiment"
	bioc = "MoleculeExperiment" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MoleculeExperiment_1.2.2.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MoleculeExperiment/MoleculeExperiment_1.2.2.tar.gz"]

	version("1.2.2", md5="d8fef705349bc9464ae152cd47bb9a58")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr@1.1.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
