# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntramirexplorer(RPackage):
	"""Predicting Targets for Drosophila Intragenic miRNAs

	Intra-miR-ExploreR, an integrative miRNA target prediction bioinformatics tool, identifies targets combining expression and biophysical interactions of a given microRNA (miR). Using the tool, we have identified targets for 92 intragenic miRs in D. melanogaster, using available microarray expression data, from Affymetrix 1 and Affymetrix2 microarray array platforms, providing a global perspective of intragenic miR targets in Drosophila. Predicted targets are grouped according to biological functions using the DAVID Gene Ontology tool and are ranked based on a biologically relevant scoring system, enabling the user to identify functionally relevant targets for a given miR.
	"""
	
	homepage = "https://github.com/VilainLab/IntramiRExploreR"
	bioc = "IntramiRExploreR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/IntramiRExploreR_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/IntramiRExploreR/IntramiRExploreR_1.24.0.tar.gz"]

	version("1.24.0", md5="e319d73695e5e1f12d9fc79896c49674")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-fgnet@3.0.7:", type=("build", "run"))
	depends_on("r-knitr@1.12.3:", type=("build", "run"))
