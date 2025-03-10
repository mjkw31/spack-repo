# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapscape(RPackage):
	"""mapscape

	MapScape integrates clonal prevalence, clonal hierarchy, anatomic and mutational information to provide interactive visualization of spatial clonal evolution. There are four inputs to MapScape: (i) the clonal phylogeny, (ii) clonal prevalences, (iii) an image reference, which may be a medical image or drawing and (iv) pixel locations for each sample on the referenced image. Optionally, MapScape can accept a data table of mutations for each clone and their variant allele frequencies in each sample. The output of MapScape consists of a cropped anatomical image surrounded by two representations of each tumour sample. The first, a cellular aggregate, visually displays the prevalence of each clone. The second shows a skeleton of the clonal phylogeny while highlighting only those clones present in the sample. Together, these representations enable the analyst to visualize the distribution of clones throughout anatomic space.
	"""
	
	bioc = "mapscape" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/mapscape_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/mapscape/mapscape_1.26.0.tar.gz"]

	version("1.26.0", md5="dc197aa43e86dc49fef0d85d2ead252c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-htmlwidgets@0.5:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.19:", type=("build", "run"))
	depends_on("r-base64enc@0.1.3:", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
