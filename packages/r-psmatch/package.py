# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsmatch(RPackage):
	"""Handling and Managing Peptide Spectrum Matches

	The PSMatch package helps proteomics practitioners to load, handle and manage Peptide Spectrum Matches. It provides functions to model peptide-protein relations as adjacency matrices and connected components, visualise these as graphs and make informed decision about shared peptide filtering. The package also provides functions to calculate and visualise MS2 fragment ions.
	"""
	
	homepage = "https://github.com/RforMassSpectrometry/PSM"
	bioc = "PSMatch" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/PSMatch_1.6.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/PSMatch/PSMatch_1.6.0.tar.gz"]

	version("1.6.0", md5="4c63ca3d541af4e5925bcc2bde7d67ea")

	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-protgenerics@1.27.1:", type=("build", "run"))
	depends_on("r-qfeatures", type=("build", "run"))
	depends_on("r-mscoreutils", type=("build", "run"))
